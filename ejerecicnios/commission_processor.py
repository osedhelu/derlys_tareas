import psycopg2
import sys

def actualizar_comision_y_crear_nueva(config_db, id_comision_base, nuevo_monto):
    """
    Conecta a PostgreSQL, elimina comisiones existentes basadas en el investment_id
    de una comisión base, y crea una nueva comisión con un monto especificado.

    Args:
        config_db (dict): Diccionario con los parámetros de conexión a la BD
                          (e.g., {'host': 'localhost', 'dbname': 'nombre_db', 
                                  'user': 'usuario_db', 'password': 'password_db', 'port': 5432}).
        id_comision_base (int): El ID de la comisión que se usará como base para
                                obtener el investment_id y la descripción.
        nuevo_monto (float): El monto para la nueva comisión a crear.

    Returns:
        int: El ID de la nueva comisión creada si la operación es exitosa, None en caso contrario.
    """
    conn = None
    cur = None
    new_commission_id_returned = None
    notices_list = []

    # SQL para establecer variables de sesión
    sql_set_id_var = "SET SESSION my.vars.id = %s;"
    sql_set_amount_var = "SET SESSION my.vars.amount = %s;"

    # Bloque DO principal (similar al proporcionado por el usuario)
    # Se añade una forma de recuperar el ID de la nueva comisión a través de una variable de sesión.
    sql_do_block = """
DO $$
DECLARE
    v_base_commission_id INT;
    v_investment_id INT;
    v_description TEXT;
    v_amount NUMERIC;
    v_new_commission_id INT;
BEGIN
    -- Obtener valores de las variables de sesión
    v_base_commission_id := current_setting('my.vars.id')::INT;
    v_amount := current_setting('my.vars.amount')::NUMERIC;

    -- Obtener investment_id y description de la comisión base
    SELECT investment_id, description
    INTO v_investment_id, v_description
    FROM commissions
    WHERE id = v_base_commission_id;

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Comisión base con ID % no encontrada.', v_base_commission_id;
    END IF;

    RAISE NOTICE 'Comisión base encontrada: investment_id=%, description=%', v_investment_id, v_description;

    -- 1. Eliminar todas las comisiones que pertenecen al investment_id obtenido
    RAISE NOTICE 'Eliminando comisiones para investment_id: %', v_investment_id;
    DELETE FROM commissions WHERE investment_id = v_investment_id;
    RAISE NOTICE 'Verificación post-eliminación: % comisiones restantes para investment_id %.', 
                 (SELECT count(*) FROM commissions WHERE investment_id = v_investment_id), v_investment_id;

    -- 2. Crear una nueva comisión
    RAISE NOTICE 'Creando nueva comisión para investment_id: % con amount: %', v_investment_id, v_amount;
    INSERT INTO commissions (
        investment_id,
        description,
        amount,
        document_id,
        published_at,
        created_by_id,
        updated_by_id,
        locale,
        statu,
        created_at,
        updated_at
    ) VALUES (
        v_investment_id,
        v_description,
        v_amount,
        NULL,           -- Ajustar si es necesario
        NULL,           -- Ajustar si es necesario (ej. NOW() o NULL)
        2,              -- Ajustar ID de usuario creador si es necesario
        2,              -- Ajustar ID de usuario actualizador si es necesario
        'es_ES',        -- Ajustar locale si es necesario
        'Cierre de comisiones suma de total de comisiones', -- Revisar si este valor de 'statu' es correcto
        NOW(),
        NULL            -- updated_at usualmente es NULL en creación o manejado por triggers
    ) RETURNING id INTO v_new_commission_id;

    RAISE NOTICE 'Nueva comisión creada con ID: %', v_new_commission_id;

    -- Guardar el ID de la nueva comisión en una variable de sesión para recuperarlo en Python
    PERFORM set_config('my.vars.new_commission_id_result', v_new_commission_id::TEXT, false);

END $$;
    """

    # SQL para obtener el ID de la nueva comisión desde la variable de sesión
    sql_get_new_id_result = "SELECT current_setting('my.vars.new_commission_id_result', true)::INT;"

    try:
        # Establecer conexión
        conn = psycopg2.connect(**config_db)
        
        # Función para capturar notices de PostgreSQL
        def psycopg2_notice_handler(notice):
            notices_list.append(notice.message) # psycopg2 >= 2.8, notice es un objeto Diagnostic
                                                # para versiones anteriores, puede ser un string.
                                                # Ajustar si es necesario.
        
        conn.add_notice_receiver(psycopg2_notice_handler)
        
        cur = conn.cursor()

        # Establecer variables de sesión con los parámetros
        print(f"DEBUG: Estableciendo my.vars.id = '{id_comision_base}'")
        cur.execute(sql_set_id_var, (str(id_comision_base),))
        
        print(f"DEBUG: Estableciendo my.vars.amount = '{nuevo_monto}'")
        cur.execute(sql_set_amount_var, (str(nuevo_monto),))

        # Ejecutar el bloque DO
        print("DEBUG: Ejecutando el bloque DO principal...")
        cur.execute(sql_do_block)
        
        # Recuperar el ID de la nueva comisión creada
        cur.execute(sql_get_new_id_result)
        result = cur.fetchone()
        if result:
            new_commission_id_returned = result[0]
            print(f"DEBUG: ID de nueva comisión recuperado: {new_commission_id_returned}")

        # Confirmar la transacción
        conn.commit()
        print("Transacción completada exitosamente.")

    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        print(f"Error de base de datos: {e}", file=sys.stderr)
        print(f"Detalles del error de PostgreSQL: {e.pgcode} {e.pgerror}", file=sys.stderr)
        new_commission_id_returned = None
    except Exception as e:
        if conn:
            conn.rollback() # Asegurarse de hacer rollback en otros errores si la conexión está activa
        print(f"Un error inesperado ocurrió: {type(e).__name__} - {e}", file=sys.stderr)
        new_commission_id_returned = None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            print("Conexión a la base de datos cerrada.")
        
        # Imprimir todos los notices recibidos de PostgreSQL
        if notices_list:
            print("\\nMensajes NOTICE de PostgreSQL:")
            for notice_msg in notices_list:
                print(f"- {notice_msg.strip()}")
    
    return new_commission_id_returned

# Ejemplo de cómo usar la función:
if __name__ == "__main__":
    # --- IMPORTANTE: CONFIGURACIÓN DE LA BASE DE DATOS ---
    # Reemplaza estos valores con los de tu base de datos PostgreSQL
    db_parameters = {
        'dbname': 'nombre_tu_db',    # Nombre de tu base de datos
        'user': 'tu_usuario_db',     # Usuario de la base de datos
        'password': 'tu_contraseña', # Contraseña del usuario
        'host': 'localhost',         # Host de la base de datos (e.g., 'localhost' o una IP)
        'port': '5432'               # Puerto de PostgreSQL (usualmente 5432)
    }

    # --- PARÁMETROS PARA LA OPERACIÓN ---
    # Estos son los valores que le pasarías a la función.
    # El 'id_comision_base_param' corresponde al 'my.vars.id' en tu script SQL.
    # El 'nuevo_monto_param' corresponde al 'my.vars.amount'.
    
    id_comision_base_param = 13940  # Reemplaza con un ID de comisión base de prueba
    nuevo_monto_param = 57.01       # Reemplaza con un monto de prueba

    print(f"Iniciando proceso para comisión base ID: {id_comision_base_param}, nuevo monto: {nuevo_monto_param}\\n")
    
    # Validar si la configuración de la BD fue actualizada antes de ejecutar
    if db_parameters['dbname'] == 'nombre_tu_db' or \
       db_parameters['user'] == 'tu_usuario_db' or \
       db_parameters['password'] == 'tu_contraseña':
        print("!!! ADVERTENCIA !!!")
        print("Por favor, actualiza los parámetros de conexión a la base de datos (db_parameters)")
        print("en la sección `if __name__ == \"__main__\":` de este script.")
        print("El script no se ejecutará con la configuración por defecto.\n")
    else:
        # Llamada a la función principal
        id_nueva_comision = actualizar_comision_y_crear_nueva(
            db_parameters, 
            id_comision_base_param, 
            nuevo_monto_param
        )

        if id_nueva_comision is not None:
            print(f"\\nProceso finalizado. Nueva comisión creada con éxito. ID: {id_nueva_comision}")
        else:
            print("\\nEl proceso de actualización de comisiones falló. Revisa los mensajes de error anteriores.") 
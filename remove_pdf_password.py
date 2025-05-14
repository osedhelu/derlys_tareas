import os
from PyPDF2 import PdfReader, PdfWriter

def remove_pdf_password(input_path, password):
    """
    Elimina la contraseña de un archivo PDF.
    
    Args:
        input_path (str): Ruta completa del archivo PDF
        password (str): Contraseña del PDF
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(input_path):
            print("Error: El archivo no existe")
            return False
            
        # Crear el nombre del archivo de salida
        output_path = os.path.splitext(input_path)[0] + "_sin_password.pdf"
        
        # Abrir el PDF con la contraseña
        reader = PdfReader(input_path)
        if reader.is_encrypted:
            reader.decrypt(password)
        
        # Crear un nuevo PDF sin contraseña
        writer = PdfWriter()
        
        # Copiar todas las páginas al nuevo PDF
        for page in reader.pages:
            writer.add_page(page)
        
        # Guardar el nuevo PDF sin contraseña
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
            
        print(f"Archivo procesado exitosamente: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error al procesar el archivo: {str(e)}")
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Pedir la ruta del archivo al usuario
    file_path = input("Ingrese la ruta completa del archivo PDF: ")
    
    # Contraseña predefinida
    password = "1127579854"
    
    # Llamar a la función para eliminar la contraseña
    remove_pdf_password(file_path, password) 
import os
from PIL import Image

def listar_formatos_soportados():
    """Muestra los formatos de imagen soportados"""
    formatos = ["JPG", "JPEG", "PNG", "GIF", "BMP", "TIFF", "WEBP"]
    print("Formatos soportados:")
    for formato in formatos:
        print(f"- {formato}")
    return formatos

def convertir_imagen(ruta_imagen, formato_salida, carpeta_destino=None):
    """Convierte una imagen al formato especificado
    
    Args:
        ruta_imagen: Ruta de la imagen a convertir
        formato_salida: Formato al que se convertira (ej: PNG)
        carpeta_destino: Carpeta donde se guardara la imagen convertida (opcional)
        
    returns:
        str: Ruta de la imagen convertida
    """
    try:
        # Verificar que la imagen exista
        if not os.path.exists(ruta_imagen):
            print(f"Error: la imagen '{ruta_imagen}' no existe.")
            return None
        
        # Abrir la imagen
        imagen = Image.open(ruta_imagen)

        # Obtener información de la imagen original
        nombre_archivo = os.path.basename(ruta_imagen)
        nombre_base = os.path.splitext(nombre_archivo)[0]

        # Determinar la carpeta de destino
        if carpeta_destino is None:
            carpeta_destino = os.path.dirname(ruta_imagen)

        # Crear carpeta de destino si no existe
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)

        # Crear la ruta de salida
        formato_salida = formato_salida.lower().strip(".")
        ruta_salida = os.path.join(carpeta_destino, f"{nombre_base}.{formato_salida}")

        # Guardar la imagen en el nuevo formato
        imagen.save(ruta_salida)
        print(f"Imagen convertida y guardada en: {ruta_salida}")

        return ruta_salida
    
    except Exception as e:
        print(f"Error al convertir la imagen: {e}")
        return None

def convertir_multiples_imagenes(carpeta_origen, formato_salida, carpeta_destino=None):
    """Convierte todas las imagenes en una carpeta al formato especificado
    
    Args:
        carpeta_origne: Carpeta que contiene las imagenes a convertir
        formato_salida: Formato al que se convertiran las imagenes (ej: PNG)
        carpeta_destino: Carpeta donde se guardaran las imagenes convertidas (opcional)
        
    returns:
        int: Numero ded imagenes convertidas
    """
    # Verificar que la carpeta existe
    if not os.path.exists(carpeta_origen):
        print(f"Error: La carpeta '{carpeta_origen}' no existe.")
        return 0
    
    # Extensiones de imágenes comunes
    extensiones_imagenes = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]

    # Contador de imágenes convertidas
    contador = 0

    # Recorrer todos los archivos de la carpeta
    for archivo in os.listdir(carpeta_origen):
        ruta_archivo = os.path.join(carpeta_origen, archivo)

        # Verificar si es un archivo y tiene extensión de imagen
        if os.path.isfile(ruta_archivo) and any(archivo.lower().endswith(ext) for ext in extensiones_imagenes):
            # Convertir la imagen
            if convertir_imagen(ruta_archivo, formato_salida, carpeta_destino):
                contador += 1

    return contador

def mostrar_menu():
    """Muestra el menú de opciones al usuario"""
    print("\n=== CONVERSOR DE IMÁGENES ===")
    print("Opciones:")
    print("1. Convertir una imagen")
    print("2. Convertir todas las imágenes en una carpeta")
    print("3. Salir")

def main():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-3): ")

        if opcion == "1":
            # Convertir una sola imagen
            ruta_imagen = input("Ingresa la ruta de la imagen a convertir: ")
            formato_salida = input("Ingresa el formato de salida (ej: PNG): ")
            carpeta_destino = input("Ingresa la carpeta de destino (opcional, deja en blanco para usar la misma carpeta): ")

            if not carpeta_destino:
                carpeta_destino = None

            convertir_imagen(ruta_imagen, formato_salida, carpeta_destino)

        elif opcion == "2":
            # Convertir múltiples imágenes
            carpeta_origen = input("Ingresa la ruta de la carpeta con las imágenes: ")
            formato_salida = input("Ingresa el formato de salida (ej: PNG): ")
            carpeta_destino = input("Ingresa la carpeta de destino (opcional, deja en blanco para usar la misma carpeta): ")

            if not carpeta_destino:
                carpeta_destino = None

            num_convertidas = convertir_multiples_imagenes(carpeta_origen, formato_salida, carpeta_destino)
            print(f"\nSe convirtieron {num_convertidas} imágenes exitosamente.")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()

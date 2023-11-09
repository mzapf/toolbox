#!/usr/bin/env python3
import os
import sys
import pyperclip

# Script para recopilar el contenido de archivos y directorios pasados como argumentos.
# Si el argumento es un archivo, agrega su contenido al portapapeles.
# Si el argumento es un directorio, agrega el contenido de todos los archivos dentro del directorio al portapapeles.
# Después de procesar todos los argumentos, el contenido recopilado se copia al portapapeles listo para ser pegado en cualquier lugar.
# Cada archivo se separa por una línea en blanco para mantener el contenido claramente diferenciado.


def process_path(path, buffer):
    # Procesa un archivo o directorio y agrega su contenido al buffer
    if os.path.isfile(path):
        with open(path, "r") as file:
            buffer.append(
                f"```{path}\n{file.read()}```\n"
            )  # Agrega el contenido del archivo al buffer
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "r") as file:
                    buffer.append(
                        f"```{file_path}\n{file.read()}```\n"
                    )  # Agrega el contenido de cada archivo en el directorio al buffer
    else:
        print(f"{path} no es un archivo o directorio válido.")


# Verifica si se pasaron argumentos al script
if len(sys.argv) > 1:
    buffer = []

    # Recorre todos los argumentos pasados al script y los procesa
    for arg in sys.argv[1:]:
        process_path(arg, buffer)

    # Si hay contenido en el buffer, lo copia al portapapeles
    if buffer:
        pyperclip.copy("\n".join(buffer))
        print("El contenido ha sido copiado al portapapeles.")
else:
    print(f"Uso: python3 {sys.argv[0]} [archivo/directorio] ...")

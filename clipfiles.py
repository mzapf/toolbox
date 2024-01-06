#!/usr/bin/env python3
import os
import sys
import pyperclip


def is_binary(file_path):
    """
    Determina si un archivo dado es binario o no leyendo un bloque de su contenido.
    Un archivo se considera binario si contiene un cierto porcentaje de caracteres no imprimibles.
    """
    try:
        with open(file_path, "rb") as file:
            chunk = file.read(1024)  # Lee los primeros 1024 bytes
            if b"\0" in chunk:  # Si hay un null byte, asume que es binario
                return True
            text_characters = bytearray(
                {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F}
            )
            return bool(chunk.translate(None, text_characters))
    except Exception as e:
        print(f"No se pudo leer {file_path}: {e}")
        return False


def process_path(path, buffer):
    # Procesa un archivo o directorio y agrega su contenido al buffer
    if os.path.isfile(path) and not is_binary(path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                buffer.append(
                    f"```{path}\n{file.read()}```\n"
                )  # Agrega el contenido del archivo al buffer
        except Exception as e:
            print(f"No se pudo leer {file_path}: {e}")
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            # Si '.git' está en el camino, salta este directorio y continúa con el siguiente
            if ".git" in root.split(os.sep):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if not is_binary(file_path):
                    try:
                        with open(
                            file_path, "r", encoding="utf-8", errors="ignore"
                        ) as file:
                            buffer.append(
                                f"```{file_path}\n{file.read()}```\n"
                            )  # Agrega el contenido de cada archivo en el directorio al buffer
                    except Exception as e:
                        print(f"No se pudo leer {file_path}: {e}")
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

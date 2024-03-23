#!/usr/bin/env python3

"""
clipfiles.py: Un script para recopilar el contenido de archivos y directorios especificados
y copiarlo al portapapeles. Es útil para compilar rápidamente información de múltiples fuentes,
como parte de procesos de documentación, revisión de código, o diagnóstico.

El script ignora archivos binarios y permite especificar archivos o directorios para ignorar,
facilitando la recopilación precisa de datos de texto. El contenido recopilado se formatea
en bloques de código Markdown, facilitando su inclusión en documentaciones o informes.

Requisitos:
- Python 3.x
- pyperclip: Una biblioteca para acceder al portapapeles en múltiples plataformas. Instalación vía pip: `pip install pyperclip`

Uso:
./clipfiles.py path1 [path2 ...] [-i ignore1 [ignore2 ...]]

Argumentos:
- path: Uno o más archivos o directorios para procesar. Se recopilará y copiará el contenido de estos archivos/directorios.
- -i, --ignore: Opcional. Uno o más archivos o directorios a ignorar durante el procesamiento.

Ejemplo de uso:
./clipfiles.py /path/to/project/**/*.py -i venv/ __pycache__/
"""

import os
import argparse
import pyperclip


def is_binary(file_path):
    """
    Determina si un archivo es binario o no.

    :param file_path: Ruta al archivo a verificar.
    :return: True si el archivo es binario, False de lo contrario.
    """
    try:
        with open(file_path, "rb") as file:
            chunk = file.read(1024)
            if b"\0" in chunk:
                return True
            text_characters = bytearray(
                {7, 8, 9, 10, 12, 13, 27} | set(range(0x20, 0x100)) - {0x7F}
            )
            return bool(chunk.translate(None, text_characters))
    except Exception as e:
        print(f"No se pudo leer {file_path}: {e}")
        return False


def should_ignore(path, base_path, ignore_list):
    """
    Determina si un archivo o directorio debe ser ignorado basado en la lista de ignorados.

    :param path: Ruta al archivo o directorio a verificar.
    :param base_path: Ruta base desde donde se ejecuta el script.
    :param ignore_list: Lista de archivos o directorios a ignorar.
    :return: True si el archivo o directorio debe ser ignorado, False de lo contrario.
    """
    absolute_path = os.path.abspath(path)
    for ignore in ignore_list:
        ignore_abs = os.path.abspath(os.path.join(base_path, ignore))
        if absolute_path == ignore_abs or absolute_path.startswith(ignore_abs + os.sep):
            return True
    return False


def process_path(base_path, path, buffer, ignore_list):
    """
    Procesa un archivo o directorio, recopilando su contenido si es texto y no está ignorado.

    :param base_path: Ruta base desde donde se ejecuta el script.
    :param path: Ruta al archivo o directorio a procesar.
    :param buffer: Lista donde se acumula el contenido recopilado.
    :param ignore_list: Lista de archivos o directorios a ignorar.
    """
    if (
        os.path.isfile(path)
        and not is_binary(path)
        and not should_ignore(path, base_path, ignore_list)
    ):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                buffer.append(f"```{path}\n{file.read()}```\n")
        except Exception as e:
            print(f"No se pudo leer {path}: {e}")
    elif os.path.isdir(path) and not should_ignore(path, base_path, ignore_list):
        for root, dirs, files in os.walk(path):
            if ".git" in root.split(os.sep):
                continue
            for file in files:
                file_path = os.path.join(root, file)
                if not is_binary(file_path) and not should_ignore(
                    file_path, base_path, ignore_list
                ):
                    try:
                        with open(
                            file_path, "r", encoding="utf-8", errors="ignore"
                        ) as file:
                            buffer.append(f"```{file_path}\n{file.read()}```\n")
                    except Exception as e:
                        print(f"No se pudo leer {file_path}: {e}")
    else:
        print(f"{path} no es un archivo o directorio válido.")


def main():
    """
    Función principal del script. Parsea argumentos de la línea de comandos, procesa los archivos
    y directorios especificados, y copia el contenido recopilado al portapapeles.
    """
    parser = argparse.ArgumentParser(
        description="Recopila contenido de archivos y directorios para copiar al portapapeles."
    )
    parser.add_argument(
        "paths",
        metavar="path",
        type=str,
        nargs="+",
        help="archivos o directorios para procesar",
    )
    parser.add_argument(
        "-i", "--ignore", nargs="*", help="archivos o rutas a ignorar", default=[]
    )

    args = parser.parse_args()

    buffer = []  # Almacena el contenido recopilado de los archivos

    for path in args.paths:
        base_path = os.path.abspath(path)
        process_path(base_path, path, buffer, args.ignore)

    if buffer:
        content_to_clip = "\n".join(buffer)
        pyperclip.copy(content_to_clip)
        print("El contenido ha sido copiado al portapapeles.")
    else:
        print("No hay contenido para copiar.")


if __name__ == "__main__":
    main()

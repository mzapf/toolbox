#!/usr/bin/env python3
import os
import sys
import argparse
import pyperclip


def is_binary(file_path):
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
    absolute_path = os.path.abspath(path)
    for ignore in ignore_list:
        ignore_abs = os.path.abspath(os.path.join(base_path, ignore))
        if absolute_path == ignore_abs or absolute_path.startswith(ignore_abs + os.sep):
            return True
    return False


def process_path(base_path, path, buffer, ignore_list):
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

    buffer = []

    for path in args.paths:
        base_path = os.path.abspath(path)
        process_path(base_path, path, buffer, args.ignore)

    if buffer:
        pyperclip.copy("\n".join(buffer))
        print("El contenido ha sido copiado al portapapeles.")
    else:
        print("No hay contenido para copiar.")


if __name__ == "__main__":
    main()

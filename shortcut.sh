#!/bin/bash

# Este script crea un enlace simbólico de un archivo en /usr/local/bin.
# Esto permite ejecutar el archivo como un comando global en el sistema.
# Uso: ./shortcut.sh <ruta_al_archivo> <nombre_comando>

# Verifica que se proporcionen exactamente dos argumentos: la ruta al archivo y el nombre del comando
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <ruta_al_archivo> <nombre_comando>"
    exit 1
fi

# Asigna los argumentos a variables para un mejor manejo
FILE_PATH=$1
COMMAND_NAME=$2

# Utiliza realpath para obtener la ruta absoluta del archivo
ABSOLUTE_PATH=$(realpath "$FILE_PATH")

# Verifica si el archivo existe
if [ ! -f "$ABSOLUTE_PATH" ]; then
    echo "Error: El archivo $FILE_PATH no existe."
    exit 1
fi

# Da permisos de ejecución al archivo
chmod +x "$ABSOLUTE_PATH"

# Crea un enlace simbólico en /usr/local/bin para que el archivo sea accesible globalmente
sudo ln -s "$ABSOLUTE_PATH" /usr/local/bin/"$COMMAND_NAME"
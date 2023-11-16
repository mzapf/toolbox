#!/bin/bash

# Este script crea un enlace simbólico de un archivo Python en /usr/local/bin.
# Esto permite ejecutar el script de Python como un comando global en el sistema.
# Uso: ./easy-link.sh <archivo_python> <nombre_comando>

# Verifica que se proporcionen exactamente dos argumentos: el archivo y el nombre del comando
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <archivo_python> <nombre_comando>"
    exit 1
fi

# Asigna los argumentos a variables para un mejor manejo
PYTHON_FILE=$1
COMMAND_NAME=$2

# Obtiene el directorio actual para asegurarse de que el archivo Python está en este directorio
CURRENT_DIR=$(pwd)

# Verifica si el archivo Python existe en el directorio actual
if [ ! -f "$CURRENT_DIR/$PYTHON_FILE" ]; then
    echo "Error: El archivo $PYTHON_FILE no existe en el directorio actual."
    exit 1
fi

# Verifica si el archivo tiene la extensión .py para asegurarse de que es un script de Python
if [[ $PYTHON_FILE != *.py ]]; then
    echo "Error: El archivo $PYTHON_FILE no es un script de Python."
    exit 1
fi

# Da permisos de ejecución al archivo Python
chmod +x $CURRENT_DIR/$PYTHON_FILE

# Crea un enlace simbólico en /usr/local/bin para que el script Python sea accesible globalmente
sudo ln -s $CURRENT_DIR/$PYTHON_FILE /usr/local/bin/$COMMAND_NAME

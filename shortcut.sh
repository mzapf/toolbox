#!/bin/bash

# Este script crea un enlace simbólico de cualquier archivo ejecutable en /usr/local/bin,
# permitiendo su ejecución global como si fuera un comando del sistema. Facilita la ejecución
# repetitiva y en cualquier directorio de herramientas o scripts frecuentemente utilizados,
# al no necesitar navegar al directorio del archivo o especificar su ruta completa.

# Uso:
# ./shortcut.sh <ruta_al_archivo> <nombre_comando>
# Donde:
# - <ruta_al_archivo> es la ruta al archivo que deseas hacer accesible globalmente.
# - <nombre_comando> es el nombre bajo el cual deseas invocar este archivo desde cualquier lugar.

# Ejemplos:
# Para hacer un script Python ejecutable globalmente:
# ./shortcut.sh /path/to/myscript.py myscript
# Ahora, puedes ejecutar 'myscript' desde cualquier lugar en tu terminal.

# Para un script bash:
# ./shortcut.sh /path/to/myscript.sh myscript
# Similarmente, 'myscript' estará disponible globalmente.

# Requisitos previos:
# - Tener instalado 'realpath' para resolver rutas absolutas.
# - Tener permisos de superusuario (sudo) para crear enlaces en /usr/local/bin.

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
# Esto implica que se necesita tener permisos de administrador para ejecutar este paso.
sudo ln -s "$ABSOLUTE_PATH" /usr/local/bin/"$COMMAND_NAME"

# Indica al usuario que el comando ha sido configurado exitosamente.
echo "El comando '$COMMAND_NAME' ha sido configurado y está listo para usarse globalmente."

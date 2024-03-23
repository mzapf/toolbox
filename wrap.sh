#!/bin/bash

# Este script formatea texto copiado al portapapeles a un ancho especificado y lo prepara para ser comentado
# en código (por defecto usando "// " al inicio de cada línea). Es útil para documentar código fuente o para
# preparar texto para ser insertado en comentarios dentro del código. El texto formateado se copia de nuevo al
# portapapeles, facilitando su uso inmediato.

# Uso:
# ./wrap.sh [ancho]
# [ancho] es opcional. Si no se proporciona, se utiliza un valor predeterminado de 60.

# Parámetros:
# ancho: El ancho deseado para el texto formateado. El valor predeterminado es 60.

# Dependencias:
# - xclip: Herramienta para manejar el portapapeles en sistemas basados en X11.
# - fmt: Herramienta para formatear texto a un ancho específico.

# Establece un ancho predeterminado. Resta 3 al ancho para compensar los caracteres adicionales "// ".
# Esto asegura que el texto formateado no exceda el ancho deseado cuando se le añaden los caracteres "// ".
ancho=${1:-60}
let ancho=ancho-3

# Lee el texto del portapapeles.
# Utiliza `xclip` con la opción `-o` para emitir el contenido del portapapeles y `-selection clipboard`
# para especificar que se debe usar el portapapeles del sistema en lugar del portapapeles primario de X11.
texto=$(xclip -o -selection clipboard)

# Formatea el texto al ancho especificado y agrega "// " al inicio de cada línea.
# Primero, `fmt -w $ancho` formatea el texto a la anchura especificada.
# Luego, `sed 's/^/\/\/ /'` añade "// " al inicio de cada línea del texto formateado.
texto_formateado=$(echo "$texto" | fmt -w $ancho | sed 's/^/\/\/ /')

# Copia el texto formateado de vuelta al portapapeles.
# Usa `echo` para emitir el texto formateado y pipearlo a `xclip -selection clipboard` para copiarlo al portapapeles.
echo "$texto_formateado" | xclip -selection clipboard

# Nota: Este script está diseñado para ser usado en entornos Linux/Unix.
# Puede requerir modificaciones para trabajar en otros entornos o sistemas operativos.


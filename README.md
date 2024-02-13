# toolbox

## Descripción
Toolbox es un repositorio que contiene una serie de scripts diseñados para simplificar y automatizar tareas comunes en el entorno de desarrollo. Ideal para desarrolladores y usuarios que buscan mejorar su eficiencia y flujo de trabajo.

## Scripts

### clipfiles.py

- **Función**: Recopila contenido de archivos y directorios especificados y lo copia al portapapeles. Ideal para recoger rápidamente datos de múltiples archivos para documentación o revisión.
- **Características**:
    - Ignora archivos binarios.
    - Permite especificar archivos o directorios a ignorar.
    - Soporte para múltiples rutas y patrones.

#### Requisitos

- **Python**: Python 3.x.
- **Dependencias**: `pyperclip` (puede instalarse vía `pip` con `pip install pyperclip`).
- **Sistema Operativo**: Compatible con sistemas basados en Unix.

#### Ejemplos de uso

```bash
# Copiar todos los archivos Python de un proyecto para revisión:
./clipfiles.py /path/to/project/**/*.py

# Recopilar y copiar scripts de configuración excluyendo directorios de entorno virtual:
./clipfiles.py /path/to/configs/ -i venv/ __pycache__/

# Copiar contenido de archivos de log para diagnóstico rápido:
./clipfiles.py /var/log/nginx/error.log /var/log/app/error.log

# Recopilar scripts de SQL de un directorio para revisión antes de la ejecución:
./clipfiles.py /path/to/sql/scripts/

# Reunir todos los archivos de configuración de Docker de un proyecto:
./clipfiles.py /path/to/project/Dockerfile /path/to/project/docker-compose.yml
```

### shortcut.sh

- **Función**: Crea un enlace simbólico de cualquier archivo ejecutable en /usr/local/bin, permitiendo su ejecución global como si fuera un comando del sistema. Esto facilita la ejecución repetitiva y en cualquier directorio de herramientas o scripts frecuentemente utilizados.
- **Características**:
    - Funciona con cualquier tipo de archivo ejecutable.
    - No se limita a scripts Python, permitiendo una mayor flexibilidad.
    - Configura los permisos adecuados y establece el enlace simbólico.

#### Requisitos

- **Shell**: Bash.
- **Sistema Operativo**: Compatible con sistemas basados en Unix (requiere /usr/local/bin o un equivalente para enlaces simbólicos).
- **Permisos**: Necesita permisos sudo.

#### Ejemplos de uso

```bash
# Crear un comando global de este mismo script:
./shortcut.sh ./shortcut.sh sc

# Crear un enlace global para un script de deployment:
./shortcut.sh /path/to/deploy_app deployapp

# Hacer accesible un script de limpieza de logs en todo el sistema:
./shortcut.sh /path/to/clean_logs cleanlogs

# Establecer un comando global para iniciar servicios con Docker:
./shortcut.sh /path/to/docker_start dstart

# Configurar un comando personalizado para ejecutar tests unitarios:
./shortcut.sh /path/to/run_tests unittests

# Habilitar un script de monitoreo de sistema para ser ejecutado desde cualquier lugar:
./shortcut.sh /path/to/system_monitor sysmon
```

## Contribuir

Se invita a los contribuyentes a colaborar con el desarrollo de estos scripts. Si tienes ideas o mejoras, no dudes en hacer un fork y enviar un pull request.
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

Copiar todos los archivos Python de un proyecto para revisión:

```bash
./clipfiles.py /path/to/project/**/*.py
```

Recopilar y copiar scripts de configuración excluyendo directorios de entorno virtual:

```bash
./clipfiles.py /path/to/configs/ -i venv/ __pycache__/
```

Copiar contenido de archivos de log para diagnóstico rápido:

```bash
./clipfiles.py /var/log/nginx/error.log /var/log/app/error.log
```

Recopilar scripts de SQL de un directorio para revisión antes de la ejecución:

```bash
./clipfiles.py /path/to/sql/scripts/
```

Reunir todos los archivos de configuración de Docker de un proyecto:

```bash
./clipfiles.py /path/to/project/Dockerfile /path/to/project/docker-compose.yml
```

### easy-link.sh

- **Función**: Crea un enlace simbólico de un script Python en `/usr/local/bin`, permitiendo su ejecución global como si fuera un comando del sistema. Facilita la ejecución repetitiva y en cualquier directorio de scripts frecuentemente utilizados.
- **Características**:
    - Verifica la existencia del script y su ubicación.
    - Asegura que el archivo tiene la extensión .py.
    - Configura los permisos adecuados y establece el enlace simbólico.

#### Requisitos

- **Shell**: Bash.
- **Sistema Operativo**: Compatible con sistemas basados en Unix (requiere `/usr/local/bin` o un equivalente para enlaces simbólicos).
- **Permisos**: Necesita permisos `sudo`.

#### Ejemplos de uso

Crear un enlace global para un script de deployment:

```bash
./easy-link.sh deploy_app.py deployapp
```

Hacer accesible un script de limpieza de logs en todo el sistema:

```bash
./easy-link.sh clean_logs.py cleanlogs
```

Establecer un comando global para iniciar servicios con Docker:

```bash
./easy-link.sh docker_start.py dstart
```

Configurar un comando personalizado para ejecutar tests unitarios:

```bash
./easy-link.sh run_tests.py unittests
```

Habilitar un script de monitoreo de sistema para ser ejecutado desde cualquier lugar:

```bash
./easy-link.sh system_monitor.py sysmon
```

## Contribuir
Se invita a los contribuyentes a colaborar con el desarrollo de estos scripts. Si tienes ideas o mejoras, no dudes en hacer un fork y enviar un pull request.

---

Este repositorio está destinado a facilitar tareas comunes de desarrollo y gestión de archivos. Siéntete libre de utilizar y adaptar estos scripts según tus necesidades.


# toolbox

## Descripción
Toolbox es un repositorio que contiene una serie de scripts diseñados para simplificar y automatizar tareas comunes en el entorno de desarrollo. Ideal para desarrolladores y usuarios que buscan mejorar su eficiencia y flujo de trabajo.

### Scripts Incluidos

1. **clipfiles.py**: Un script de Python que facilita la recopilación de contenidos de archivos y directorios. Es útil para copiar rápidamente el contenido al portapapeles, ya sea un archivo individual o todos los archivos dentro de un directorio específico.

2. **easy-link.sh**: Un script de Bash que crea enlaces simbólicos de scripts de Python en `/usr/local/bin`. Esto permite ejecutar cualquier script de Python como si fuera un comando global en el sistema, mejorando la accesibilidad y la eficiencia.

## Uso

### clipfiles.py
Para usar `clipfiles.py`, ejecute el script con la ruta del archivo o directorio como argumento. Por ejemplo:

```python3
clipfiles.py /ruta/al/archivo
```

Esto copiará el contenido del archivo o directorio especificado en el portapapeles.

### easy-link.sh
Para crear un enlace simbólico para un script de Python, utilice `easy-link.sh` de la siguiente manera:

```bash
./easy-link.sh mi_script.py mi_comando
```

Esto creará un enlace simbólico en `/usr/local/bin`, permitiendo ejecutar `mi_script.py` usando `mi_comando` desde cualquier lugar en el sistema.

## Requisitos
- Python para `clipfiles.py`.
- Bash y privilegios de administrador para `easy-link.sh`.

## Contribuir
Se invita a los contribuyentes a colaborar con el desarrollo de estos scripts. Si tienes ideas o mejoras, no dudes en hacer un fork y enviar un pull request.

---

Este repositorio está destinado a facilitar tareas comunes de desarrollo y gestión de archivos. Siéntete libre de utilizar y adaptar estos scripts según tus necesidades.


# Actividad Unidad 1 — Sandboxing
---

## Documento donde se explica como se ejecuta lo de nota en Sanboxing (Firejail y Firetools)

### 1. Instalar Firejail y Firetools

```bash
# En Debian/Ubuntu
sudo apt update
sudo apt install -y firejail firetools

# Verificar instalación
firejail --version
```

> Nota: `firetools` proporciona una interfaz gráfica para Firejail; no es estrictamente necesaria si prefieres la línea de comandos.

### 2. Preparar la aplicación

Supongamos que estás en `~/proyecto-nota` y que `nota.py` (o la app extraída) está presente.

```bash
cd ~/proyecto-nota
ls -la nota.py
python3 --version
```

### 3. Ejecutar la aplicación con Firejail (línea de comandos)

```bash
# Ejecutar en sandbox con perfil por defecto
firejail --private=~/proyecto-nota python3 nota.py

# Explicación:
# --private=DIR  : hace que el contenedor vea Dir como su directorio home aislado
#                : cualquier cambio quedará en un FS temporal
```

**Salida esperada:** la salida normal de `nota.py` (registros de inicio y pruebas). Si Python falta dentro del contexto por la forma de aislamiento, usa `--whitelist` o instala Python dentro del sandbox.

### 4. Ejecutar con perfil más restrictivo

```bash
# Ejecutar con restricciones adicionales (sin red, sin acceso a /home, etc.)
firejail --private=~/proyecto-nota --net=none --whitelist=~/proyecto-nota python3 nota.py
```

### 5. Capturar evidencias

- Captura 1: Lista de archivos antes de ejecutar (`ls -la`)
- Captura 2: Salida del comando `firejail` y de `python3 nota.py`
- Captura 3: Resultado de `firejail --list` para ver procesos

Para capturar salidas a archivos (logs):

```bash
# Guardar salida de ejecución en archivo
firejail --private=~/proyecto-nota python3 nota.py > DOCUMENTACION/logs_aplicacion.txt 2>&1

# Guardar info de firejail
firejail --list > DOCUMENTACION/firejail_list.txt
```

### 6. Verificación de aislamiento

Dentro de la sesión (si ejecutas `firejail --shell` o `firejail --private` y luego `bash`), prueba:

```bash
# Desde dentro del sandbox
ls /home       # debería mostrar solo el home aislado
ping -c 1 8.8.8.8  # si usaste --net=none, esto fallará
ps aux | head -n 20
```




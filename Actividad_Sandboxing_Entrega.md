# Actividad Unidad 1 — Sandboxing

---

## Objetivo de la actividad

Realizar pruebas de ejecución en un entorno controlado (sandbox) con una aplicación en Python (por ejemplo, `nota.py` o la incluida en `Archivador.zip`) y documentar el proceso y evidencias. La entrega debe incluir:

- Reflexión sobre medidas de seguridad en lenguajes (apartado 1) — ya en `Reflexion_Lenguajes.md`.
- Documentación de la prueba en sandbox (apartado 2) — este documento.
- Capturas de pantalla y logs como evidencias.

---

## Resumen del enfoque que uso aquí

Voy a describir dos opciones para crear el entorno aislado:

- Opción A (recomendada por la asignatura): Firejail + Firetools (sandbox a nivel de usuario, sencillo y ligero).
- Opción B (alternativa): Docker (contenedorización) — ya documentada en otros archivos del repositorio.

A continuación se describe paso a paso la Opción A (Firejail), y al final se incluye un anexo con la Opción B (Docker) por si no puedes usar Firejail.

---

## Requisitos previos

- Sistema Linux (Ubuntu/Debian recomendado) o WSL2 con X server (para Firetools GUI).
- Permisos de sudo para instalar paquetes.
- Python 3 instalado (a nivel del host o dentro del sandbox si el sandbox permite acceder a binarios).
- El código `nota.py` (o la aplicación `notas` extraída de `Archivador.zip`) situado en la carpeta del proyecto.


---

## Parte A — Opción recomendada: Firejail

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




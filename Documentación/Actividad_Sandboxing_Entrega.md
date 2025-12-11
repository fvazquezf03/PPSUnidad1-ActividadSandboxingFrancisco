# Actividad Unidad 1 — Sandboxing (Firetools GUI)

---

## Documento donde se explica como se ejecuta lo de nota en Sanboxing (Firejail y Firetools)

---

Este documento contiene únicamente los pasos para ejecutar y documentar la aplicación `nota` usando **Firetools** (interfaz gráfica de Firejail). Incluye instalación, configuración del perfil gráfico, ejecución, y lugares donde colocar las capturas de evidencia.

## 1. Instalar Firejail y Firetools

```bash
# En Debian/Ubuntu
sudo apt update
sudo apt install -y firejail firetools

# Verificar instalación
firejail --version
```

* **Instalación de Firejail y Firetools :**


![alt text](image.png)

* **Para saber que versión tiene :**

![Cámara](image-1.png)
## 2. Preparar la aplicación

- Coloca el código de la aplicación en `~/proyecto-nota` (por ejemplo `nota.py` o los ficheros extraídos de `Archivador.zip`).

**EVIDENCIA (captura): Preparar la aplicación**

- Inserta una captura que muestre la lista de archivos y `nota.py` presente.
- Ruta sugerida: `DOCUMENTACION/capturas/captura_02_listado_proyecto.png`

`![Captura 02 - Listado proyecto](DOCUMENTACION/capturas/captura_02_listado_proyecto.png)`

## 3. Uso de Firetools (modo gráfico) — pasos

1. Abre `Firetools` desde el menú de aplicaciones o ejecutando `firetools` en una terminal.

2. En la ventana de Firetools, crea una nueva ejecución:
	- En el campo **Command** escribe: `python3 nota.py`.
	- En **Working Directory** indica: `donde esta ubicado el proyecto`.

3. Configura el perfil de aislamiento (opciones gráficas) — mapea las opciones a las banderas equivalentes de Firejail:
	- **Private mode** → `--private=~/proyecto-nota` (aisla el filesystem).
	- **Disable network** → `--net=none` (deshabilita red).
	- **Whitelist** / **Allowed directories** → añade `~/proyecto-nota` si quieres limitar el acceso solo a esa carpeta.
	- Opciones adicionales (si están disponibles): bloquear dispositivos, evitar acceso a `/home` completo, o cargar un perfil personalizado.

4. Guarda el perfil si planeas repetir la ejecución (muchas instalaciones de Firetools permiten guardar configuraciones).

5. Haz clic en **Run / Launch** para iniciar `nota.py` dentro del sandbox.

**EVIDENCIA (captura): Firetools — configuración y ejecución**

- Inserta una captura de la ventana de configuración de Firetools (perfil con las opciones marcadas).
- Ruta sugerida: `DOCUMENTACION/capturas/captura_05_config_firetools.png`

`![Captura 05 - Config Firetools](DOCUMENTACION/capturas/captura_05_config_firetools.png)`

## 4. Capturar salida y logs

- Si Firetools muestra la salida en la ventana, copia el texto o usa la opción de guardar si existe.
- Alternativa (si necesitas forzar el guardado desde fuera de la GUI): ejecuta el mismo comando con Firejail y redirección para guardar logs:

```bash
firejail --private=~/proyecto-nota python3 nota.py > DOCUMENTACION/logs_aplicacion.txt 2>&1
```

**EVIDENCIA (captura): Salida y logs**

- Inserta una captura de la salida mostrada por Firetools.
- Ruta sugerida: `DOCUMENTACION/capturas/captura_06_salida_firetools.png`

`![Captura 06 - Salida Firetools](DOCUMENTACION/capturas/captura_06_salida_firetools.png)`

- Inserta una captura que muestre que `DOCUMENTACION/logs_aplicacion.txt` fue creado y contiene registros.
- Ruta sugerida: `DOCUMENTACION/capturas/captura_07_logs_aplicacion_txt.png`

`![Captura 07 - Logs aplicación](DOCUMENTACION/capturas/captura_07_logs_aplicacion_txt.png)`

## 5. Verificación de aislamiento (desde Firetools o con comandos dentro del sandbox)

- Verifica que el sandbox está aislado:

```bash
# Ejemplos de verificación (puedes ejecutarlos dentro de una shell si Firetools ofrece una):
ls /home       # debería mostrar solo el home aislado
ping -c 1 8.8.8.8  # si usaste --net=none, esto fallará
```

**EVIDENCIA (captura): Verificación de aislamiento**

- Inserta una captura que muestre las salidas de los comandos de verificación (por ejemplo, `ls /home` y `ping` fallido) dentro del sandbox.
- Ruta sugerida: `DOCUMENTACION/capturas/captura_08_verificacion_aislamiento.png`

`![Captura 08 - Verificación aislamiento](DOCUMENTACION/capturas/captura_08_verificacion_aislamiento.png)`

[← Volver al índice](../README.md#índice)

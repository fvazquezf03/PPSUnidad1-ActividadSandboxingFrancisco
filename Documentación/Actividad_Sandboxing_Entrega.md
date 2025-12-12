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
```

* **Captura de la instalación**


![alt text](image.png)

* **Para saber que versión tiene :**
```bash
# Verificar instalación
firejail --version
```

![Cámara](image-1.png)

## 2. Primero preparar el firejail:

* Si quieres que tu aplicación acceda solo en una carpeta especifica
```bash
firejail --private=/home/ppsfran/Proyecto-notas/
```

![alt text](image-6.png)


## 3.Primero prepara el entorno para poder ejecutar las pruebas:

1. Creamos entorno virtual de Python
```bash
python3 -m venv sanbox
```

![alt text](image-8.png)


2. Activamos el entorno virtual:
```bash
source sanbox/bin/activate
```
![alt text](image-7.png)

3. Instalación de dependencias:
```bash
pip install -r requeriments.txt
pip install -e .
```
![alt text](image-9.png)

![alt text](image-5.png)

## 4. Ejecutar el programa dentro de sanbox dentro de la carpeta aislada:

* Ejecutamos el siguiente comando:
```bash
PYTHONPATH=src python3 src/notas/main.py
```

![alt text](image-10.png)







[← Volver al índice](../README.md#índice)

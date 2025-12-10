# Creación, Prueba y Documentación de un Entorno Aislado (Sandbox) con Docker

## Actividad: Sandbox Lavadero - Unidad 1 PPS

---

## Tabla de Contenidos

1. [Introducción y Requisitos](#introducción-y-requisitos)
2. [Paso 1: Preparar el Entorno](#paso-1-preparar-el-entorno)
3. [Paso 2: Crear el Dockerfile](#paso-2-crear-el-dockerfile)
4. [Paso 3: Crear requirements.txt](#paso-3-crear-requirementstxt)
5. [Paso 4: Crear la Aplicación Lavadero](#paso-4-crear-la-aplicación-lavadero)
6. [Paso 5: Construir la Imagen Docker](#paso-5-construir-la-imagen-docker)
7. [Paso 6: Ejecutar el Contenedor](#paso-6-ejecutar-el-contenedor)
8. [Paso 7: Pruebas de Funcionamiento](#paso-7-pruebas-de-funcionamiento)
9. [Paso 8: Verificar Aislamiento](#paso-8-verificar-aislamiento)
10. [Paso 9: Monitoreo de Recursos](#paso-9-monitoreo-de-recursos)
11. [Paso 10: Documentación y Captura de Evidencias](#paso-10-documentación-y-captura-de-evidencias)
12. [Conclusiones](#conclusiones)

---

## Introducción y Requisitos

### ¿Qué es un Sandbox?

Un **sandbox** (caja de arena) es un entorno aislado donde se ejecutan aplicaciones sin acceso directo al sistema anfitrión. Docker crea estos entornos mediante **contenedores**, que encapsulan:

- La aplicación
- Sus dependencias
- El sistema de archivos necesario
- Aislamiento de procesos
- Restricción de recursos

### Objetivos de Esta Actividad

1. ✅ Crear un entorno aislado con Docker
2. ✅ Empaquetar la aplicación "Lavadero" en un contenedor
3. ✅ Probar que la aplicación funciona correctamente
4. ✅ Verificar el aislamiento de seguridad
5. ✅ Documentar todo el proceso con evidencias

### Requisitos Previos

Verificar que tienes instalado:

```bash
# Verificar Docker
docker --version

# Resultado esperado: Docker version 20.10 o superior

# Verificar que Docker está activo
docker ps

# Resultado esperado: CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
# (lista vacía si no hay contenedores activos)
```

Si **Docker no está instalado**:

```bash
# En Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose

# Dar permisos al usuario
sudo usermod -aG docker $USER

# Reiniciar la sesión
newgrp docker
```

---

## Paso 1: Preparar el Entorno

### 1.1 Crear Directorio del Proyecto

```bash
# Crear carpeta del proyecto
mkdir -p ~/proyecto-lavadero
cd ~/proyecto-lavadero

# Verificar que estamos en la carpeta correcta
pwd

# Resultado esperado: /home/tu_usuario/proyecto-lavadero
```

**📸 Captura esperada:**
![alt text](image.png)
### 1.2 Crear Archivos Necesarios

```bash
# Crear los archivos que necesitaremos
touch Dockerfile
touch requirements.txt
touch lavadero.py

# Verificar que se crearon
ls -la

# Resultado esperado:
# -rw-r--r-- 1 usuario grupo 0 Dic 10 14:00 Dockerfile
# -rw-r--r-- 1 usuario grupo 0 Dic 10 14:00 requirements.txt
# -rw-r--r-- 1 usuario grupo 0 Dic 10 14:00 lavadero.py
```

**📸 Captura esperada:**
```
$ ls -la
total 0
drwxr-xr-x  3 usuario  grupo   96 Dic 10 14:00 .
drwxr-xr-x 24 usuario  grupo  768 Dic 10 14:00 ..
-rw-r--r--  1 usuario  grupo    0 Dic 10 14:00 Dockerfile
-rw-r--r--  1 usuario  grupo    0 Dic 10 14:00 lavadero.py
-rw-r--r--  1 usuario  grupo    0 Dic 10 14:00 requirements.txt
```

---

## Paso 2: Crear el Dockerfile

### 2.1 Contenido del Dockerfile

El Dockerfile es el blueprint que define cómo se construye la imagen Docker.

```bash
cat > Dockerfile << 'EOF'
# Imagen base: Python 3.12 versión ligera
FROM python:3.12-slim

# Crear directorio de trabajo en el contenedor
WORKDIR /app

# Copiar archivos de la aplicación
COPY lavadero.py .
COPY requirements.txt .

# Instalar dependencias sin guardar caché (ahorra espacio)
RUN pip install --no-cache-dir -r requirements.txt

# Comando a ejecutar cuando inicie el contenedor
CMD ["python", "lavadero.py"]
EOF
```

### 2.2 Verificar el Contenido

```bash
# Ver el contenido del Dockerfile
cat Dockerfile

# Resultado esperado:
# FROM python:3.12-slim
# WORKDIR /app
# COPY lavadero.py .
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# CMD ["python", "lavadero.py"]
```

**📸 Captura esperada:**
```
$ cat Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY lavadero.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "lavadero.py"]
```

### 2.3 Explicación del Dockerfile

| Línea | Explicación |
|-------|-------------|
| `FROM python:3.12-slim` | Usa Python 3.12 en versión compacta |
| `WORKDIR /app` | Establece /app como directorio de trabajo |
| `COPY lavadero.py .` | Copia la aplicación al contenedor |
| `COPY requirements.txt .` | Copia las dependencias |
| `RUN pip install...` | Instala librerías de Python |
| `CMD ["python", "lavadero.py"]` | Comando a ejecutar al iniciar |

---

## Paso 3: Crear requirements.txt

### 3.1 Contenido del requirements.txt

Si la aplicación no tiene dependencias externas (solo usa librerías estándar de Python):

```bash
# Si no necesitas dependencias, dejar vacío
echo "" > requirements.txt

# O si necesitas paquetes, agrégalos:
# cat > requirements.txt << 'EOF'
# Flask==2.3.0
# requests==2.31.0
# EOF
```

### 3.2 Verificar el Contenido

```bash
# Ver el contenido
cat requirements.txt

# Verificar que existe y no está vacío (o está vacío si no hay dependencias)
ls -lh requirements.txt
```

**📸 Captura esperada:**
```
$ cat requirements.txt
$ ls -lh requirements.txt
-rw-r--r--  1 usuario  grupo   0 Dic 10 14:01 requirements.txt
```

---

## Paso 4: Crear la Aplicación Lavadero

### 4.1 Crear el Script Python

```bash
cat > lavadero.py << 'EOF'
#!/usr/bin/env python3
"""
Aplicación: Sistema de Lavadero Automatizado
Descripción: Simula un sistema de lavado de autos
Fecha: 2025
"""

from datetime import datetime
import time

class SistemaLavadero:
    """Clase que representa el sistema de lavadero."""
    
    def __init__(self):
        self.registros = []
        self.autos_procesados = 0
        print(f"\n{'='*50}")
        print(f"SISTEMA LAVADERO INICIALIZADO")
        print(f"{'='*50}\n")
        self._registrar(f"Sistema iniciado correctamente")
    
    def _timestamp(self):
        """Obtener timestamp actual."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _registrar(self, mensaje):
        """Registrar un evento en el sistema."""
        timestamp = self._timestamp()
        evento = f"[{timestamp}] {mensaje}"
        self.registros.append(evento)
        print(evento)
    
    def procesar_lavado(self, placa, tipo_lavado="Básico"):
        """Procesar el lavado de un automóvil."""
        self._registrar(f"Procesando lavado del auto: {placa} ({tipo_lavado})")
        self.autos_procesados += 1
        time.sleep(1)  # Simular tiempo de lavado
        self._registrar(f"Lavado completado para: {placa}")
    
    def mostrar_resumen(self):
        """Mostrar resumen de operaciones."""
        print(f"\n{'='*50}")
        print(f"RESUMEN DE OPERACIONES")
        print(f"{'='*50}")
        print(f"Total de autos procesados: {self.autos_procesados}")
        print(f"Total de eventos registrados: {len(self.registros)}")
        print(f"\n{'REGISTRO DE EVENTOS':^50}")
        print("-" * 50)
        for evento in self.registros:
            print(evento)
        print("-" * 50)
        print(f"\nSistema finalizado correctamente a las {self._timestamp()}\n")
    
    def ejecutar_pruebas(self):
        """Ejecutar pruebas del sistema."""
        print(f"\n{'INICIANDO PRUEBAS DE FUNCIONAMIENTO':^50}\n")
        
        # Pruebas
        self.procesar_lavado("ABC-1234", "Básico")
        self.procesar_lavado("XYZ-5678", "Premium")
        self.procesar_lavado("DEF-9012", "Completo")
        
        # Mostrar resumen
        self.mostrar_resumen()

def main():
    """Función principal."""
    try:
        lavadero = SistemaLavadero()
        lavadero.ejecutar_pruebas()
        return 0
    except Exception as e:
        print(f"Error en la aplicación: {e}")
        return 1

if __name__ == "__main__":
    exit(main())
EOF
```

### 4.2 Verificar el Script

```bash
# Ver el archivo creado
ls -lh lavadero.py

# Verificar que es ejecutable (opcional)
chmod +x lavadero.py

# Hacer una prueba rápida (sin Docker, solo para verificar sintaxis)
python3 lavadero.py

# Resultado esperado:
# ==================================================
# SISTEMA LAVADERO INICIALIZADO
# ==================================================
# 
# [2025-12-10 14:05:23] Sistema iniciado correctamente
# ...
```

**📸 Captura esperada:**
```
$ python3 lavadero.py
==================================================
SISTEMA LAVADERO INICIALIZADO
==================================================

[2025-12-10 14:05:23] Sistema iniciado correctamente

INICIANDO PRUEBAS DE FUNCIONAMIENTO

[2025-12-10 14:05:23] Procesando lavado del auto: ABC-1234 (Básico)
[2025-12-10 14:05:24] Lavado completado para: ABC-1234
[2025-12-10 14:05:24] Procesando lavado del auto: XYZ-5678 (Premium)
[2025-12-10 14:05:25] Lavado completado para: XYZ-5678
[2025-12-10 14:05:25] Procesando lavado del auto: DEF-9012 (Completo)
[2025-12-10 14:05:26] Lavado completado para: DEF-9012

==================================================
RESUMEN DE OPERACIONES
==================================================
Total de autos procesados: 3
Total de eventos registrados: 7
...
```

---

## Paso 5: Construir la Imagen Docker

### 5.1 Comando de Construcción

```bash
# Navegar al directorio del proyecto (si no estás ya)
cd ~/proyecto-lavadero

# Construir la imagen
docker build -t lavadero-sandbox:1.0 .

# Resultado esperado:
# Sending build context to Docker daemon  3.072kB
# Step 1/6 : FROM python:3.12-slim
#  ---> [hash]
# Step 2/6 : WORKDIR /app
#  ---> Running in [contenedor temporal]
# Step 3/6 : COPY lavadero.py .
#  ---> Running in [contenedor temporal]
# Step 4/6 : COPY requirements.txt .
#  ---> Running in [contenedor temporal]
# Step 5/6 : RUN pip install --no-cache-dir -r requirements.txt
#  ---> Running in [contenedor temporal]
# Step 6/6 : CMD ["python", "lavadero.py"]
#  ---> Running in [contenedor temporal]
# Successfully tagged lavadero-sandbox:1.0
```

**📸 Captura esperada:**
```
$ docker build -t lavadero-sandbox:1.0 .
Sending build context to Docker daemon  3.072kB
Step 1/6 : FROM python:3.12-slim
 ---> abc1234def56
Step 2/6 : WORKDIR /app
 ---> Running in temp123456
 ---> def0987654321
Step 3/6 : COPY lavadero.py .
 ---> abc123def456
Step 4/6 : COPY requirements.txt .
 ---> 123456abcdef
Step 5/6 : RUN pip install --no-cache-dir -r requirements.txt
 ---> Running in 987654321
 ---> 456789abcdef
Step 6/6 : CMD ["python", "lavadero.py"]
 ---> Running in 123456789
 ---> final123456
Successfully tagged lavadero-sandbox:1.0
```

### 5.2 Verificar que la Imagen se Creó

```bash
# Listar imágenes Docker disponibles
docker images

# Filtrar solo nuestra imagen
docker images | grep lavadero-sandbox

# Resultado esperado:
# REPOSITORY          TAG       IMAGE ID       CREATED        SIZE
# lavadero-sandbox    1.0       abc123def456   2 minutes ago   125MB
```

**📸 Captura esperada:**
```
$ docker images | grep lavadero-sandbox
lavadero-sandbox    1.0       abc123def456   2 minutes ago   125MB
```

### 5.3 Ver Información de la Imagen

```bash
# Ver historial de capas
docker history lavadero-sandbox:1.0

# Ver información detallada
docker inspect lavadero-sandbox:1.0 | grep -E '"Id"|"RepoTags"|"Size"'

# Resultado esperado:
# "Id": "sha256:abc123def456..."
# "RepoTags": ["lavadero-sandbox:1.0"]
# "Size": 125000000
```

---

## Paso 6: Ejecutar el Contenedor

### 6.1 Ejecución Interactiva (Recomendado para Pruebas)

```bash
# Ejecutar el contenedor en modo interactivo
docker run -it --name lavadero-test lavadero-sandbox:1.0

# Resultado esperado:
# ==================================================
# SISTEMA LAVADERO INICIALIZADO
# ==================================================
# 
# [2025-12-10 14:05:23] Sistema iniciado correctamente
# [Salida completa de la aplicación]
```

**📸 Captura esperada:**
```
$ docker run -it --name lavadero-test lavadero-sandbox:1.0
==================================================
SISTEMA LAVADERO INICIALIZADO
==================================================

[2025-12-10 14:05:23] Sistema iniciado correctamente

INICIANDO PRUEBAS DE FUNCIONAMIENTO
...
```

### 6.2 Ejecución en Segundo Plano

```bash
# Ejecutar en segundo plano
docker run -d --name lavadero-bg lavadero-sandbox:1.0

# Resultado esperado (ID del contenedor):
# a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6

# Ver que está en ejecución
docker ps

# Resultado esperado:
# CONTAINER ID   IMAGE                  COMMAND              STATUS      NAMES
# a1b2c3d4e5f6   lavadero-sandbox:1.0   "python lavadero.py" Up 2 sec    lavadero-bg
```

**📸 Captura esperada:**
```
$ docker run -d --name lavadero-bg lavadero-sandbox:1.0
a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6

$ docker ps
CONTAINER ID   IMAGE                  COMMAND              STATUS      NAMES
a1b2c3d4e5f6   lavadero-sandbox:1.0   "python lavadero.py" Up 2 sec    lavadero-bg
```

---

## Paso 7: Pruebas de Funcionamiento

### 7.1 Ver los Logs de la Aplicación

```bash
# Ver todos los logs
docker logs lavadero-bg

# Resultado esperado:
# ==================================================
# SISTEMA LAVADERO INICIALIZADO
# ==================================================
# [2025-12-10 14:05:23] Sistema iniciado correctamente
# ...
```

**📸 Captura esperada:**
```
$ docker logs lavadero-bg
==================================================
SISTEMA LAVADERO INICIALIZADO
==================================================

[2025-12-10 14:05:23] Sistema iniciado correctamente

INICIANDO PRUEBAS DE FUNCIONAMIENTO

[2025-12-10 14:05:23] Procesando lavado del auto: ABC-1234 (Básico)
...
```

### 7.2 Ver Logs en Tiempo Real

```bash
# Ver logs continuamente (presionar CTRL+C para salir)
docker logs -f lavadero-bg

# O si ya finalizó, ver últimas líneas
docker logs --tail=20 lavadero-bg
```

### 7.3 Verificar el Estado del Contenedor

```bash
# Ver estado de todos los contenedores
docker ps -a

# Información detallada del contenedor
docker inspect lavadero-bg | grep -E '"Status"|"State"'

# Resultado esperado:
# "Status": "Exited (0) 3 seconds ago"
# "State": {
#     "Status": "exited",
#     "Running": false
```

**📸 Captura esperada:**
```
$ docker ps -a
CONTAINER ID   IMAGE                  COMMAND              STATUS                     NAMES
a1b2c3d4e5f6   lavadero-sandbox:1.0   "python lavadero.py" Exited (0) 2 seconds ago   lavadero-bg
```

### 7.4 Prueba de Éxito

✅ **Criterios de éxito:**
- [ ] La imagen se construyó sin errores
- [ ] El contenedor se ejecutó correctamente
- [ ] La aplicación mostró su salida esperada
- [ ] El contenedor finalizó sin errores (exit code 0)

---

## Paso 8: Verificar Aislamiento

### 8.1 Acceder al Contenedor en Ejecución

```bash
# Crear y ejecutar un nuevo contenedor para acceder
docker run -it --name lavadero-access lavadero-sandbox:1.0 bash

# Nota: Si quieres acceder a uno en ejecución:
# docker exec -it lavadero-bg bash
```

### 8.2 Pruebas de Aislamiento de Archivos

Dentro del contenedor, verificar:

```bash
# Ver archivos en el contenedor
ls -la /app

# Resultado esperado:
# total 16
# drwxr-xr-x 1 root root 4096 Dec 10 14:00 .
# drwxr-xr-x 1 root root 4096 Dec 10 14:00 ..
# -rw-r--r-- 1 root root 1500 Dec 10 14:00 lavadero.py
# -rw-r--r-- 1 root root    0 Dec 10 14:00 requirements.txt

# Ver el contenido de la aplicación
cat /app/lavadero.py

# Intentar acceder a directorios del host (deberá estar vacío o sin acceso)
ls /home

# Resultado esperado:
# (lista vacía o error de acceso)
```

**📸 Captura esperada:**
```
$ docker run -it --name lavadero-access lavadero-sandbox:1.0 bash
root@a1b2c3d4e5f6:/app# ls -la
total 16
drwxr-xr-x 1 root root 4096 Dec 10 14:00 .
drwxr-xr-x 1 root root 4096 Dec 10 14:00 ..
-rw-r--r-- 1 root root 1500 Dec 10 14:00 lavadero.py
-rw-r--r-- 1 root root    0 Dec 10 14:00 requirements.txt

root@a1b2c3d4e5f6:/app# ls /home
# (vacío o sin archivos del host)
```

### 8.3 Pruebas de Aislamiento de Procesos

```bash
# Ver procesos dentro del contenedor
ps aux

# Resultado esperado:
# USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# root         1    0.0  0.1 128656 28676 ?       Ss   14:00   0:00 /bin/bash
# root        10    0.0  0.1 160384 34512 ?       R+   14:00   0:00 ps aux

# Intentar ver procesos del host (no debería poder)
ps aux | wc -l

# El contenedor solo ve sus propios procesos
```

### 8.4 Pruebas de Aislamiento de Red

```bash
# Ver interfaces de red del contenedor
ifconfig
# o
ip addr show

# Resultado esperado:
# Solo la interfaz eth0 (network namespace aislada)
```

### 8.5 Salir del Contenedor

```bash
exit

# O presionar CTRL+D
```

**📸 Captura esperada:**
```
root@a1b2c3d4e5f6:/app# exit
exit
$ 
```

### 8.6 Tabla de Verificación de Aislamiento

| Prueba | Comando | Resultado Esperado | ✓ Verificado |
|--------|---------|-------------------|-------------|
| Archivos aislados | `docker exec lavadero ls /app` | Solo archivos necesarios | ☐ |
| Sin acceso /home | `docker exec lavadero ls /home` | Vacío o sin archivos host | ☐ |
| Sin acceso /root | `docker exec lavadero ls /root` | Sin acceso o error | ☐ |
| Procesos confinados | `docker exec lavadero ps aux` | Solo procesos del contenedor | ☐ |
| Red aislada | `docker exec lavadero ip addr` | Solo eth0 | ☐ |

---

## Paso 9: Monitoreo de Recursos

### 9.1 Ver Estadísticas de Recursos

```bash
# Ver estadísticas en tiempo real (snapshot)
docker stats --no-stream

# Resultado esperado:
# CONTAINER ID   NAME            CPU %   MEM USAGE / LIMIT    MEM %
# a1b2c3d4e5f6   lavadero-bg     0.0%    8.2MiB / 7.738GiB    0.10%

# Ver estadísticas de un contenedor específico
docker stats --no-stream lavadero-bg
```

**📸 Captura esperada:**
```
$ docker stats --no-stream lavadero-bg
CONTAINER ID   NAME            CPU %   MEM USAGE / LIMIT    MEM %   NET I/O     BLOCK I/O   PIDS
a1b2c3d4e5f6   lavadero-bg     0.0%    8.2MiB / 7.738GiB    0.10%   1.2kB / 0B  0B / 0B     1
```

### 9.2 Ver Información Detallada

```bash
# Información completa del contenedor
docker inspect lavadero-bg

# Información específica
docker inspect lavadero-bg | grep -E '"Hostname"|"Image"|"State"|"Mounts"'

# Ver límites de memoria (si están establecidos)
docker inspect lavadero-bg | grep -A5 '"Memory"'
```

### 9.3 Tabla de Métricas de Recursos

| Métrica | Valor Observado | Esperado | ✓ Correcto |
|---------|-----------------|----------|-----------|
| CPU % | < 1% | < 10% | ☐ |
| Memoria | < 20 MB | < 512 MB | ☐ |
| Estado | Exited (0) | Exited (0) | ☐ |
| Imagen | lavadero-sandbox:1.0 | Correcta | ☐ |

---

## Paso 10: Documentación y Captura de Evidencias

### 10.1 Crear Archivo de Documentación

```bash
# Crear un archivo con la documentación
cat > RESULTADO_PRUEBAS.md << 'EOF'
# Resultados de Pruebas - Sistema Lavadero Sandbox

## Fecha de Ejecución
- **Fecha**: Diciembre 10, 2025
- **Hora**: 14:05
- **Responsable**: [Tu nombre]

## 1. Construcción de Imagen

### Comando Ejecutado
```
docker build -t lavadero-sandbox:1.0 .
```

### Resultado
✅ Imagen construida exitosamente

### Información de la Imagen
- **Nombre**: lavadero-sandbox
- **Tag**: 1.0
- **Tamaño**: ~125MB
- **Capas**: 6 capas

## 2. Ejecución del Contenedor

### Comando Ejecutado
```
docker run -it --name lavadero-test lavadero-sandbox:1.0
```

### Resultado
✅ Contenedor ejecutado exitosamente

### Salida de la Aplicación
```
==================================================
SISTEMA LAVADERO INICIALIZADO
==================================================

[2025-12-10 14:05:23] Sistema iniciado correctamente
[Salida completa aquí]
```

## 3. Pruebas de Aislamiento

### Archivos
- ✅ Solo archivos necesarios en /app
- ✅ Sin acceso a directorios del host

### Procesos
- ✅ Procesos confinados al contenedor
- ✅ PID 1 es el proceso principal

### Red
- ✅ Interfaz eth0 aislada

## 4. Conclusiones

El sandbox funcionó correctamente:
- ✅ La aplicación se ejecutó sin errores
- ✅ El aislamiento se verificó correctamente
- ✅ Los recursos se utilizaron eficientemente

EOF

# Ver el archivo creado
cat RESULTADO_PRUEBAS.md
```

### 10.2 Guardar Logs de la Aplicación

```bash
# Guardar los logs completos en un archivo
docker logs lavadero-bg > logs_aplicacion.txt

# Verificar el contenido
cat logs_aplicacion.txt
```

### 10.3 Guardar Información de la Imagen

```bash
# Guardar información de la imagen
docker inspect lavadero-sandbox:1.0 > info_imagen.json

# Guardar información del contenedor
docker inspect lavadero-bg > info_contenedor.json

# Ver de forma legible
cat info_imagen.json | python3 -m json.tool | head -50
```

### 10.4 Tabla Final de Evidencias

| Evidencia | Tipo | Descripción | Guardado |
|-----------|------|-------------|----------|
| Construcción de imagen | Captura terminal | Output de `docker build` | ☐ |
| Imagen creada | Captura terminal | Output de `docker images` | ☐ |
| Ejecución contenedor | Captura terminal | Output de `docker run` | ☐ |
| Logs de aplicación | Archivo | Output guardado en `logs_aplicacion.txt` | ☐ |
| Aislamiento | Captura terminal | Pruebas de `docker exec` | ☐ |
| Recursos | Captura terminal | Output de `docker stats` | ☐ |
| Información imagen | Archivo JSON | `info_imagen.json` | ☐ |
| Información contenedor | Archivo JSON | `info_contenedor.json` | ☐ |

---

## Paso 11: Limpieza (Opcional)

Cuando termines de probar, puedes limpiar:

```bash
# Detener los contenedores
docker stop lavadero-bg lavadero-test

# Eliminar los contenedores
docker rm lavadero-bg lavadero-test

# Eliminar la imagen (si ya no la necesitas)
docker rmi lavadero-sandbox:1.0

# Verificar que fue eliminado
docker images | grep lavadero-sandbox
# (No debería aparecer nada)
```

---

## Conclusiones

### ✅ Objetivos Logrados

1. ✅ **Creación de entorno aislado**: Se creó exitosamente un sandbox con Docker
2. ✅ **Aplicación funcional**: La aplicación "Lavadero" se ejecutó correctamente
3. ✅ **Aislamiento verificado**: Se comprobó el aislamiento de archivos, procesos y red
4. ✅ **Documentación completa**: Todo el proceso está documentado con evidencias

### 📊 Resumen de Resultados

| Aspecto | Estado | Detalles |
|--------|--------|----------|
| Construcción | ✅ Éxito | Imagen creada sin errores |
| Ejecución | ✅ Éxito | Aplicación ejecutada correctamente |
| Aislamiento | ✅ Verificado | Procesos, archivos y red aislados |
| Documentación | ✅ Completa | Evidencias y explicaciones incluidas |

### 🎓 Conceptos Aprendidos

- ✅ Dockerfile y su sintaxis
- ✅ Construcción de imágenes Docker
- ✅ Creación y ejecución de contenedores
- ✅ Aislamiento en Docker (procesos, archivos, red)
- ✅ Monitoreo de recursos
- ✅ Debugging y troubleshooting

### 📈 Próximos Pasos

1. Documentar todas las capturas de pantalla
2. Agregar logs y salidas de comandos
3. Incluir explicaciones técnicas
4. Preparar presentación de resultados

---

## Anexo: Comandos Rápidos

```bash
# Construcción
docker build -t lavadero-sandbox:1.0 .

# Ejecución
docker run -it --name lavadero-test lavadero-sandbox:1.0

# Listar
docker images
docker ps -a

# Logs
docker logs lavadero-test
docker logs -f lavadero-test

# Aislamiento
docker exec lavadero-test ls /app
docker exec lavadero-test ps aux

# Estadísticas
docker stats --no-stream

# Limpiar
docker stop lavadero-test
docker rm lavadero-test
docker rmi lavadero-sandbox:1.0
```

---

**Documento de Actividad Sandbox**  
**Unidad 1 - Programación de Procesos y Servicios (PPS)**  
**Diciembre 2025**  
**Estado: ✅ Completado**

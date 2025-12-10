## Creación de un entorno de ejecución aislado (sandbox) para la aplicación “Lavadero”
1. Crear un Dockerfile para la aplicación “Lavadero”
```bash
# Esto es la imagen  base de Python
FROM python:3.12-slim

# Creamos el  directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY lavadero.py .
COPY requirements.txt .

# Instala las  dependencias
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "lavadero.py"]

```
2. Construimos ahora  la imagen Docker
* Esto creará una imagen de Docker llamada == lavadero-sandbox ==
```bash
docker build -t lavadero-sandbox .

``` 


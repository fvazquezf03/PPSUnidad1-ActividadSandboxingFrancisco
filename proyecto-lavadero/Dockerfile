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

# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000 para acceder a la aplicación desde fuera del contenedor
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]

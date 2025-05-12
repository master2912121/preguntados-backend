# Usar una imagen base de Python

FROM python:3.8-slim



# Establecer el directorio de trabajo

WORKDIR /app



# Copiar los archivos del proyecto

COPY . /app



# Instalar las dependencias

RUN pip install -r requirements.txt



# Exponer el puerto

EXPOSE 8000



# Comando para iniciar la aplicación

CMD ["python", "app.py"]

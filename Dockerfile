# Dockerfile
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y libreoffice ghostscript && \
    pip install --no-cache-dir Flask PyPDF2

WORKDIR /app
COPY . .

EXPOSE 5000
CMD ["python", "backend/app.py"]

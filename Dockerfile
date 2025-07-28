# Dockerfile (este arquivo fica na raiz do seu repositório)
FROM python:3.9-slim

# 1. Instala o git
RUN apt-get update && apt-get install -y git

# 2. Clona SEU próprio repositório (incluindo este Dockerfile)
RUN git clone https://github.com/GabrielMenetrier/RestapiForAIagents /app

# 3. Configura o ambiente
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
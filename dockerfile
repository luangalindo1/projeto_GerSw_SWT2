# Usar a imagem base do Python 3.10 slim (para usar menos espaço no contêiner)
FROM python:3.10-slim

# Instalar dependências do sistema para OpenCV, Tkinter e outras bibliotecas necessárias
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libglib2.0-dev \
    libgl1-mesa-glx \
    tk \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt e instalar as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código-fonte para o diretório de trabalho
COPY . /app/

# Definir o comando padrão para executar o aplicativo
CMD ["python", "conversor.py"]
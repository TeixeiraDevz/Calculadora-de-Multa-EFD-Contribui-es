FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY calculadora.py .

# Expõe a porta 8501
EXPOSE 8501

# Comando para executar a aplicação
CMD ["streamlit", "run", "calculadora.py", "--server.port=8501", "--server.address=0.0.0.0"]

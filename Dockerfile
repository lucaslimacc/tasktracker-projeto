# Imagem base oficial do Python, versão "slim" (leve, só o essencial)
FROM python:3.11-slim

# Pasta de trabalho dentro do container
WORKDIR /app

# Mostra as saídas do Python imediatamente no terminal, sem buffer
ENV PYTHONUNBUFFERED=1

# Copia o código-fonte da aplicação para dentro da imagem
COPY src/ /app/src/

# Comando executado quando o container inicia
CMD ["python", "src/main.py"]

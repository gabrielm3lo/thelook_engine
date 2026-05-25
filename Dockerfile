# 1. Pegamos um "mini-computador" Linux com Python 3.9
FROM python:3.9-slim

# 2. Criamos a pasta de trabalho
WORKDIR /app

# 3. Copiamos nosso código para lá
COPY . /app

# 4. Instalamos o Pytest
RUN pip install pytest

# 5. Comando para rodar os testes
CMD ["python", "-m", "pytest"]

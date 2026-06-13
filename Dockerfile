FROM python:3.11.13-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* 

RUN pip install --no-cache-dir \
    pip==25.1.1 \
    setuptools==80.9.0 \
    wheel==0.45.1 && \
    pip install --no-cache-dir -r requirements.txt
    
RUN groupadd -g 10001 appgroup && \
    useradd -u 10001 -g 10001 -m appuser

COPY . .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000

CMD ["python","app.py"]

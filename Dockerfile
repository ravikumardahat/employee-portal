FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt
RUN useradd -m appuser

COPY . .
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000

CMD ["python","app.py"]

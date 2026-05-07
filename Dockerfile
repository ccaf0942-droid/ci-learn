FROM python:3.11-slim
WORKDIR /app

# Установка уязвимой версии OpenSSL
RUN apt-get update && apt-get install -y openssl=1.1.1n-0+deb11u3

COPY reqmest.txt .
RUN pip install --no-cache-dir -r reqmest.txt
COPY chels.py .

RUN useradd -m -u 1001 appuser
USER appuser

CMD ["python", "chels.py"]
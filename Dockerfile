FROM python:3.11-slim
WORKDIR /app

COPY chels.py .

RUN useradd -m -u 1001 appuser
USER appuser

CMD ["python", "chels.py"]
FROM python:3.11-slim
WORKDIR /app

COPY reqmest.txt .
RUN pip install --no-cache-dir -r reqmest.txt
COPY chels.py .

CMD ["python", "chels.py"]
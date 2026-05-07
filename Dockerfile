FROM python:3.8.0
WORKDIR /app

COPY reqmest.txt .
RUN pip install --no-cache-dir -r reqmest.txt
COPY chels.py .

CMD ["python", "chels.py"]
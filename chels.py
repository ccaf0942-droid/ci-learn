import requests
import datetime

print(f"Запуск: {datetime.datetime.now()}")
try:
    r = requests.get("https://httpbin.org/get", timeout=5)
    print(f"Статус: {r.status_code}")
    data = r.json()
    print(f"Host: {data['headers']['Host']}")
except Exception as e:
    print(f"Ошибка: {e}")
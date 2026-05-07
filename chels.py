import requests
import datetime

print(f"Запуск: {datetime.datetime.now()}")
try:
    r = requests.get("https://api.github.com", timeout=5)
    print(f"GitHub API Status: {r.status_code}")
except Exception as e:
    print(f"Ошибка: {e}")
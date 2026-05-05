import requests

try:
    r = requests.get("https://api.github.com", timeout=5)
    print(f"Статус: {r.status_code}")
    print("Зависимость requests работает!")
    print("DOWN?")
except Exception as e:
    print(f"Ошибка: {e}")
    print("?NODOWN?")

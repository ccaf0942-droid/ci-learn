import requests

try:
    r = requests.get("https://api.github.com", timeout=5)
    print(f"GitHub API: {r.status_code}")
except Exception as e:
    print(f"Ошибка: {e}")
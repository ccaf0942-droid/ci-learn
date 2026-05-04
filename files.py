import os

files = os.listdir(".")

print(f"Файлов в папке: {len(files)}")

for f in files:
    print(f"  - {f}")
from pathlib import Path
import json


path = Path('favorite_number.json')
if path.exists():
    text = path.read_text()
    favorite_number = json.loads(text)
    print(f"Я знаю ваше любимое число! Это {favorite_number}")

else:
    favorite_n = int(input('Введите ваше любимое число: '))
    text = json.dumps(favorite_n)
    path.write_text(text)
    print(f"Я запомнил ваше любимое число! Это {favorite_n}")

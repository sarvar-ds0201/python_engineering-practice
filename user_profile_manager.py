from pathlib import Path
import json


def greet_user():
    path = Path('info.json')
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        print(f"С возвращением пользователь!")
        for key, value in info.items():
            print(f"{key}: {value}")

    else:
        info = {}
        name = input("Как вас зовут? ")
        age = int(input("Сколько тебе лет? "))
        location = input("Как называется ваш город? ")
        info['name'] = name
        info['age'] = age
        info['location'] = location

        contents = json.dumps(info)
        path.write_text(contents)
        print(f"Приветствую вас пользователь!")
        print(f"\nИмя: {info['name']} \nВозраст: {info['age']} \nЛокация: {info['location']}")


greet_user()

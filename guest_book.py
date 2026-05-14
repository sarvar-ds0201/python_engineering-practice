from pathlib import Path

path = Path('guest_book.txt')

while True:
    name = input("Введите ваше имя(введите 'q' чтобы выйти): ")
    if name == 'q':
        break
    new_name = path.read_text()
    new_name += f"{name}\n"
    path.write_text(new_name)

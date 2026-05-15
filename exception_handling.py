from pathlib import Path

path1 = Path('cats.txt')
path2 = Path('dogs.txt')
try:
    texts1 = path1.read_text()
    texts2 = path2.read_text()
except FileNotFoundError:
    print(f"Извините файл {path1} или {path2} отсутствует")
else:
    print(f"Текст файла {path1}: \n{texts1}")
    print(f"\nТекст файла {path2}: \n{texts2}")

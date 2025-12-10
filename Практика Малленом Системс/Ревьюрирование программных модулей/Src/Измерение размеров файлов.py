import os

def get_file_size(filepath):
    """Возвращает размер файла в байтах."""
    return os.path.getsize(filepath)

def format_size(bytes):
    """Преобразует байты в читаемый формат (КБ, МБ)."""
    for unit in ['Б', 'КБ', 'МБ', 'ГБ']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024
    return f"{bytes:.2f} ТБ"


# Пример использования
if __name__ == "__main__":
    files = ["main.py", "input.txt", "output.txt"]
    
    print("РАЗМЕРЫ ФАЙЛОВ")
    print("-"*40)
    for file in files:
        if os.path.exists(file):
            size = get_file_size(file)
            print(f"{file}: {format_size(size)}")
        else:
            print(f"{file}: не найден")

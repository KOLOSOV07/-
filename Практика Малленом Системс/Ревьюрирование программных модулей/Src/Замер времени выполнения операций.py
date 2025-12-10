import time
import os

def timed_operation(name, func, *args, **kwargs):
    """
    Замеряет время выполнения функции func.
    Возвращает: (результат функции, затраченное время в сек.)
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    duration = end - start
    print(f"{name}: {duration:.4f} сек")
    return result, duration

# Пример использования
if __name__ == "__main__":
    # Функции
    def load_data(filepath):
        with open(filepath, 'r') as f:
            return f.readlines()

    def process_data(data):
        return [line.upper() for line in data]

    def save_report(data, filepath):
        with open(filepath, 'w') as f:
            f.writelines(data)

    # Замеры
    data, t1 = timed_operation("Загрузка данных", load_data, "input.txt")
    processed, t2 = timed_operation("Обработка данных", process_data, data)
    timed_operation("Сохранение отчёта", save_report, processed, "output.txt")

    # Итоговая таблица (вывод в консоль)
    print("\n" + "-"*50)
    print("РЕЗУЛЬТАТЫ ЗАМЕРОВ")
    print("-"*50)
    print(f"Загрузка данных:    {t1:.4f} сек")
    print(f"Обработка данных:    {t2:.4f} сек")
    print(f"Сохранение отчёта:  {_:.4f} сек")  # _ — последнее возвращённое время

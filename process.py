"""
Консольное приложение для работы с процессами
Операционные системы и среды - Занятие 7-8
Демонстрация использования многопроцессности (multiprocessing)
"""

import os
import time
from multiprocessing import Process, current_process
from datetime import datetime


def format_timestamp():
    """Получить отформатированное время"""
    return datetime.now().strftime("%H:%M:%S")


def print_info(message: str):
    """
    Вывести информационное сообщение с временной меткой
    
    Args:
        message: Текст сообщения
    """
    timestamp = format_timestamp()
    pid = os.getpid()
    print(f"[{timestamp}] PID {pid}: {message}")


def task_one():
    """
    Первая задача: обработка данных
    Выполняет операции в отдельном процессе
    """
    process_id = os.getpid()
    print_info(f"🟢 ПРОЦЕСС 1 ЗАПУЩЕН | ID процесса: {process_id}")
    
    for i in range(1, 4):
        print_info(f"   Задача 1: Шаг {i}/3 - обработка данных...")
        time.sleep(2)  # Имитация работы
    
    print_info(f"✅ ПРОЦЕСС 1 ЗАВЕРШЕН | ID процесса: {process_id}")


def task_two():
    """
    Вторая задача: вычисления
    Выполняет математические операции в отдельном процессе
    """
    process_id = os.getpid()
    print_info(f"🟡 ПРОЦЕСС 2 ЗАПУЩЕН | ID процесса: {process_id}")
    
    result = 0
    for i in range(1, 6):
        result += i * i
        print_info(f"   Задача 2: Вычисление {i} - результат: {result}")
        time.sleep(1.5)  # Имитация работы
    
    print_info(f"✅ ПРОЦЕСС 2 ЗАВЕРШЕН | ID процесса: {process_id} | Итого: {result}")


def task_three():
    """
    Третья задача: файловые операции
    Имитирует работу с файлами в отдельном процессе
    """
    process_id = os.getpid()
    print_info(f"🔵 ПРОЦЕСС 3 ЗАПУЩЕН | ID процесса: {process_id}")
    
    files = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    
    for file in files:
        print_info(f"   Задача 3: Обработка файла '{file}'...")
        time.sleep(1)  # Имитация работы
    
    print_info(f"✅ ПРОЦЕСС 3 ЗАВЕРШЕН | ID процесса: {process_id} | Обработано файлов: {len(files)}")


def task_four():
    """
    Четвертая задача: передача данных
    Имитирует обмен данными в отдельном процессе
    """
    process_id = os.getpid()
    print_info(f"🟣 ПРОЦЕСС 4 ЗАПУЩЕН | ID процесса: {process_id}")
    
    packets = ["Пакет 1", "Пакет 2", "Пакет 3", "Пакет 4", "Пакет 5"]
    
    for packet in packets:
        print_info(f"   Задача 4: Передача '{packet}'...")
        time.sleep(0.8)  # Имитация работы
    
    print_info(f"✅ ПРОЦЕСС 4 ЗАВЕРШЕН | ID процесса: {process_id} | Передано пакетов: {len(packets)}")


def main():
    """
    Главная функция - запуск всех процессов
    """
    print("\n" + "="*70)
    print("🔷 КОНСОЛЬНОЕ ПРИЛОЖЕНИЕ: РАБОТА С ПРОЦЕССАМИ")
    print("="*70)
    print(f"Главный процесс ID: {os.getpid()}")
    print(f"Время начала: {format_timestamp()}")
    print("="*70 + "\n")
    
    # Создание объектов Process с привязкой к функциям
    print("📋 Создание процессов...\n")
    
    process_1 = Process(target=task_one, name="Process-1")
    process_2 = Process(target=task_two, name="Process-2")
    process_3 = Process(target=task_three, name="Process-3")
    process_4 = Process(target=task_four, name="Process-4")
    
    print(f"✓ Создан {process_1.name}")
    print(f"✓ Создан {process_2.name}")
    print(f"✓ Создан {process_3.name}")
    print(f"✓ Создан {process_4.name}\n")
    
    print("─"*70)
    print("🚀 ЗАПУСК ВСЕХ ПРОЦЕССОВ\n")
    print("─"*70 + "\n")
    
    # Запуск всех процессов
    start_time = time.time()
    
    process_1.start()
    process_2.start()
    process_3.start()
    process_4.start()
    
    print_info("Все процессы запущены параллельно!")
    print("\n" + "─"*70)
    print("⏳ ОЖИДАНИЕ ЗАВЕРШЕНИЯ ВСЕХ ПРОЦЕССОВ\n")
    print("─"*70 + "\n")
    
    # Ожидание завершения всех процессов
    process_1.join()
    process_2.join()
    process_3.join()
    process_4.join()
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    print("\n" + "="*70)
    print("📊 СВОДКА РЕЗУЛЬТАТОВ ВЫПОЛНЕНИЯ")
    print("="*70)
    print(f"Главный процесс ID: {os.getpid()}")
    print(f"Время завершения: {format_timestamp()}")
    print(f"Общее время выполнения: {execution_time:.2f} секунд")
    print("\n📈 Статус процессов:")
    print(f"  • {process_1.name}: {process_1.exitcode} (завершен)")
    print(f"  • {process_2.name}: {process_2.exitcode} (завершен)")
    print(f"  • {process_3.name}: {process_3.exitcode} (завершен)")
    print(f"  • {process_4.name}: {process_4.exitcode} (завершен)")
    print("\n✅ Все процессы успешно завершены!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()






"""
Расширенная версия: Работа с процессами и потоками
Демонстрирует различия между multiprocessing и threading
"""

import os
import time
from multiprocessing import Process, Queue, Pool
from threading import Thread, Lock
from datetime import datetime


# Глобальная блокировка для безопасного вывода
output_lock = Lock()


def safe_print(message: str):
    """Безопасный вывод из разных потоков"""
    with output_lock:
        timestamp = datetime.now().strftime("%H:%M:%S")
        pid = os.getpid()
        print(f"[{timestamp}] PID {pid}: {message}")


def worker_with_queue(queue: Queue, worker_id: int):
    """
    Рабочая функция, которая получает данные из очереди
    
    Args:
        queue: Очередь для получения данных
        worker_id: Идентификатор рабочего процесса
    """
    pid = os.getpid()
    safe_print(f"🔵 Рабочий {worker_id} запущен (PID: {pid})")
    
    try:
        while True:
            # Получить данные из очереди с таймаутом
            data = queue.get(timeout=2)
            
            if data is None:  # Сигнал завершения
                break
            
            safe_print(f"   Рабочий {worker_id}: обрабатываю {data}")
            time.sleep(1)
    
    except:
        pass
    
    safe_print(f"✅ Рабочий {worker_id} завершен")


def cpu_bound_task(n: int) -> int:
    """
    Задача, интенсивная по CPU
    
    Args:
        n: Диапазон для вычисления суммы
    
    Returns:
        Сумма квадратов
    """
    pid = os.getpid()
    safe_print(f"   Вычисление суммы для {n} (PID: {pid})")
    
    result = sum(i**2 for i in range(1, n + 1))
    time.sleep(1)  # Имитация долгой операции
    
    return result


def demonstrate_multiprocessing():
    """Демонстрация многопроцессности с очередями"""
    print("\n" + "="*70)
    print("📌 ДЕМОНСТРАЦИЯ: МНОГОПРОЦЕССНОСТЬ С ОЧЕРЕДЯМИ")
    print("="*70 + "\n")
    
    # Создание очереди
    queue = Queue()
    
    # Добавление данных в очередь
    data = ["Данные-1", "Данные-2", "Данные-3", "Данные-4"]
    for item in data:
        queue.put(item)
    
    # Добавление сигналов завершения
    for _ in range(2):
        queue.put(None)
    
    # Создание и запуск рабочих процессов
    processes = [
        Process(target=worker_with_queue, args=(queue, 1)),
        Process(target=worker_with_queue, args=(queue, 2))
    ]
    
    print(f"Главный процесс: {os.getpid()}\n")
    
    for p in processes:
        p.start()
    
    # Ожидание завершения
    for p in processes:
        p.join()
    
    print("\n✅ Все рабочие завершили работу\n")


def demonstrate_pool():
    """Демонстрация пула процессов"""
    print("\n" + "="*70)
    print("📌 ДЕМОНСТРАЦИЯ: ПУЛ ПРОЦЕССОВ (PROCESS POOL)")
    print("="*70 + "\n")
    
    # Данные для обработки
    numbers = [100000, 200000, 300000, 400000, 500000]
    
    print(f"Главный процесс: {os.getpid()}")
    print(f"Обработка {len(numbers)} задач...\n")
    
    # Создание пула из 3 процессов
    with Pool(processes=3) as pool:
        results = pool.map(cpu_bound_task, numbers)
    
    print("\n📊 Результаты:")
    for num, result in zip(numbers, results):
        print(f"   Сумма для {num}: {result}")
    
    print("\n✅ Все задачи обработаны\n")


def demonstrate_threading():
    """Демонстрация потоков (threading)"""
    print("\n" + "="*70)
    print("📌 ДЕМОНСТРАЦИЯ: ПОТОКИ (THREADING)")
    print("="*70 + "\n")
    
    def thread_task(thread_id: int):
        """Задача для потока"""
        safe_print(f"🟢 Поток {thread_id} запущен")
        
        for i in range(3):
            safe_print(f"   Поток {thread_id}: итерация {i+1}")
            time.sleep(1)
        
        safe_print(f"✅ Поток {thread_id} завершен")
    
    print(f"Главный процесс: {os.getpid()}\n")
    
    # Создание и запуск потоков
    threads = [
        Thread(target=thread_task, args=(1,), name="Thread-1"),
        Thread(target=thread_task, args=(2,), name="Thread-2"),
        Thread(target=thread_task, args=(3,), name="Thread-3")
    ]
    
    for t in threads:
        t.start()
    
    # Ожидание завершения потоков
    for t in threads:
        t.join()
    
    print("\n✅ Все потоки завершены\n")


def main():
    """Главная функция"""
    print("\n" + "="*70)
    print("🔷 РАСШИРЕННАЯ ДЕМОНСТРАЦИЯ: ПРОЦЕССЫ И ПОТОКИ")
    print("="*70)
    
    # Демонстрация различных подходов
    demonstrate_multiprocessing()
    demonstrate_pool()
    demonstrate_threading()
    
    print("="*70)
    print("✅ ВСЕ ДЕМОНСТРАЦИИ ЗАВЕРШЕНЫ")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()


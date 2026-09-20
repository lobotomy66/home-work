import os
import sys
import platform

# ============================================================================
# ЭТАП 1: Создание переменных с информацией об ОС
# ============================================================================

# Информация об ОС
os_name = os.name
platform_system = platform.system()
platform_release = platform.release()
platform_version = platform.version()
processor = platform.processor()
machine = platform.machine()

# Информация о Python
python_version = platform.python_version()
python_implementation = platform.python_implementation()

# Информация о пользователе и путях
username = os.getenv('USERNAME') or os.getenv('USER')
home_directory = os.path.expanduser('~')
current_directory = os.getcwd()

# ============================================================================
# ЭТАП 2: Сохранение результатов в список
# ============================================================================

system_info_list = [
    os_name,
    platform_system,
    platform_release,
    platform_version,
    processor,
    machine,
    python_version,
    python_implementation,
    username,
    home_directory,
    current_directory
]

# Описания для каждого индекса
descriptions = [
    "Тип ОС (os.name):",
    "Платформа (platform.system()):",
    "Версия платформы (platform.release()):",
    "Полная версия (platform.version()):",
    "Процессор (platform.processor()):",
    "Архитектура (platform.machine()):",
    "Версия Python (platform.python_version()):",
    "Реализация Python (platform.python_implementation()):",
    "Имя пользователя (os.getenv()):",
    "Домашняя директория (os.path.expanduser()):",
    "Текущая директория (os.getcwd()):"
]

# ============================================================================
# ЭТАП 3: Функция для отображения информации
# ============================================================================

def display_full_info():
    """Вывод всей информации об ОС"""
    sys.stdout.write("\n" + "="*60 + "\n")
    sys.stdout.write("ПОЛНАЯ ИНФОРМАЦИЯ О СИСТЕМЕ\n")
    sys.stdout.write("="*60 + "\n\n")
    
    for i, description in enumerate(descriptions):
        sys.stdout.write(f"{i + 1}. {description}\n")
        sys.stdout.write(f"   └─ {system_info_list[i]}\n\n")
    
    sys.stdout.write("="*60 + "\n\n")

def display_by_index():
    """Вывод информации по индексу"""
    sys.stdout.write("\nДоступные индексы:\n")
    for i, description in enumerate(descriptions):
        sys.stdout.write(f"  [{i}] - {description}\n")
    
    sys.stdout.write("\nВведите номер индекса (0-10): ")
    sys.stdout.flush()
    
    try:
        index = int(sys.stdin.readline().strip())
        
        if 0 <= index < len(system_info_list):
            sys.stdout.write("\n" + "-"*60 + "\n")
            sys.stdout.write(f"{descriptions[index]}\n")
            sys.stdout.write(f"→ {system_info_list[index]}\n")
            sys.stdout.write("-"*60 + "\n\n")
        else:
            sys.stdout.write("\n⚠ Ошибка: Некорректный индекс!\n\n")
    except ValueError:
        sys.stdout.write("\n⚠ Ошибка: Введите число!\n\n")

def display_menu():
    """Вывод главного меню"""
    sys.stdout.write("\n" + "="*60 + "\n")
    sys.stdout.write("ДИАГНОСТИКА СИСТЕМЫ - ГЛАВНОЕ МЕНЮ\n")
    sys.stdout.write("="*60 + "\n")
    sys.stdout.write("1 - Показать всю информацию об ОС\n")
    sys.stdout.write("2 - Показать информацию по индексу\n")
    sys.stdout.write("3 - Выход\n")
    sys.stdout.write("="*60 + "\n")
    sys.stdout.write("Выберите пункт меню (1-3): ")
    sys.stdout.flush()

# ============================================================================
# ЭТАП 4: Основной цикл программы
# ============================================================================

def main():
    """Главная функция программы"""
    sys.stdout.write("\n✓ Приложение диагностики системы запущено!\n")
    
    while True:
        display_menu()
        
        try:
            choice = sys.stdin.readline().strip()
            
            if choice == '1':
                display_full_info()
            
            elif choice == '2':
                display_by_index()
            
            elif choice == '3':
                sys.stdout.write("\nСпасибо за использование приложения!\n")
                sys.stdout.write("До свидания!\n\n")
                sys.exit(0)
            
            else:
                sys.stdout.write("\n⚠ Ошибка: Выберите 1, 2 или 3!\n\n")
        
        except KeyboardInterrupt:
            sys.stdout.write("\n\nПрограмма прервана пользователем.\n")
            sys.exit(0)
        
        except Exception as e:
            sys.stdout.write(f"\n⚠ Ошибка: {str(e)}\n\n")

# ============================================================================
# ТОЧКА ВХОДА
# ============================================================================

if __name__ == "__main__":
    main()

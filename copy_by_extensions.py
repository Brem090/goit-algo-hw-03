import os
import shutil
import sys
from pathlib import Path

def copy_files_to_extension_based_dirs(source_dir, dest_dir):

    try:
        # Перевірка на існування директорії
        if not os.path.exists(source_dir):
            print(f"Вихідна директорія {source_dir} не існує.")
            return

        # Створення директорії призначення, якщо вона не існує
        os.makedirs(dest_dir, exist_ok=True)

        # Рекурсивне проходження через вихідну директорію
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)

                # Отримання розширення файлу та створення відповідної піддиректорії у директорії призначення
                file_extension = Path(file).suffix[1:]  # Видалення крпаки з розширення
                extension_dir = os.path.join(dest_dir, file_extension)
                os.makedirs(extension_dir, exist_ok=True)

                # Копіювання файлу у нову директорію
                shutil.copy(file_path, extension_dir)
                print(f"Скопійовано {file_path} до {extension_dir}")

    except Exception as e:
        print(f"Сталася помилка: {e}")


def main():
    # Парсинг аргументів командного рядка
    if len(sys.argv) < 2:
        print("Використання: python script.py <source_directory> [destination_directory]")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"

    # Виклик функції для копіювання файлів
    copy_files_to_extension_based_dirs(source_directory, destination_directory)


if __name__ == "__main__":
    main()
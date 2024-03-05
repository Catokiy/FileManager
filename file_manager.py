import os
import shutil
from config import *
from pathlib import Path


class FileManager:
    def __init__(self):
        self.workspace = WORKSPACE if os.path.exists(WORKSPACE) else DEFAULT_WORKSPACE
        self.root = Path(self.workspace)
        os.chdir(self.workspace)  # Установка рабочей папки
        self.level = 0

    def create_folder(self, folder_name):
        try:
            os.mkdir(folder_name)
            print(f"Папка '{folder_name}' успешно создана.")
        except FileExistsError:
            print(f"Папка '{folder_name}' уже существует.")

    def delete_folder(self, folder_name):
        try:
            os.rmdir(folder_name)
            print(f"Папка '{folder_name}' успешно удалена.")
        except FileNotFoundError:
            print(f"Папка '{folder_name}' не найдена.")
        except OSError:
            print(f"Папка '{folder_name}' не пуста или не может быть удалена.")

    def move_to_folder(self, folder_name):
        try:
            os.chdir(folder_name)
            self.level += 1
            print(f"Перешли в папку '{folder_name}'.")
        except FileNotFoundError:
            print(f"Папка '{folder_name}' не найдена.")

    def move_up(self):
        if self.level > 0:
            os.chdir("..")
            self.level -= 1
            print("Перешли на уровень вверх.")
        else:
            print("Выход из корневой папки невозможен.")

    def create_file(self, file_name):
        try:
            with open(file_name, 'w') as file:
                print(f"Файл '{file_name}' успешно создан.")
        except FileExistsError:
            print(f"Файл '{file_name}' уже существует.")

    def write_to_file(self, file_name, content):
        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Текст успешно записан в файл '{file_name}'.")

    def read_file(self, file_name):
        try:
            with open(file_name, 'r') as file:
                print(f"Содержимое файла '{file_name}':")
                print(file.read())
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")

    def delete_file(self, file_name):
        try:
            os.remove(file_name)
            print(f"Файл '{file_name}' успешно удален.")
        except FileNotFoundError:
            print(f"Файл '{file_name}' не найден.")

    def copy_file(self, source, destination):
        try:
            if self.check_child(destination):
                shutil.copy(source, destination)
                print(f"Файл '{source}' успешно скопирован в '{destination}'.")
            else:
                print("Папка назначения выходит за рабочую область")
        except FileNotFoundError:
            print(f"Файл '{source}' не найден.")

    def move_file(self, source, destination):
        try:
            if self.check_child(destination):
                shutil.move(source, destination)
                print(f"Файл '{source}' успешно перемещен в '{destination}'.")
            else:
                print("Папка назначения выходит за рабочую область")
        except FileNotFoundError:
            print(f"Файл '{source}' не найден.")

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Файл '{old_name}' успешно переименован в '{new_name}'.")
        except FileNotFoundError:
            print(f"Файл '{old_name}' не найден.")

    def check_child(self, destination):
        if os.path.abspath(destination) in self.root:
            return True
        else:
            return False

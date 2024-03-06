from file_manager import FileManager


def main():
    file_manager = FileManager()

    while True:
        command = input("Введите команду (для справки введите 'help'): ").strip().split()

        if not command:
            continue

        if command[0] == "exit":
            print("Выход из программы.")
            break

        if command[0] == "help":
            print("Доступные команды:")
            print("- show_workspace вывести рабочую папку")
            print("- create_folder <folder_name>: создать папку")
            print("- delete_folder <folder_name>: удалить папку")
            print("- move_to_folder <folder_name>: переместиться в папку")
            print("- move_up: перейти на уровень вверх")
            print("- create_file <file_name>: создать файл")
            print("- write_to_file <file_name> <content>: записать текст в файл")
            print("- read_file <file_name>: прочитать содержимое файла")
            print("- delete_file <file_name>: удалить файл")
            print("- copy_file <source> <destination>: скопировать файл")
            print("- move_file <source> <destination>: переместить файл")
            print("- rename_file <old_name> <new_name>: переименовать файл")
            print("- help: вывести эту справку")
            print("- exit: выйти из программы")
            continue

        command_name = command[0]
        command_args = command[1:]

        if command_name == "create_folder":
            file_manager.create_folder(*command_args)
        elif command_name == "delete_folder":
            file_manager.delete_folder(*command_args)
        elif command_name == "move_to_folder":
            file_manager.move_to_folder(*command_args)
        elif command_name == "move_up":
            file_manager.move_up()
        elif command_name == "create_file":
            file_manager.create_file(*command_args)
        elif command_name == "write_to_file":
            file_manager.write_to_file(command_args[0], " ".join(command_args[1:]))
        elif command_name == "read_file":
            file_manager.read_file(*command_args)
        elif command_name == "delete_file":
            file_manager.delete_file(*command_args)
        elif command_name == "copy_file":
            file_manager.copy_file(*command_args)
        elif command_name == "move_file":
            file_manager.move_file(*command_args)
        elif command_name == "rename_file":
            file_manager.rename_file(*command_args)
        elif command_name == "show_workspace":
            file_manager.show_workspace()
        else:
            print("Неизвестная команда. Для справки введите 'help'.")

main()

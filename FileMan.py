import os
import shutil

with open('settings.txt', 'r') as f:
        working_dir = f.readline() # Указать путь к рабочей папке

print(working_dir)
def list_files():
    files = os.listdir(working_dir)
    for file in files:
        print(file)

def create_folder():
    global folder_name
    folder_name = input("Введите название папки: ")
    os.mkdir(os.path.join(working_dir, folder_name))

def delete_folder():
    delete_folder_name = input("Введите имя удаляемой папки: ")
    os.rmdir(os.path.join(working_dir, folder_name))

def change_folder():
    global working_dir
    new_dir = input("Введите новую директорию с двумя //: ")
    if os.path.isdir(new_dir):
        working_dir = new_dir
        print(f"Текущая директория: {working_dir}")
    else:
        print("Такой директории не существует")

def create_file():
    global file_name
    file_name = input("Введите имя файла: ")
    with open(os.path.join(working_dir, file_name), 'w'):
        pass

def write_text_to_file():
    text = input("Введите текст: ")
    with open(os.path.join(working_dir, file_name), 'w') as file:
        file.write(text)

def view_file_contents():
    text_file = input("Введите текст, какого файла вы хотите увидеть: ")
    with open(os.path.join(working_dir, text_file), 'r') as file:
        print(file.read())

def delete_file():
    delete_file_name = input("Введите имя удаляемого файла: ")
    os.remove(os.path.join(working_dir, file_name))

def copy_file():
    source_file = input("Введите название файла: ")
    target_folder = input("Введите название папки: ")
    shutil.copyfile(os.path.join(working_dir, source_file), os.path.join(working_dir, target_folder, source_file))

def move_file():
    source_file = input("Введите название файла: ")
    target_folder = input("Введите название папки: ")
    os.replace(os.path.join(working_dir, source_file), os.path.join(working_dir, target_folder, source_file))

def rename_file():
    old_name = input("Введите старое название файла: ")
    new_name = input("Введите новое название файла: ")
    os.rename(os.path.join(working_dir, old_name), os.path.join(working_dir, new_name))

# Пример использования функций:

print(
    "1 - создать папку \n"
    "2 - удалить папку \n"
    "3 - поменять путь \n"
    "4 - создать файл \n"
    "5 - написать что-то в файле \n"
    "6 - увидеть содержание файла \n"
    "7 - удалить файл \n"
    "8 - скопировать файл \n"
    "9 - переместить файл \n"
    "10 - переименовать файл \n"
    "11 - список файлов \n"
    "0 - закончить")
while True:
    try:
        a = int(input("Введите число: "))
        if a == 1:
            create_folder()
        elif a == 2:
            delete_folder()
        elif a == 3:
            change_folder()
        elif a == 4:
            create_file()
        elif a == 5:
            write_text_to_file()
        elif a == 6:
            view_file_contents()
        elif a == 7:
            delete_file()
        elif a == 8:
            copy_file()
        elif a == 9:
            move_file()
        elif a == 10:
            rename_file()
        elif a == 11:
            list_files()
        else:
            break
    except FileExistsError as err:
        print("Файл не существует", err)
        pass
    except NameError as orr:
        print("Файл не существует: ", orr)
        pass
    except FileNotFoundError as arr:
        print("Папки не существует", arr)
        pass
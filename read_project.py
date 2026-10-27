import json
import pathlib

from project_validation import get_missing_fields, get_invalid_fields


def load_project(path):

    with open (path, "r", encoding = "utf-8") as file:
        project = json.load(file)

    return project

def save_project(project, path):

    with open (path, "w", encoding = "utf-8") as file:
        json.dump(project, file, ensure_ascii=False, indent=4 )

def create_project(title, idea):
    draft = {}
    draft["title"] = title
    draft["idea"] = idea
    draft["status"] = "draft"
            
    return draft

def read_nonempty(prompt):
    answer = input(prompt)
    strip_prompt = answer.strip()

    while strip_prompt == "":
        print("Поле не может быть пустым")
        answer = input(prompt)
        strip_prompt = answer.strip()
    return strip_prompt

def main():

    folder = pathlib.Path("C:/Users/ketab/Desktop/python/projects")
    folder.mkdir(exist_ok = True)
    print("Папка готова, продолжаем работу")

    number = input("Введите номер проекта: ")

    if number.isdecimal():
        project_folder = folder/ f"project_{number}"
        project_folder.mkdir(exist_ok = True) 

        project_path = project_folder / "project.json"

        folder_names = ["script", "images", "audio", "output"]

        for name in folder_names:
            subfolder_path =  project_folder / name
            subfolder_path.mkdir(exist_ok=True)
            print(f"Папка готова: {name}")
    else:
        print("Ошибка! Поле должно содержать цифры")
        return

    try:
        my_project = load_project(project_path)
       
    except FileNotFoundError:
        title = read_nonempty("Название проекта: ")
        idea = read_nonempty("Идея ролика: ")
        project = create_project(title, idea)
    
        save_project(project, project_path)
        print(project)

    except json.JSONDecodeError:
            print(f"Не удалось прочитать JSON в файле {project_path}. Проверьте его содержимое.")
    else:
        if isinstance(my_project, dict):
            missing = get_missing_fields(my_project)
            if missing:
                print(f"Ошибка! В проекте не хватает обязательных полей: {missing}")
            elif get_invalid_fields(my_project):
                print(f"Поле должно содержать строку и не должно быть пустым.")
            else:
        
                idea = read_nonempty("Идея ролика: ")
                my_project ["idea"] = idea
        
                save_project(my_project, project_path)
                print(my_project)
        else:
            print("Конфигурация должна содеражать словарь")


if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        print(f"Не удалось выполнить операцию с файлами: {error}")



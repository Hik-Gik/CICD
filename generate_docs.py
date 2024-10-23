import os
import inspect
import project  # Импортируем модуль с функциями

def generate_doc():
    doc_dir = 'docs'
    
    # Создаем директорию для документации, если она еще не создана
    if not os.path.exists(doc_dir):
        os.makedirs(doc_dir)
    
    # Открываем файл для записи документации
    with open(os.path.join(doc_dir, 'API.md'), 'w') as f:
        f.write("# API Documentation\n\n")
        
        # Получаем все функции из модуля project
        for name, func in inspect.getmembers(project, inspect.isfunction):
            doc = inspect.getdoc(func)  # Извлекаем docstring
            f.write(f"## {name}\n\n")
            f.write(f"{doc}\n\n")

if __name__ == "__main__":
    generate_doc()

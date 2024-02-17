import os
import ast
from skill_builder_exams.sql import insert_exam

def find_dicts_in_file(filepath):
    """
    Parses a Python file and extracts all top-level dictionary definitions.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        node = ast.parse(file.read(), filename=filepath)
    
    dicts = []
    for elem in node.body:
        if isinstance(elem, ast.Assign):
            for target in elem.targets:
                if isinstance(target, ast.Name) and isinstance(elem.value, ast.Dict):
                    dict_content = {ast.literal_eval(key): ast.literal_eval(value) for key, value in zip(elem.value.keys, elem.value.values)}
                    dicts.append({target.id: dict_content})
    return dicts

def process_and_insert_exams_from_directory():
    """
    Iterates over all Python files in the specified directory, extracts dictionary definitions,
    and inserts them into the database using the 'insert_exam' function.
    """
    directory_path = '/content/skill_builder_exams/exams'
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                file_tag = file[:-3]  # Remove '.py' extension to get the tag
                file_dicts = find_dicts_in_file(filepath)
                for dict_item in file_dicts:
                    for exam_name, exam_data in dict_item.items():
                        insert_exam(exam_name, file_tag, exam_data, db_path="/content/refs/skill_builder_exams/exams.db")

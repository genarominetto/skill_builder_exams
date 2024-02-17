import sqlite3
from skill_builder_exams.exam import Exam

def create_table(table_name, table_structure, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE TABLE {table_name} ({table_structure})")
        connection.commit()
    finally:
        connection.close()

def execute_query(query, db_path, *args):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query, *args)
    connection.commit()
    connection.close()

def fetch_query(query, db_path, *args):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(query, *args)
    records = cursor.fetchall()
    connection.close()
    return records

def insert_dict_records(table_name, data_dict, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    for question, answer in data_dict.items():
        cursor.execute(f"SELECT * FROM {table_name} WHERE QUESTION = ? AND ANSWER = ?", (question, answer))
        result = cursor.fetchone()

        if not result:
            cursor.execute(f"INSERT INTO {table_name} (QUESTION, ANSWER) VALUES (?, ?)", (question, answer))

    connection.commit()
    connection.close()

def get_table_names(db_path):
    return [table[0] for table in fetch_query("SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence'", db_path)]

def read_records_as_dict(table_name, db_path):
    records = fetch_query(f"SELECT * FROM {table_name}", db_path)
    result_dict = {record[1]: record[2] for record in records}
    return result_dict

# Main functions accepting db_path as a keyword argument
def insert_exam(exam_name, tag, exam_data={}, db_path='/content/skill_builder_exams/exams.db'):
    table_structure = "ID INTEGER PRIMARY KEY AUTOINCREMENT, QUESTION VARCHAR(255), ANSWER VARCHAR(255)"
    existing_exam = fetch_query("SELECT * FROM TABLE_EXAMS WHERE EXAM_NAME = ?", db_path, (exam_name,))
    if not existing_exam:
        create_table(exam_name, table_structure, db_path)
        insert_dict_records(exam_name, exam_data, db_path)
        execute_query(f"INSERT INTO TABLE_EXAMS VALUES (NULL, '{tag}', '{exam_name}')", db_path)

def read_all_exams(tags=[], db_path='/content/skill_builder_exams/exams.db'):
    records = fetch_query("SELECT * FROM TABLE_EXAMS", db_path)
    table_names = get_table_names(db_path)

    filtered_table_names = [table_name for table_name in table_names if table_name not in ['sqlite_sequence', 'TABLE_EXAMS']] if not tags else \
    [record[2] for record in records if record[1] in tags]

    return [Exam(read_records_as_dict(table_name, db_path), table_name) for table_name in filtered_table_names]

def delete_exam(table_name, db_path='/content/skill_builder_exams/exams.db'):
    execute_query(f"DROP TABLE IF EXISTS {table_name}", db_path)
    execute_query(f"DELETE FROM TABLE_EXAMS WHERE EXAM_NAME='{table_name}'", db_path)

def delete_all_exams(db_path='/content/skill_builder_exams/exams.db'):
    for exam in read_all_exams(db_path=db_path):
        delete_exam(exam.exam_description, db_path)

def print_all_exams(db_path='/content/skill_builder_exams/exams.db'):
    tuples_list = fetch_query("SELECT * FROM TABLE_EXAMS", db_path)
    sorted_tuples_list = sorted(tuples_list, key=lambda x: x[1])

    # Adjusting the column widths in the format strings
    print("{:<20} {:<30} {:<15}".format("TAG", "EXAM", "QUESTIONS"))
    print("-" * 210)  # Adjusting the total length to match the new column widths

    for t in sorted_tuples_list:
        _, tag, exam = t
        questions_count = len(read_records_as_dict(exam, db_path))
        # Adjusting the column widths in the format strings for each row
        print("{:<20} {:<30} {:<15}".format(tag, exam, questions_count))
    print()


# sql.py

import sqlite3

def create_table(database_name, table_name, table_structure):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE TABLE {table_name} ({table_structure})")
        connection.commit()
        connection.close()
    except sqlite3.OperationalError:
        pass

def execute_query(database_name, query, *args):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute(query, *args)
    connection.commit()
    connection.close()

def fetch_query(database_name, query, *args):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()
    cursor.execute(query, *args)
    records = cursor.fetchall()
    connection.close()
    return records

def insert_record(database_name, record):
    execute_query(database_name, record)

def insert_several_records(database_name, multiple_records):
    for record in multiple_records:
        execute_query(database_name, record)

def read_records(database_name, table_name):
    return fetch_query(database_name, f"SELECT * FROM {table_name}")

def read_last_record(database_name, table_name):
    records = fetch_query(database_name, f"SELECT * FROM {table_name} ORDER BY ID DESC LIMIT 1")
    return records[0]

def update_record(database_name, record):
    execute_query(database_name, record)

def remove_record(database_name, record):
    execute_query(database_name, record)

def run_command(database_name, command):
    execute_query(database_name, command)

def insert_dict_records(database_name, table_name, data_dict):
    connection = sqlite3.connect(database_name)
    cursor = connection.cursor()

    for question, answer in data_dict.items():
        cursor.execute(f"SELECT * FROM {table_name} WHERE QUESTION = ? AND ANSWER = ?", (question, answer))
        result = cursor.fetchone()

        if not result:
            cursor.execute(f"INSERT INTO {table_name} (QUESTION, ANSWER) VALUES (?, ?)", (question, answer))

    connection.commit()
    connection.close()

def read_records_as_dict(database_name, table_name):
    records = fetch_query(database_name, f"SELECT * FROM {table_name}")
    result_dict = {record[1]: record[2] for record in records}
    return result_dict

def read_exam(table_name):
    return read_records_as_dict("/content/skill_builder_exams/exams.db", table_name)

def get_table_names(database_name):
    return [table[0] for table in fetch_query(database_name, "SELECT name FROM sqlite_master WHERE type='table' AND name != 'sqlite_sequence'")]

def insert_exam(exam_name, tag, exam_data={}):
    table_structure = """
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        QUESTION VARCHAR(255),
        ANSWER VARCHAR(255)
    """
    create_table("/content/skill_builder_exams/exams.db", exam_name, table_structure)
    insert_dict_records("/content/skill_builder_exams/exams.db", exam_name, exam_data)
    insert_record("/content/skill_builder_exams/exams.db",f"INSERT INTO TABLE_EXAM VALUES (NULL,'{exam_name}','{tag}')")

from skill_builder_exams.exam import Exam

def read_all_exams():
    return [Exam(read_exam(table_name), table_name) for table_name in get_table_names("/content/skill_builder_exams/exams.db")]

def delete_exam(table_name, database_name="/content/skill_builder_exams/exams.db"):
    execute_query(database_name, f"DROP TABLE IF EXISTS {table_name}")

def delete_all_exams():
    for exam in read_all_exams():
        delete_exam(exam.exam_description)


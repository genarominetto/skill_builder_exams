import sqlite3
from skill_builder_exams.exam import Exam

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

    # Check if the exam_name already exists in the TABLE_EXAMS
    existing_exam = fetch_query("/content/skill_builder_exams/exams.db", "SELECT * FROM TABLE_EXAMS WHERE EXAM_NAME = ?", (exam_name,))
    
    # If the exam_name does not exist, create the table and insert the exam
    if not existing_exam:
        create_table("/content/skill_builder_exams/exams.db", exam_name, table_structure)
        insert_dict_records("/content/skill_builder_exams/exams.db", exam_name, exam_data)
        insert_record("/content/skill_builder_exams/exams.db", f"INSERT INTO TABLE_EXAMS VALUES (NULL, '{tag}', '{exam_name}')")

def read_all_exams(tags=[]):
    records = read_records("/content/skill_builder_exams/exams.db", "TABLE_EXAMS")
    table_names = get_table_names("/content/skill_builder_exams/exams.db")

    if tags:
        filtered_records = [record for record in records if record[1] in tags]
        filtered_table_names = [record[2] for record in filtered_records]
    else:
        filtered_table_names = [table_name for table_name in table_names if table_name not in ['sqlite_sequence', 'TABLE_EXAMS']]

    return [Exam(read_exam(table_name), table_name) for table_name in filtered_table_names]


def delete_exam(table_name, database_name="/content/skill_builder_exams/exams.db"):
    execute_query(database_name, f"DROP TABLE IF EXISTS {table_name}")
    execute_query(database_name, f"DELETE FROM TABLE_EXAMS WHERE EXAM_NAME='{table_name}'")
    records = fetch_query(database_name, f"SELECT * FROM TABLE_EXAMS")
    execute_query(database_name, f"DELETE FROM TABLE_EXAMS")

    for i, record in enumerate(records, start=1):
        execute_query(database_name, f"INSERT INTO TABLE_EXAMS VALUES ({i}, '{record[1]}', '{record[2]}')")

def delete_all_exams():
    for exam in read_all_exams():
        delete_exam(exam.exam_description)
        
def print_all_exams():
    tuples_list = read_records("/content/skill_builder_exams/exams.db", "TABLE_EXAMS")
    
    # Sort the tuples_list by the tag (element at index 1)
    sorted_tuples_list = sorted(tuples_list, key=lambda x: x[1])

    print("{:<15} {:<15} {:<10}".format("EXAM", "TAG", "QUESTIONS"))
    print("-" * 40)

    # Loop through the sorted list to print exams grouped by their tags
    for t in sorted_tuples_list:
        _, tag, exam = t
        questions_count = len(read_exam(exam))
        print("{:<15} {:<15} {:<10}".format(exam, tag, questions_count))
    print()





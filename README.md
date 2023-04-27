# Skill Builder Exams

Skill Builder Exams is a Python program designed to manage and practice exams, allowing users to create, read, update, and delete exams, as well as practice them interactively.

## Main Files

- `exam.py`: Contains the Exam class definition and related methods.
- `practice.py`: Provides the function to practice exams interactively.
- `sql.py`: Offers functions to interact with the SQLite3 database (`exams.db`).
- `main.ipynb`: Jupyter Notebook to run the program.

## Key Functions

- `insert_exam(exam_name, questions)`: Inserts a new exam with the given name and questions into the database.
- `read_exam(exam_name)`: Retrieves a specific exam by its name from the database.
- `read_all_exams()`: Fetches all exams from the database.
- `delete_exam(exam_name)`: Deletes a specific exam by its name from the database.
- `delete_all_exams()`: Deletes all exams from the database.
- `practice(exams)`: Allows users to interactively practice the exams passed as an argument.

To use the program, open `main.ipynb` in a Jupyter Notebook or Google Colab, and execute all cells.

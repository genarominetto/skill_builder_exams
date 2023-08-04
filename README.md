# Skill Builder Exams
**To use the program**, open `main.ipynb` in a Jupyter Notebook or Google Colab, and **execute all cells**.

Skill Builder Exams is a Python program designed to manage and practice exams, allowing users to create, read, update, and delete exams, as well as practice them interactively.

## Main Files

- `main.ipynb`: Jupyter Notebook to run the program.
- `exam.py`: Contains the Exam class definition.
- `practice.py`: Provides the function to practice exams interactively.
- `sql.py`: Offers functions to interact with the SQLite3 database (`exams.db`).

## Key Functions

- `insert_exam(exam_name, tag, questions)`: Inserts a new exam into the database with a given question aswer dictionary.
- `read_exam(exam_name)`: Retrieves a specific exam by its name from the database.
- `read_all_exams(tags)`: Fetches exams from the database that match the tags in the given list. If the list is empty, it returns all exams.
- `delete_exam(exam_name)`: Deletes a specific exam by its name from the database.
- `delete_all_exams()`: Deletes all exams from the database.
- `practice(exams)`: Allows users to interactively practice the exams passed as an argument.

To use the program, open `main.ipynb` in a Jupyter Notebook or Google Colab, and execute all cells.

### Adding an Exam to the Database

To add an exam to the database, follow these steps:

1. Open `main.ipynb` in a Jupyter Notebook or Google Colab.
2. Execute all cells to ensure all required functions and dependencies are loaded.
3. Utilize the `insert_exam` function to add the desired exam. Example usage would be `insert_exam('Final Exam', 'mathematics', {'What is 2+2?': '4', 'What is 3+3?': '6'})`.
4. After inserting the exam, download the updated `exams.db` database file.
5. Commit and push the updated `exams.db` file to the repository.

This process will add the new exam with the given name, tag, and questions into the `exams.db` database, making it accessible for others using the system.

Welcomes contributions or feedback.

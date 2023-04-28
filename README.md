# Skill Builder Exams

This repository contains a Python program that allows users to practice different exams on various topics like programming languages or music theory. It consists of several Python files and a Jupyter Notebook.

## Table of Contents
- [Files](#files)
- [Usage](#usage)

## Files
- **exam.py**: Contains code related to exam functionality.
- **exams.db**: SQLite3 database that stores exam questions and related data.
- **main.ipynb**: Jupyter Notebook file to run the program in Google Colab.
- **practice.py**: Contains practice functionality to go through the questions.
- **sql.py**: Contains functions for interacting with the database.

## Usage
To use the program, open the  file in Google Colab and follow the instructions provided in the notebook.

### Import the code
To import the necessary code, run the following cell:

```
%%capture
!git clone https://github.com/GenaroHacker/skill_builder_exams.git

from skill_builder_exams.sql import insert_exam
from skill_builder_exams.sql import read_all_exams
from skill_builder_exams.sql import delete_exam
from skill_builder_exams.sql import delete_all_exams
from skill_builder_exams.practice import practice
```

### Practice
To practice exams, run the following cell:

```
practice(read_all_exams(["python","guitar"]))
```

Follow the prompts to select the exams you would like to practice.


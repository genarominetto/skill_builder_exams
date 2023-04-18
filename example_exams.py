def example_exams():
  CRUD = {'Adding new data to a database': 'Create',
  'Retrieving existing data from a database': 'Read',
  'Modifying existing data in a database': 'Update',
  'Removing data from a database': 'Delete'}
  BASH = {'Prints the current working directory': 'pwd',
  'Lists the contents of a directory': 'ls',
  'Changes the current directory': 'cd',
  'Creates an empty file': 'touch',
  'Displays the contents of a file': 'cat'}
  OOP = {
      'Focusing only on the essential features of an object or a class while ignoring the unnecessary details': 'Abstraction',
      'Bundling the data and the functions that manipulate the data within a single unit, which is known as a class': 'Encapsulation',
      'Allows a new class to be based on an existing class, inheriting its properties and methods': 'Inheritance',
      'Refers to the ability of an object to take on different forms or behaviors depending on the context in which it is used': 'Polymorphism',
      'A blueprint or a template for creating objects that defines a set of properties and methods that are common to all objects of that class': 'Class'
  }
  PYTHON_BASICS = {
  'A built-in Python function to calculate the length of a string or a list': 'len',
  'Used to create a comment in Python': '#',
  'A data type in Python that stores an ordered sequence of values': 'List',
  'A Python keyword used to create a loop that iterates over a sequence': 'for',
  'A Python keyword used to define a user-defined function': 'def'
  }

  EMPTY = {}

  exams = [
      Exam(
          CRUD,
          "CRUD"
      ),
      Exam(
          BASH,
          "Bash"
      ),
      Exam(
          OOP,
          "OOP"
      ),
      Exam(
          PYTHON_BASICS,
          "Python Basics"
      ),
      Exam(
          EMPTY,
          "Your title here"
      )
  ]
  return exams

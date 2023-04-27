
def delete_all_exams():
  for i in read_all_exams():
    delete_exam(i.exam_description)

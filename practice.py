from skill_builder_exams.sql import read_all_exams

def practice(tags, db_path='/content/skill_builder_exams/exams.db'):
    exams = read_all_exams(tags, db_path=db_path)
    print(f"{len(exams)} exams selected.\n")
    import random
    random.shuffle(exams)
    for exam in exams:
        questions_count = len(exam.question_answer_dict)
        response = input(f"Do you want to practice {exam.exam_description}? (y/n) {questions_count} questions.\n")
        if response.lower() == "y":
            print(f"Practicing ---{exam.exam_description}---")
            exam.practice_row()  # Assuming this method exists within the Exam class
            print()
        else:
            print(f"Skipping ---{exam.exam_description}---")
            print()

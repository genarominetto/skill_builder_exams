from skill_builder_exams.sql import read_all_exams

def practice(tags):
    exams = read_all_exams[tags]
    print(str(len(exams)) + " exams selected.")
    print()
    import random
    random.shuffle(exams)
    for exam in exams:
        response = input("Do you want to practice " + exam.exam_description + "? (y/n) " + str(len(exam.question_answer_dict)) + " questions.\n")
        if response.lower() == "y":
            print("Practicing ---" + exam.exam_description + "---")
            exam.practice_row()
            print()
        else:
            print("Skipping ---" + exam.exam_description + "---")
            print()

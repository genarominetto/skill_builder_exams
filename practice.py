def practice(exams):
    print(str(len(exams)) + " exams selected.")
    print()
    import random
    random.shuffle(exams)
    for exam in exams:
        response = input("Do you want to practice " + exam.exam_description + "? (y/n) " + str(len(exam.question_answer_dict)) + " questions.\n")
        if response.lower() == "y":
            print("Practicing ---" + exam.exam_description + "---")
            exam.practice_row()
        else:
            print("Skipping ---" + exam.exam_description + "---")

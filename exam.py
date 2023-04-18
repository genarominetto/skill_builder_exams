import random

class Exam:
    def __init__(self, question_answer_dict, exam_description):
        self.question_answer_dict = question_answer_dict
        self.exam_description = exam_description

    def practice_row(self):
        d = self.question_answer_dict
        while d != {}:
            # Extract a list of keys:
            key_list = list(d.keys())

            # Randomize the order of the keys:
            random.shuffle(key_list)

            score = 0
            max_score = len(key_list)
            for key in key_list:
                print("---->  " + key + "?")
                answer = input("? ")
                if answer.upper() == d[key].upper():
                    print("✔")
                    print("")
                    score += 1
                    d.pop(key)
                else:
                    print("✘")
                    print("The correct answer is --> ", (d[key]).upper())
                    print("---->  " + key)
                    answer = input("? ")
                    while answer.upper() != d[key].upper():
                        print("---->  " + key)
                        answer = input("? ")
                    print("")

            print("")       
            print("-------------------------------------------------------------------------")
            print("Your score is: " + str(score) + "/" + str(max_score))
            print("-------------------------------------------------------------------------")
            print("")

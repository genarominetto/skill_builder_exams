import random
import time
class Exam:
    def __init__(self, question_answer_dict, exam_description):
        self.question_answer_dict = question_answer_dict
        self.exam_description = exam_description
    def practice_row(self):
        d = self.question_answer_dict
        start_time = time.time()
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
        end_time = time.time()
        time_taken = end_time - start_time
        minutes, seconds = divmod(time_taken, 60)
        print("")       
        print("-------------------------------------------------------------------------")
        print(f"Your score is: {score}/{max_score}")
        print(f"Time taken: {int(minutes)} minutes and {int(seconds)} seconds")
        print("-------------------------------------------------------------------------")
        print("")

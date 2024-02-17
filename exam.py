import random
import time

class Exam:
    def __init__(self, question_answer_dict, exam_description):
        self.question_answer_dict = question_answer_dict
        self.exam_description = exam_description

    def practice_row(self):
        d = self.question_answer_dict.copy()
        start_time = time.time()
        first_round_score = None
        max_score = len(d)  # Moved max_score initialization here

        while d != {}:
            key_list = list(d.keys())
            random.shuffle(key_list)
            score = 0
            for key in key_list:
                print(" ---->  " + key + "?")
                answer = input(" <---- ")
                if answer.upper() == d[key].upper():
                    print(" ---->  ✔")
                    print("\n\n\n\n\n\n\n\n\n\n")
                    score += 1
                    d.pop(key)
                else:
                    while answer.upper() != d[key].upper():
                        print(" ---->  ✘")
                        print(f' ---->  The correct answer is "{(d[key]).upper()}"')
                        print()
                        print(" ---->  " + key + "?")
                        answer = input(" <---- ")
                    print(" ---->  ✔")
                    print("\n\n\n\n\n\n\n\n\n\n")

            if first_round_score is None:
                first_round_score = score

        end_time = time.time()
        time_taken = end_time - start_time
        minutes, seconds = divmod(time_taken, 60)
        print("")
        print("-------------------------------------------------------------------------")
        print(f"{self.exam_description} test finished.")
        print(f"Your score was: {first_round_score}/{max_score}")  # Now max_score is the total number of questions
        print(f"Time taken: {int(minutes)} minutes and {int(seconds)} seconds")
        print("-------------------------------------------------------------------------")
        print("")

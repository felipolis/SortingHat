import os
import sys
from time import sleep
from lib import interface
from lib import hat
from lib import questions
from lib import houses


def after_question():
    sleep(1)
    os.system('cls')
    hat.hat_ideas()
    sleep(1)

# ----------------main
os.system('cls')
interface.about()
os.system('cls')
hat.presentation()
while True:
    os.system('cls')
    interface.start()

    choice = str(input(">>>>> ")).strip().upper()[0]

    if choice == "A":
        break
    elif choice == "B":
        sys.exit()
    else:
        print("[WARNING] You should write A or B!!!")
        sleep(3)

os.system('cls')
# Question 01
answ1 = questions.first_question()
after_question()
# Question 02
answ2 = questions.second_question()
after_question()
# Question 03
answ3 = questions.third_question()
after_question()
# Question 04
answ4 = questions.fourth_question()
after_question()
# Question 05
answ5 = questions.fifth_question()
after_question()
# Question 06
answ6 = questions.sixth_question()
after_question()
# Question 07
answ7 = questions.seventh_question()
after_question()
# Question 08
answ8 = questions.eighth_question()
after_question()

results = list()
for i in range(0, 4):
    num = (answ1[i] + answ2[i] + answ3[i] + answ4[i] + answ5[i] + answ6[i] + answ7[i] + answ8[i])
    results.append(num)

# print(results)
# sleep(2)
if results[0] == max(results):
    os.system('cls')
    hat.hat_speaking(1)
    os.system('cls')
    houses.sorting_griffindor()
elif results[1] == max(results):
    os.system('cls')
    hat.hat_speaking(2)
    os.system('cls')
    houses.sorting_ravenclaw()
elif results[2] == max(results):
    os.system('cls')
    hat.hat_speaking(3)
    os.system('cls')
    houses.sorting_hufflepuff()
elif results[3] == max(results):
    os.system('cls')
    hat.hat_speaking(4)
    os.system('cls')
    houses.sorting_slytherin()

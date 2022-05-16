import random
from tkinter import*
import requests
import html

# Constant
QUESTIONS_URL = "https://opentdb.com/api.php?amount=50&category=18&type=multiple"
FONT = ("Courier", 20, "bold")
AS_FONT = ("Courier", 15, "bold")

# Properties
questions = requests.get(QUESTIONS_URL).json()["results"]
index = 0
score = 0
answer_collection = []

# Color
CYBER = "#80ffdf"
WHITE = "#ffffff"
GREEN = "#00ff00"

#--------Functions-----
def check_answer(anwer):
    global score, index

    if anwer == questions[index]['correct_answer']:
        score += 1
        display_score.config(text=f"Score: {score}")
        index += 1
        print("True")
        text_area.config(text=f"{generate_question()}")
        option1.config(text=f"{answer_collection[0]}")
        option2.config(text=f"{answer_collection[1]}")
        option3.config(text=f"{answer_collection[2]}")

    else:
        index += 1
        text_area.config(text=f"{generate_question()}")
        option1.config(text=f"{answer_collection[0]}")
        option2.config(text=f"{answer_collection[1]}")
        option3.config(text=f"{answer_collection[2]}")
        print("False")


# Get the question and generate the answer
def generate_question():
    global counter, questions, index, answer_collection
    get_question = questions[index]["question"]
    get_question = html.unescape(get_question)
    del(answer_collection)
    answer_collection = [html.unescape(questions[index]['incorrect_answers'][0]), html.unescape(questions[index]['incorrect_answers'][1]),
                         html.unescape(questions[index]['correct_answer'])]
    random.shuffle(answer_collection)
    return get_question

# -----------UI-------------
window = Tk()
window.config(pady=10, padx=10, height=400, bg=CYBER)

# Get var from ratio button
var = StringVar()

img_false = PhotoImage(file="./img/false.png")
img_true = PhotoImage(file="./img/true.png")

display_score = Label(text=f"Score: {score}",bg=CYBER, font=FONT)
display_score.grid(column=0, row=0)

text_area = Label(text=f"{generate_question()}", bg=WHITE, wraplength=300, height=10, width=20, font=FONT)
text_area.grid(column=0, row=1, columnspan=2, sticky='w')

option1 = Button(text=f"{answer_collection[0]}", bg=WHITE, font=AS_FONT, pady=10, command=lambda : check_answer(answer_collection[0]))
option1.grid(column=0, row=2, columnspan=2, sticky='w', pady=5)

option2 = Button(text=f"{answer_collection[1]}", bg=WHITE, font=AS_FONT, command=lambda : check_answer(answer_collection[1]))
option2.grid(column=0, row=3, columnspan=2, sticky='w', pady=5)

option3 = Button(text=f"{answer_collection[2]}", bg=WHITE, font=AS_FONT, command=lambda: check_answer(answer_collection[2]))
option3.grid(column=0, row=4, columnspan=2, sticky='w', pady=5)

window.mainloop()




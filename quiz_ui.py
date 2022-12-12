from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


def quiz(quiz_brain):

    
    qb = quiz_brain
    root = Tk()
    root.title("GyaniBot Quiz")
    root.geometry("850x530")

    user_answer = StringVar()


    def display_title():
        """To display title"""

        # Title
        title = Label(root, text="GyaniBot Quiz",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    def display_question():
        """To display the question"""

        q_text = qb.next_question()
        canvas.itemconfig(question_text, text=q_text)

    def radio_buttons():
        """To create four options (radio buttons)"""

        # initialize the list with an empty list of options
        choice_list = []

        # position of the first option
        y_pos = 220

        # adding the options to the list
        while len(choice_list) < 4:

            # setting the radio button properties
            radio_btn = Radiobutton( text="", variable=user_answer,
                                    value='', font=("ariel", 14),master=root)

            # adding the button to the list
            choice_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=200, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return choice_list

    def display_options():
        """To display four options"""

        val = 0

        # deselecting the options
        user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in qb.current_question.choices:
            opts[val]['text'] = option
            opts[val]['value'] = option
            val += 1

    display_title()

        # Creating a canvas for question text, and dsiplay question
    canvas = Canvas(width=800, height=250,master=root)
    question_text = canvas.create_text(400, 125,
                                                     text="Question here",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
    canvas.grid(row=2, column=0, columnspan=2, pady=50)
    display_question()

        # Declare a StringVar to store user's answer

        # Display four options(radio buttons)
    opts = radio_buttons()
    display_options()
    def display_result():
        """To display the result using messagebox"""
        correct, wrong, score_percent = qb.get_score()

        correct = f"Correct: {correct}"
        wrong = f"Wrong: {wrong}"

        # calculates the percentage of correct answers
        result = f"Score: {score_percent}%"

        # Shows a message box to display the result
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        # Display Title
    def next_btn():
        """To show feedback for each answer and keep checking for more questions"""

        # Check if the answer is correct
        if qb.check_answer(user_answer.get()):
            print(user_answer.get())
            feedback["fg"] = "green"
            feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            feedback['fg'] = 'red'
            feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {qb.current_question.correct_answer}')

        if qb.has_more_questions():
            # Moves to next to display next question and its options
            display_question()
            display_options()
        else:
            # if no more questions, then it displays the score
            display_result()

            # destroys the self.window
            root.destroy()

    def buttons():
        """To show next button and quit button"""

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(root, text="Next", command=next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # palcing the button  on the screen
        next_button.place(x=350, y=460)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(root, text="Quit", command=root.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700, y=50)


        # To show whether the answer is correct or wrong
    feedback = Label(root, pady=10, font=("ariel", 15, "bold"))
    feedback.place(x=300, y=380)

        # Next and Quit Button
    buttons()

        # Mainloop
    root.mainloop()


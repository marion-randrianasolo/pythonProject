import tkinter.messagebox
from moordle import Moordle
import random
from tkinter import *

# Data to load
question_set = Moordle.load_question_set("quiz.py")
# Picks some lyrics randomly
lyrics = random.choice(list(question_set))
# Title of the song picked randomly
title_a = question_set.get(lyrics)
# Create a moordle entity
moordle = Moordle(title_a)

# Get the generated lyrics
def generate_lyrics_q():
    return lyrics

# Check if the answer is right
def check_guess():
    feedback = Label(root, font=("ariel", 15, "bold"), bg="black", justify="center")
    feedback.place(x=230, y=350)
    feedback["fg"] = "green"
    if moordle.can_attempt:
        guess = guess_entry.get()
        guess = guess.upper()
        moordle.attempt(guess)
        if guess == title_a:
            tkinter.messagebox.showinfo("Réponse", "Slay ! You got it ! ")
        else:
            tkinter.messagebox.showinfo("Réponse", "Ooop.. ")
    else:
        feedback["text"] = 'The answer is : ' + title_a

# GUI creation with tkinter
root = Tk()
root.title("Moordle")
root.geometry("800x400")
root.resizable(False,False)


# Creating a canvas for question text,
canvas = Canvas(root, bg="black", width=850, height=530)
canvas.pack()

# Display text
canvas.create_text(400, 80, text="A 마마무(MAMAMOO) GUESSING GAME",
                                width=500,
                                font=('Arial', 20, 'bold'), justify="center", fill="#a1f0b6")

canvas.create_text(400, 140, text="Guess which song are these lyrics from : ",
                                width=500,
                                font=('Arial', 13, 'italic'), justify="center", fill="white")

canvas.create_text(400, 180, text="\""+ generate_lyrics_q()+ "\"",
                                width=500,
                                font=('Arial', 15, 'bold'), justify="center", fill="white")
canvas.create_text(400, 230, text="The only rule : you have 5 tries.. are you a MooMoo ?",
                                width=300,
                                font=('Arial', 9, 'italic'), justify="center", fill="white")
# Display Title
title = Label(root, text="Moordle", width=50, bg="#a1f0b6", fg="black", justify="center" ,font=("ariel", 20, "bold"))
title.place(x=-80, y=0)

# Label for entry
prompt_label = Label(root, text="Enter your guess :", bg="black", fg="white")
prompt_label.place(x=150, y=250)

# Add an entry field for the player to enter their guess
guess_entry = Entry(root, bg="black", fg="white", justify="center", width=40)
guess_entry.place(x=300, y=250)

# Submit button
submit_button = Button(root, text="Submit", command=check_guess,
                       width=5, bg="green", fg="white", font=("ariel", 16, " bold"))
submit_button.place(x=350, y=290)

# This is the second button which is used to Quit the self.window
quit_button = Button(root, text="Quit", command=root.destroy,
                     width=5, bg="red", fg="white", font=("ariel", 16, " bold"))
# Placing the Quit button on the screen
quit_button.place(x=696, y=360)

# Run the GUI
root.mainloop()

import tkinter as tk
from tkinter import simpledialog, Tk
from PIL import Image, ImageTk
from playsound import playsound




def animals():
    global window
    window = Tk()
    window.withdraw()

    # TODO 1. Ask the user which animal they want, then see and
    #  hear the animal they chose using one of the methods below.


    # TODO 2. Make it so that the user can keep entering new animals.


    while True:
        user_answer = simpledialog.askstring(None, " Do you want a cat, dog, duck, llama, or cow? ")

        if user_answer == "cow":
             moo()

        elif user_answer == "dog":
            woof()

        elif user_answer == "duck":
            quack()

        elif user_answer == "cat":
            meow()

        elif user_answer == "llama":
            llama_scream()

        elif user_answer == "exit":
            exit()

        else:
            ask()



    # TODO 3. If the user enters 'exit', stop the program


# ======================= DO NOT EDIT THE CODE BELOW =========================

def show_image(filename=None):
    try:
        image = Image.open(filename)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)
        return

    # Put the image on the Tk window used by simpledialog so that when the
    # window with the image is closed, the interpreter moves to the next
    # line of code
    global window
    window.deiconify()
    image = ImageTk.PhotoImage(image)
    tk.Label(master=window, image=image).pack()

    # Blocks so picture can be shown--resumes when picture window is closed
    window.mainloop()

    # Regenerate a new window after closing so more simpledialogs and
    # images can be shown
    window = Tk()
    window.withdraw()

def ask():
    user_answer = simpledialog.askstring(None, " Do you want a cat, dog, duck, llama, or cow? ")



def moo():
    show_image('cow.jpg')
    playsound('moo.wav')


def quack():
    show_image('duck.jpg')
    playsound('quack.wav')


def woof():
    show_image('dog.jpg')
    playsound('woof.wav')


def meow():
    show_image('cat.jpg')
    playsound('meow.wav')


def llama_scream():
    show_image('llama.jpg')
    playsound('llama.wav')


if __name__ == '__main__':
    animals()

import random
from tkinter import messagebox, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    random_number = random.randint(1, 5)

    print(random_number)

    # TODO 1) Use each value of random_number to give the user a random compliment

    # TODO 2) Repeat all the code above 10 times

    # TODO 3) Find someone to test out your program. They will like it :)
<<<<<<< HEAD
=======

    for i in range (10):

        if random_number == 1:
            messagebox.showinfo(None,"You look amazing today!")

        elif random_number == 2:
            messagebox.showinfo(None, "You are the best!")

        elif random_number == 3:
            messagebox.showinfo(None,"You light up the room!")

        elif random_number == 4:
            messagebox.showinfo(None,"You have the best smile!")
>>>>>>> 658340c (Initial commit)

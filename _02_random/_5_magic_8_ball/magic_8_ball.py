import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

<<<<<<< HEAD
=======
    random_number = random.randint(0, 3)

    user_answer = simpledialog.askstring(None,"Ask a question for the 8 ball")

>>>>>>> 658340c (Initial commit)
    # TODO Get the user to enter a question for the 8 ball to answer

    # Make a variable and initialize it to a random number between 0 and 3

    # If the random number is 0

        # tell the user "Yes"
<<<<<<< HEAD

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
=======
    if random_number == 0:
        messagebox.showinfo(None, "yes")

        # If the random number is 1

            # tell the user "No"

    elif random_number == 1:
        messagebox.showinfo(None, "no")

        # If the random number is 2

            # tell the user "Maybe you should ask Google?"

    elif random_number == 2:
        messagebox.showinfo(None, "maybe you should ask Google?")

        # If the random number is 3

            # write your own answer
    else:
        messagebox.showinfo(None, "maybe")
>>>>>>> 658340c (Initial commit)

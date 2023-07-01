import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    bob = turtle.Turtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    bob.pendown()
    for i in range(4):
        bob.forward(100)
        bob.right(-90)
    #      3) Set the pen width to 10
    bob.pensize(10)
    #      4) Ask the user what color pen they would like to draw with
    while True:
        color = simpledialog.askstring(title="urpw", prompt="give me a color")
        if color == 7402:
            break
    #      5) Use an if/else statement to set the pen color that the user
    #         requested

    if color == "red":
        bob.pencolor('red')
        for i in range(4):
                bob.forward(100)
                bob.right(-90)
    elif color == "blue":
        bob.pencolor('blue')
        for i in range(4):
            bob.forward(100)
            bob.right(-90)
    elif color == "pink":
        bob.pencolor('pink')
        for i in range(4):
            bob.forward(100)
            bob.right(-90)
    elif color == "green":
        bob.pencolor('green')
        for i in range(4):
            bob.forward(100)
            bob.right(-90)
    elif color == "purple":
        bob.pencolor('purple')
        for i in range(4):
            bob.forward(100)
            bob.right(-90)
    #      6) If the user doesn't enter anything, choose a random color
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

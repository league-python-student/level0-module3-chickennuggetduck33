import turtle

if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')
    my_turtle.color('blue', 'green')
    my_turtle.speed(100)

    # TODO 1) Set the X position of the turtle so that it starts on the left.
    my_turtle.penup()
    my_turtle.goto(-475,3)
    # TODO 2) Make the turtle draw a star shape. Hint: angle=144.

    for i in range(9):
        for i in range(5):
            my_turtle.pendown()
            my_turtle.forward(30)
            my_turtle.left(144)
            my_turtle.penup()
        my_turtle.forward(80)
    # TODO 3) Set the length of each line in the star to 30

    # TODO: CHALLENGE
    #       Make the turtle draw a line of stars like the image in
    #       this folder.
    #       Hint: The distance between stars is 50.

# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

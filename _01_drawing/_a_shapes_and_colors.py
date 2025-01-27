import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    aidan = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    aidan .shape('turtle')

    # Set your turtle's speed using .speed(2)
    aidan .speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    aidan .color('green')
    aidan .pencolor('blue')
    # Move your turtle forward using .forward(100)
    for i in range(4):
        aidan .forward(100)
        aidan .left(90)

    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)


    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    aidan .goto (50,0)
    # x=0 and y=0 is the center of the screen

    # Have your turtle draw a circle using .circle(radius, steps=30)
    aidan .begin_fill()
    aidan .circle(50, steps=30)
    aidan .end_fill()
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!

    aidan .goto(200,200)
    aidan .color('orange')
    aidan .begin_fill()
    for i in range(5):
        aidan .forward(100)
        aidan .left(72)
    aidan .end_fill()
    aidan .color('green')

    aidan .goto(-100,200)
    aidan .color('red')
    aidan . begin_fill()
    for i in range(8):
        aidan .forward(60)
        aidan . right(360/8)
    aidan .end_fill()

    aidan .goto(-200,-100)
    aidan .color('purple')
    aidan .begin_fill()
    aidan .forward(100)
    aidan .left(150)
    aidan .forward(50)
    aidan .left(30)
    aidan .forward(13.3975)
    aidan .left(30)
    aidan .forward(50)
    aidan .end_fill()

    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()

from turtle import Screen, Turtle

def square(size):
    count = 0

    if turtle.filling():
        turtle.pensize(5)
    else:
        turtle.pensize(3)

    while count < 4:
        turtle.forward(size)
        turtle.right(90)
        count += 1

def drawing(number):
    red = 30
    green = 10
    blue = 20

    times = 0

    while times < number:
        turtle.color(red % 255, green % 255, blue % 255)

        turtle.begin_fill()
        square(size)
        turtle.end_fill()

        turtle.right(360 / number)

        red, green, blue = red + 20, green + 30, blue + 10
        times += 1

size = 200
number = 100

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.speed('fastest')  # because I have no patience

drawing(number)

screen.exitonclick()

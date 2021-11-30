import turtle


def draw_star(size,color):
    count=0
    angle=144
    while count<=5:
        turtle.forward(size)
        turtle.right(angle)
        count += 1
    return
draw_star(100,"purple")
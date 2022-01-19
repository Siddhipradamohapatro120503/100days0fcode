from turtle import*

bgcolor('red')
pencolor('magenta')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for i in range(4):
    forward(250)
    circle(34,90)

penup()
goto(85,30)
pendown()
circle(80,360)
pendown()
circle(7,360)

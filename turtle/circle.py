import turtle

rohan = turtle.Turtle()

# rohan.circle(50)
rohan.color("red", "yellow")
i = 20
rohan.begin_fill()
while i <= 200:
    rohan.circle(i)
    i = i+30
rohan.end_fill()
turtle.done()

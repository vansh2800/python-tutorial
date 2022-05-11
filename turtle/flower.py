import turtle
# import math
neha = turtle.Turtle()
neha.speed(0)

n = 100
neha.color("red", "yellow")
neha.begin_fill()
for i in range(0, n):
    neha.fd(200)
    neha.lt(170)
    if abs(neha.pos()) < 1:
        break
neha.end_fill()
turtle.done()

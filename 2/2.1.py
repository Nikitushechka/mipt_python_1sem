import turtle
from random import randint
turtle.shape('turtle')
for i in range(30):
    x=randint(50,100)
    y=randint(0,360)
    turtle.forward(x)
    turtle.left(y)

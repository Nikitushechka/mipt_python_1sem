import turtle
turtle.shape('turtle')
n=20
while n<200:
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    turtle.pendown()
    n+=20
    
    

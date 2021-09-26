import turtle
turtle.shape('turtle')
x=1
y=1
z=1
a=1
b=1
turtle.up()
turtle.goto(0,-5)
turtle.down()
def ok(x):
    turtle.color('black','yellow')
    turtle.begin_fill()
    for x in range (100):
        turtle.forward(3)
        turtle.left(3.6)
    turtle.end_fill()    
def ol(y):
    turtle.up()
    turtle.goto(-15,50)
    turtle.down()
    turtle.color('black','blue')
    turtle.begin_fill()
    for x in range (100):
        turtle.forward(0.5)
        turtle.left(3.6)
    turtle.end_fill()
def om(z):
    turtle.up()
    turtle.goto(15,50)
    turtle.down()
    turtle.color('black','blue')
    turtle.begin_fill()
    for x in range (100):
        turtle.forward(0.5)
        turtle.left(3.6)
    turtle.end_fill()
def op(a):
    turtle.up()
    turtle.goto(0,40)
    turtle.down()
    turtle.color('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.width(10)
    turtle.forward(10)
    turtle.end_fill()
def oc(b):
    turtle.up()
    turtle.goto(-20,20)
    turtle.down()
    turtle.width(5)
    turtle.color('red',)
    turtle.left(30)
    for x in range (100):
        turtle.forward(0.5)
        turtle.left(1.2)
for i in range(1):
    ok(x)
    ol(y)
    om(z)
    op(a)
    oc(b)

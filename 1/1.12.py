import turtle
turtle.shape('turtle')
x=int(turtle.textinput('Введите количество вершин', 'Введите количество вершин: '))
def ok(x):
    turtle.up()
    turtle.goto(40,30)
    turtle.left(180)
    turtle.down()
    for i in range(x):
        turtle.forward(80)
        turtle.left(180-(180/x))
ok(x)        

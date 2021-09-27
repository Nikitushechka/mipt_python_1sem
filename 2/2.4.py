import turtle
turtle.shape('turtle')
x=0
y=0
V1=30
V2=40
dt=0.1
g=10
i=1
while i<=83:
    turtle.goto(x,y)
    x+=V1*dt
    y+=V2*dt+g*dt**2/2
    V1+=0
    V2+=-g*dt
    i+=1
    

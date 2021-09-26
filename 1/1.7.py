import turtle                                         
import numpy as np
import math
turtle.shape('turtle')                                     
R = 30                                                
x = 1                                                 
n = 3
turtle.up()
turtle.goto(R,0)
turtle.down()
def ok(x):
    while x<=n:
        turtle.left((180 - 360 / n) / 2)                   
        turtle.left(360 / n)                               
        turtle.forward(2 * R * math.sin(math.pi/n))        
        x += 1                                        
        turtle.right((180 - 360 / n) / 2)     
while n<=10:
    ok(x)
    R+=10
    n+=1
    turtle.up()
    turtle.goto(R,0)
    turtle.down()
    
    

    

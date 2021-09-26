import turtle
import numpy as np

turtle.shape('turtle')
for i in range(400):
    u=i/30
    p=(1/6)*u
    
    turtle.forward(p*np.sqrt(1+u**2))
    turtle.left(u)

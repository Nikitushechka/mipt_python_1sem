import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 700))

pygame.draw.rect(screen,(70,50,0), (0,0,1000,350))       #фон
pygame.draw.rect(screen,(184, 134, 11), (0,350,1000,700))

pygame.draw.ellipse(screen, (255, 140, 0), (310,400,100,50)) #хвост
pygame.draw.ellipse(screen, (0, 0, 0), (310,400,100,50),2)

pygame.draw.ellipse(screen, (255, 140, 0), (50,370,280,150)) #туловище
pygame.draw.ellipse(screen, (0, 0, 0), (50,370,280,150),2)

pygame.draw.ellipse(screen, (255, 140, 0), (25,370,100,80)) #голова
pygame.draw.ellipse(screen, (0, 0, 0), (25,370,100,80),2)

pygame.draw.ellipse(screen, (255, 140, 0), (50,480,100,50)) #передняя лапа
pygame.draw.ellipse(screen, (0, 0, 0), (50,480,100,50),2)

pygame.draw.circle(screen, (255, 140, 0), (300, 500), 50)  #задняя лапа
pygame.draw.circle(screen, (0, 0, 0), (300, 500), 50,2)
pygame.draw.ellipse(screen, (255, 140, 0), (330,500,30,80))
pygame.draw.ellipse(screen, (0, 0, 0), (330,500,30,80),2)

pygame.draw.circle(screen, (0, 255, 0), (55, 410), 10)
pygame.draw.circle(screen, (0, 0, 0), (55, 410), 10,2) #глаз1

pygame.draw.ellipse(screen, (0, 0, 0), (55,404,5,14)) #зрачок1

pygame.draw.circle(screen, (0, 255, 0), (95, 410), 10) #глаз2
pygame.draw.circle(screen, (0, 0, 0), (95, 410), 10,2)

pygame.draw.ellipse(screen, (0, 0, 0), (95,404,5,14)) #зрачок2

pygame.draw.polygon(screen,(200,190,140),[[90, 380], [110, 360],[113, 390]]) #ухо1
pygame.draw.lines(screen,(255, 140, 0),True,[[90, 380], [110, 360],[113, 390]],7)
pygame.draw.lines(screen,(0, 0, 0),True,[[87, 380], [112, 357],[117, 391]],2)

pygame.draw.polygon(screen,(200,190,140),[[60, 380], [40, 360],[37, 390]]) #ухо2
pygame.draw.polygon(screen,(255,140,0),[[60, 380], [40, 360],[37, 390]],7)
pygame.draw.lines(screen,(0, 0, 0),True,[[62, 380], [38, 355],[35, 391]],2)

pygame.draw.arc(screen, (0,0,0),(65, 420, 10, 15),8*np.pi/6, 2*np.pi, 1) #усынос
pygame.draw.arc(screen, (0,0,0),(75, 420, 10, 15), np.pi,10*np.pi/6, 1)
pygame.draw.polygon(screen,(200,190,140),[[75, 425], [80,420],[70, 420]])

pygame.draw.rect(screen,(0, 0, 225), (200,30,180,280))
pygame.draw.rect(screen,(225, 225, 225), (200,30,180,280),10)  #окно
pygame.draw.line(screen,(225, 225, 225),[290,310],[290,30],10)
pygame.draw.line(screen,(225, 225, 225),[200,170],[380,170],10)

pygame.draw.circle(screen, (200, 200, 200), (300, 610), 40) #клубок

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

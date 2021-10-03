import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


rect(screen, (125, 125, 125), (0, 0, 400, 400))
circle(screen, (225, 255, 0), (200, 175), 120)
circle(screen, (255,0,0), (160, 150), 23)
circle(screen, (0,0,0), (200, 175), 120,2)
circle(screen, (0,0,0), (160, 150), 23,2)
pygame.draw.polygon(screen, (0,0,0), [[100, 90],[230, 115],[205,140],[75,115]]) 
circle(screen, (225,0,0), (250, 150), 15)
pygame.draw.polygon(screen, (0,0,0), [[230, 125],[340, 115],[330,135],[220,145]])
circle(screen, (0,0,0), (250, 150), 15,2)
rect(screen, (0, 0, 0), (120, 220, 160, 30))
circle(screen, (0,0,0), (160, 150), 12)
circle(screen, (0,0,0), (250, 150), 6)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

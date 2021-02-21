import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (0, 0, 0), (200, 200), 155)
circle(screen, (255, 255, 0), (200, 200), 150)

line(screen, (0, 0, 0), [50, 50], [150, 150], 20)
line(screen, (0, 0, 0), [250, 150], [350, 50], 20)
circle(screen, (128, 0, 0), (150, 150), 50)
circle(screen, (128, 0, 0), (250, 150), 50)
circle(screen, (0, 0, 0), (150, 175), 15)
circle(screen, (0, 0, 0), (250, 175), 15)
line(screen, (0, 0, 0), [100, 300], [300, 300], 20)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
SnoopDogg = pygame.Surface((600, 800))
SnoopDogg.set_colorkey((0, 0, 0))
screen = pygame.display.set_mode((600, 800))

rect(screen, (0, 255, 255), (0, 0, 600, 400))  # небо

rect(screen, (0, 128, 0), (0, 401, 600, 400))  # трава


def fence(x_fence, y_fence, l_fence, h_fence):
    rect(screen, (128, 128, 0), (x_fence, y_fence, l_fence, h_fence))  # забор (прямоугольник)

    n = 10
    color = (255, 255, 255)
    rect(screen, color, (x_fence, y_fence, l_fence, h_fence), 2)
    h = l_fence // (n + 1)
    x = x_fence
    for i in range(n):
        x += h
        line(screen, color, (x, y_fence), (x, y_fence + h_fence))


fence(30, 40, 600, 400)
fence(0, 0, 500, 300)
fence(10, 10, 400, 400)
fence(300, 40, 300, 200)
fence(0, 0, 200, 200)
fence(10, 10, 100, 500)

# будка + цепь
polygon(screen, (235, 191, 0), [[350, 450], [350, 650], [500, 700], [550, 650], [550, 450], [450, 300], [400, 350]])
aalines(screen, (0, 0, 0), False,
        [[350, 450], [350, 650], [500, 700], [550, 650], [550, 450], [450, 300], [400, 350], [500, 500], [500, 700]])
aalines(screen, (0, 0, 0), False, [[400, 350], [350, 450], [500, 500], [550, 450]])
ellipse(screen, (0, 0, 0), (375, 500, 100, 150))
pi = 3.14
arc(screen, (255, 255, 0), (355, 610, 15, 30), 0, pi, 4)
arc(screen, (255, 255, 0), (355, 610, 15, 30), pi, 2 * pi, 4)
arc(screen, (255, 255, 0), (357, 630, 15, 30), 0, pi, 4)
arc(screen, (255, 255, 0), (357, 630, 15, 30), pi, 2 * pi, 4)
arc(screen, (255, 255, 0), (355, 650, 15, 30), 0, pi, 4)
arc(screen, (255, 255, 0), (355, 650, 15, 30), pi, 2 * pi, 4)
arc(screen, (255, 255, 0), (345, 665, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (345, 665, 30, 15), pi, 2 * pi, 4)
arc(screen, (255, 255, 0), (325, 663, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (325, 663, 30, 15), pi, 2 * pi, 4)
arc(screen, (255, 255, 0), (305, 665, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (305, 665, 30, 15), pi, 2 * pi, 4)
arc(screen, (255, 255, 0), (285, 663, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (285, 663, 30, 15), pi, 2 * pi, 4)
arc(screen, (255, 255, 0), (265, 665, 30, 15), 0, pi, 4)
arc(screen, (255, 255, 0), (265, 665, 30, 15), pi, 2 * pi, 4)

# собака-кусака
ellipse(SnoopDogg, (153, 102, 0), (50, 580, 120, 70))
ellipse(SnoopDogg, (153, 102, 0), (150, 590, 90, 45))
ellipse(SnoopDogg, (153, 102, 0), (200, 600, 50, 50))
ellipse(SnoopDogg, (153, 102, 0), (150, 580, 50, 50))
ellipse(SnoopDogg, (153, 102, 0), (235, 620, 20, 50))
ellipse(SnoopDogg, (153, 102, 0), (180, 600, 20, 50))
ellipse(SnoopDogg, (153, 102, 0), (220, 665, 30, 10))
ellipse(SnoopDogg, (153, 102, 0), (165, 645, 30, 10))
ellipse(SnoopDogg, (153, 102, 0), (115, 625, 35, 70))
ellipse(SnoopDogg, (153, 102, 0), (40, 600, 35, 70))
ellipse(SnoopDogg, (153, 102, 0), (25, 665, 35, 15))
ellipse(SnoopDogg, (153, 102, 0), (100, 690, 35, 15))
rect(SnoopDogg, (153, 102, 0), (45, 545, 80, 80))
aalines(SnoopDogg, (0, 0, 0), True, [[45, 545], [125, 545], [125, 625], [45, 625]])
ellipse(SnoopDogg, (153, 102, 0), (30, 545, 20, 30))
arc(SnoopDogg, (0, 0, 0), (30, 545, 20, 30), pi, 2 * pi, 1)
arc(SnoopDogg, (0, 0, 0), (30, 545, 20, 30), 0, pi, 1)
ellipse(SnoopDogg, (153, 102, 0), (120, 545, 20, 30))
arc(SnoopDogg, (0, 0, 0), (120, 545, 20, 30), pi, 2 * pi, 1)
arc(SnoopDogg, (0, 0, 0), (120, 545, 20, 30), 0, pi, 1)
ellipse(SnoopDogg, (255, 255, 255), (100, 570, 20, 15))
arc(SnoopDogg, (0, 0, 0), (100, 570, 20, 15), pi, 2 * pi, 2)
arc(SnoopDogg, (0, 0, 0), (100, 570, 20, 15), 0, pi, 2)
ellipse(SnoopDogg, (255, 255, 255), (50, 570, 20, 15))
arc(SnoopDogg, (0, 0, 0), (50, 570, 20, 15), pi, 2 * pi, 2)
arc(SnoopDogg, (0, 0, 0), (50, 570, 20, 15), 0, pi, 2)
ellipse(SnoopDogg, (0, 0, 0), (55, 575, 5, 5))
ellipse(SnoopDogg, (0, 0, 0), (110, 575, 5, 5))
arc(SnoopDogg, (0, 0, 0), (65, 590, 40, 20), pi, 2 * pi, 2)
polygon(SnoopDogg, (255, 255, 255), [[70, 605], [70, 615], [75, 610]])
polygon(SnoopDogg, (255, 255, 255), [[100, 605], [100, 615], [95, 610]])
aalines(SnoopDogg, (0, 0, 0), True, [[70, 605], [70, 615], [75, 610]])
aalines(SnoopDogg, (0, 0, 0), True, [[100, 605], [100, 615], [95, 610]])

screen.blit(SnoopDogg, (0, 0, 600, 800))
dog1 = pygame.transform.flip(SnoopDogg, True, False)
screen.blit(dog1, (-300, -200, 600, 800))
dog2 = pygame.transform.scale(SnoopDogg, (300, 400))
screen.blit(dog2, (400, 100, 600, 800))
dog3 = pygame.transform.scale(SnoopDogg, (1000, 1500))
screen.blit(dog3, (400, -500, 600, 800))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

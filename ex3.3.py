import pygame
import pygame.draw as draw

pygame.init()

FPS = 30
SnoopDogg = pygame.Surface((600, 800))
SnoopDogg.set_colorkey((0, 0, 0))
screen = pygame.display.set_mode((600, 800))
pi = 3.14

draw.rect(screen, (0, 255, 255), (0, 0, 600, 400))  # небо
draw.rect(screen, (0, 128, 0), (0, 401, 600, 400))  # трава
BLACK = (0, 0, 0,)
BLACK_KOSTYL = (0, 1, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
def budka_plus_cep():
    '''
    Draw the home for dogs
    :return:
    '''
    draw.polygon(screen, (235, 191, 0),[[350, 450], [350, 650], [500, 700], [550, 650], [550, 450], [450, 300], [400, 350]])
    draw.aalines(screen, BLACK, False,[[350, 450], [350, 650], [500, 700], [550, 650], [550, 450], [450, 300], [400, 350], [500, 500],[500, 700]])
    draw.aalines(screen, BLACK, False, [[400, 350], [350, 450], [500, 500], [550, 450]])
    draw.ellipse(screen, BLACK, (375, 500, 100, 150))
    draw.arc(screen, YELLOW, (355, 610, 15, 30), 0, pi, 4)
    draw.arc(screen, YELLOW, (355, 610, 15, 30), pi, 2 * pi, 4)
    draw.arc(screen, YELLOW, (357, 630, 15, 30), 0, pi, 4)
    draw.arc(screen, YELLOW, (357, 630, 15, 30), pi, 2 * pi, 4)
    draw.arc(screen, YELLOW, (355, 650, 15, 30), 0, pi, 4)
    draw.arc(screen, YELLOW, (355, 650, 15, 30), pi, 2 * pi, 4)
    draw.arc(screen, YELLOW, (345, 665, 30, 15), 0, pi, 4)
    draw.arc(screen, YELLOW, (345, 665, 30, 15), pi, 2 * pi, 4)
    draw.arc(screen, YELLOW, (325, 663, 30, 15), 0, pi, 4)
    draw.arc(screen, YELLOW, (325, 663, 30, 15), pi, 2 * pi, 4)
    draw.arc(screen, YELLOW, (305, 665, 30, 15), 0, pi, 4)
    draw.arc(screen, YELLOW, (305, 665, 30, 15), pi, 2 * pi, 4)
    draw.arc(screen, YELLOW, (285, 663, 30, 15), 0, pi, 4)
    draw.arc(screen, YELLOW, (285, 663, 30, 15), pi, 2 * pi, 4)
    draw.arc(screen, YELLOW, (265, 665, 30, 15), 0, pi, 4)
    draw.arc(screen, YELLOW, (265, 665, 30, 15), pi, 2 * pi, 4)

def fence(x_fence, y_fence, l_fence, h_fence):
    '''
    draw the fence
    :param x_fence: x-coordinate
    :param y_fence: y-cooradinate
    :param l_fence: length of the fence
    :param h_fence: high of the fence
    :return:
    '''
    draw.rect(screen, (128, 128, 0), (x_fence, y_fence, l_fence, h_fence))  # забор (прямоугольник)

    n = 10
    color = BLACK
    draw.rect(screen, color, (x_fence, y_fence, l_fence, h_fence), 2)
    h = l_fence // (n + 1)
    x = x_fence
    for i in range(n):
        x += h
        draw.line(screen, color, (x, y_fence), (x, y_fence + h_fence))

def dog_drawing():
    '''
    this function draws a dog
    :return:
    '''
    body()
    head()
def dog(x, y, x_size, y_size, direct:bool):
    '''

    :param x: x-coordinate
    :param y: y-coordinate
    :param x_size: lenght of the dog
    :param y_size: high of the dog
    :return:
    '''
    if direct:
        dog1 = pygame.transform.scale(SnoopDogg, (x_size, y_size))
        #screen.blit(поверхность,(x, y, размеры экрана))
        screen.blit(dog1, (x, y, 600, 800))
    else:
        dog1 = pygame.transform.scale(SnoopDogg, (x_size, y_size))
        dog1 = pygame.transform.flip(SnoopDogg, True, False)
        screen.blit(dog1, (x, y, 600, 800))

def body():
    '''
    draw the body of the dog
    :return:
    '''
    draw.ellipse(SnoopDogg, (153, 102, 0), (50, 580, 120, 70))
    draw.ellipse(SnoopDogg, (153, 102, 0), (150, 590, 90, 45))
    draw.ellipse(SnoopDogg, (153, 102, 0), (200, 600, 50, 50))
    draw.ellipse(SnoopDogg, (153, 102, 0), (150, 580, 50, 50))
    draw.ellipse(SnoopDogg, (153, 102, 0), (235, 620, 20, 50))
    draw.ellipse(SnoopDogg, (153, 102, 0), (180, 600, 20, 50))
    draw.ellipse(SnoopDogg, (153, 102, 0), (220, 665, 30, 10))
    draw.ellipse(SnoopDogg, (153, 102, 0), (165, 645, 30, 10))
    draw.ellipse(SnoopDogg, (153, 102, 0), (115, 625, 35, 70))
    draw.ellipse(SnoopDogg, (153, 102, 0), (40, 600, 35, 70))
    draw.ellipse(SnoopDogg, (153, 102, 0), (25, 665, 35, 15))
    draw.ellipse(SnoopDogg, (153, 102, 0), (100, 690, 35, 15))

def head():
    '''
    draw the head of the dog
    :return:
    '''
    draw.rect(SnoopDogg, (153, 102, 0), (45, 545, 80, 80))#морда
    draw.aalines(SnoopDogg, BLACK_KOSTYL,True, [[45, 545], [125, 545], [125, 625], [45, 625]])
    draw.ellipse(SnoopDogg, (153, 102, 0), (30, 545, 20, 30))# left ear
    draw.arc(SnoopDogg, BLACK_KOSTYL, (30, 545, 20, 30), pi, 2 * pi, 1)
    draw.arc(SnoopDogg, BLACK_KOSTYL, (30, 545, 20, 30), 0, pi, 1)
    draw.ellipse(SnoopDogg, (153, 102, 0), (120, 545, 20, 30))#right ear
    draw.arc(SnoopDogg, BLACK_KOSTYL, (120, 545, 20, 30), pi, 2 * pi, 1)
    draw.arc(SnoopDogg, BLACK_KOSTYL, (120, 545, 20, 30), 0, pi, 1)
    draw.ellipse(SnoopDogg, WHITE, (100, 570, 20, 15))#right zrachok
    draw.arc(SnoopDogg, BLACK_KOSTYL, (100, 570, 20, 15), pi, 2 * pi, 2)
    draw.arc(SnoopDogg, BLACK_KOSTYL, (100, 570, 20, 15), 0, pi, 2)
    draw.ellipse(SnoopDogg, WHITE, (50, 570, 20, 15))#left zrachok
    draw.arc(SnoopDogg, BLACK_KOSTYL, (50, 570, 20, 15), pi, 2 * pi, 2)
    draw.arc(SnoopDogg, BLACK_KOSTYL, (50, 570, 20, 15), 0, pi, 2)
    draw.ellipse(SnoopDogg, BLACK_KOSTYL, (55, 575, 5, 5))#tocka right
    draw.ellipse(SnoopDogg, BLACK_KOSTYL, (110, 575, 5, 5))#tocka left
    draw.arc(SnoopDogg, BLACK_KOSTYL, (65, 590, 40, 20), pi, 2 * pi, 2)#mouth
    draw.polygon(SnoopDogg, WHITE, [[70, 605], [70, 615], [75, 610]])#left tooth
    draw.polygon(SnoopDogg, WHITE, [[100, 605], [100, 615], [95, 610]])#right tooth
    draw.aalines(SnoopDogg, BLACK_KOSTYL, True, [[70, 605], [70, 615], [75, 610]])
    draw.aalines(SnoopDogg, BLACK_KOSTYL, True, [[100, 605], [100, 615], [95, 610]])

fence(30, 40, 600, 400)
fence(0, 0, 500, 300)
fence(10, 10, 400, 400)
fence(300, 40, 300, 200)
fence(0, 0, 200, 200)
fence(10, 10, 100, 350)

budka_plus_cep()
dog_drawing()
dog(320, 280, 300, 400, True)
dog(400, -500, 1000, 1500, True)
dog(0, -100, 600, 800, True)
dog(-300, 50, 600, 800, False)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

import pygame
from pygame.draw import *
import random
from random import randint 
pygame.init()

FPS = 3
screen = pygame.display.set_mode((700, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball(x, y):
  '''
  Функция рисует цветной мяч на экране.
  Параметры:
     x (int): Абсцисса центра мяча
     y (int): Ордината центра мяча
  Возвращаемые значения:
    Pigame.Rect: Выводит мяч на экран
  '''
  color = COLORS[randint(0, 5)]
  circle(screen, color, (x, y), 30)

def new_angry(a, b, R):
  '''
  Функция рисует злой смайлик на экране.
  Параметры:
     x (int): Абсцисса центра смайлика
     y (int): Ордината центра смайлика
     R (int): Радиус смайлика 
  Возвращаемые значения:
    Pigame.Rect: Выводит смайлик на экран
  '''
  N = 150//R
  circle(screen, (225, 225, 0), (a, b), 150//N)
  circle(screen, (255, 0, 0), (a - 80//N, b - 25//N), 40//N)
  circle(screen, (255, 0, 0), (a + 80//N, b - 25//N), 40//N)
  circle(screen, (0, 0, 0), (a + 80//N, b - 25//N), 20//N)
  circle(screen, (0, 0, 0), (a - 80//N, b - 25//N), 20//N)
  rect(screen, (0, 0, 0), (a - 80//N, b + 55//N , 150//N, 30//N))
  polygon(screen, (0, 0, 0), [[a + 40//N, b - 35//N], [a + 20//N, b - 55//N], [a + 110//N, b - 95//N], [a + 100//N, b - 75//N]])
  polygon(screen, (0, 0, 0,), [[a - 40//N, b - 35//N], [a - 20//N, b - 55//N], [a - 110//N, b - 95//N], [a - 100//N, b - 75//N]])

def new_sad(a, b, R):
  '''
  Функция рисует грустный смайлик на экране.
  Параметры:
     x (int): Абсцисса центра смайлика
     y (int): Ордината центра смайлика
     R (int): Радиус смайлика 
  Возвращаемые значения:
    Pigame.Rect: Выводит смайлик на экран
  '''
  N = 150//R
  circle(screen, (225, 225, 0), (a, b), 150//N)
  circle(screen, (0, 200, 0), (a - 80//N, b - 25//N), 40//N)
  circle(screen, (0, 200, 0), (a + 80//N, b - 25//N), 40//N)
  circle(screen, (0, 0, 0), (a + 80//N, b - 25//N), 20//N)
  circle(screen, (0, 0, 0), (a - 80//N, b - 25//N), 20//N)
  rect(screen, (0, 0, 0), (a - 80//N, b + 55//N, 150//N, 30//N))
  polygon(screen, (0, 0, 0,), [[a - 110//N, b - 35//N], [a - 130//N, b - 55//N], [a - 40//N, b - 95//N], [a - 50//N, b - 75//N]])
  polygon(screen, (0, 0, 0,), [[a + 110//N, b - 35//N], [a + 130//N, b - 55//N], [a + 40//N, b - 95//N], [a + 50//N, b - 75//N]])

def ball_move(x, determination):
  '''
  Функция управляет движением мячика.
  Параметры:
     x (int): координата центра мяча
     determination {1, 2}: параметр отвечающий за движение мяча 1 - увеличение координаты, 2 - уменьшение
  Возвращаемые значения:
    list: Список из двух элементов: новой координаты и нового направления
  '''
  if x < 560:
    if determination == 1:
      x = x + randint(1, 30)
    else:
      if x > 30:
        x = x - randint(1, 30)
      else:
        determination = 1
        x = x + 31
  else:
    determination = 2
    x = x - 31
  return list([x, determination])
  
def move(a):
  '''
  Функция управляет движением смайликов.
  Параметры:
     a (int): координата центра смайлика
  Возвращаемые значения:
     a (int): новая координата центра смайлика
  '''
  if a < 500 and a > 100: 
    a = a + int(random.uniform(100, -100))
  else:
    a = randint(50, 500)
  return a


print('Game rules:')
print('Your main aim is to click to a sad green smile by left mousebutton. If it is suceccessful you get + 10 scores')
print('However you should not click to the angre smile (big and little), else you would get -1 life. At the beginning you have 10 lives so if it turns 0 you lose.')
print('If you have 100 points you should click by right mousebutton. When you do it you scores turns 0 and a new small angre smile appear. Do not click on it!')
print('You have also another opportunity to get points. There is also a colourful ball on the screen. So if you click right mousebutton on the moment the main (big) angry smile is situated on the ball, it would be a strike and you get +30 scores!')
print('You win if there are 3 small angre smiles on the screen and you have 100 scores')


a0 = randint(15, 585)
b0 = randint(15, 585)
R = randint(30,50)
x = randint(15, 585)
y = randint(15, 585)
r = randint(30,50)
c = randint(15, 585)
d = randint(15, 585)
x_determination = 1
y_determination = 1
t = 1
lives = 10
a = []
b = []
for i in range(1,21):
  a.append(randint(15, 585))
  b.append(randint(15, 585))
scores = 0
new_angry(a0, b0, R)
new_sad(c, d, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        finished = True
      elif event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        x_mouse = pos[0]
        y_mouse = pos[1]
        if ((a0 - x_mouse)**2 + (b0 - y_mouse)**2) < R**2:
          lives = lives - 1
        if t >= 2:
          for i in range(1, t):
            if ((a[i] - x_mouse)**2 + (b[i] - y_mouse)**2) < 400:
              lives = lives - 1
              print('scores = ', scores)
              print('lives = ', lives)
        if ((c - x_mouse)**2 + (d - y_mouse)**2) < r**2:
          scores = scores + 10
          print('scores = ', scores)
          print('lives = ', lives)
        if (((a0 - x)**2 + (b0 - y)**2) < (R +30)**2) and (event.button == 3):
          scores = scores + 30
          print('Strike!!!')
          print('scores = ', scores)
          print('lives = ', lives)
        if (scores >= 100) and (event.button == 3):
          t = t + 1;
          scores = 0;
        if lives <= 0:
          f1 = open('You have lost.txt', 'w')
          f1.write('You have lost.Better luck next time.\n')
          f1.write('your lives = 0!!!\n')
        if t >= 6:
          f1 = open('Congratulations.txt', 'w')
          f1.write('Congratulations!!!\n')
          f1.write('You get more than 100 points!!!\n')
          f1.write('You are the winner!!!')
    rect(screen, (102, 0, 102), (0, 0, 600, 600), 20)
    f = ball_move(x, x_determination)
    x = f[0]
    x_determination = f[1]
    g = ball_move(y, y_determination)
    y = g[0]
    y_determination = g[1]
    new_ball(x, y)
    a0 = move(a0)
    b0 = move(b0)
    R = randint(30,50)
    new_angry(a0, b0, R)
    c =move(c)
    d = move(d)
    for i in range(1, t):
      a[i] = move(a[i])
      b[i] = move(b[i])
      new_angry(a[i], b[i], 20)
    r = randint(30,50)
    new_sad(c, d, r)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
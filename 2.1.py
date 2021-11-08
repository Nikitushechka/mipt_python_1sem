import math
from random import choice
from random import randint as rnd
import pygame


FPS = 30

MAX_TIME = 100
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, go1):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = go1.x
        self.y = go1.y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.time = 0
        self.g = 0

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.x += self.vx
        self.y -= self.vy-self.g
        self.g += 2
        if self.x+self.r >= WIDTH:
            self.vx = -0.5*self.vx
            self.x = WIDTH - self.r
        if self.y+self.r >= HEIGHT:
            self.y = HEIGHT - self.r
            self.vy = -0.8*self.vy
            self.g = 0

    def draw(self):
        if self.time < 100:
            pygame.draw.circle(
                self.screen,
                self.color,
                (self.x, self.y),
                self.r
            )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """

        if (obj.x - self.x)**2 + (obj.y-self.y)**2 <= (self.r+obj.r)**2:
            return True
        else:
            return False

    def tic(self):
        self.time+=1

class Rect:
    def __init__(self, screen: pygame.Surface, go2):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = go2.x
        self.y = go2.y
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.time = 0
        self.g = 0
        self.width = 3
        self.length = 3
        self.bn = 1

    def move(self):
        self.x += self.vx
        self.y -= self.vy-self.g
        self.g += 2

    def draw(self):
        if self.time < 100:
            pygame.draw.polygon(self.screen, self.color,
                [(self.x - self.width // 2 * math.sin(-self.bn), self.y - self.width // 2 * math.cos(-self.bn)),
                 (self.x + self.length * math.cos(-self.bn) - self.width // 2 * math.sin(-self.bn),
                  self.y - self.length * math.sin(-self.bn) - self.width // 2 * math.cos(-self.bn)),
                 (self.x + self.length * math.cos(-self.bn) + self.width // 2 * math.sin(-self.bn),
                  self.y - self.length * math.sin(-self.bn) + self.width // 2 * math.cos(-self.bn)),
                 (self.x + self.width // 2 * math.sin(-self.bn), self.y + self.width // 2 * math.cos(-self.bn))]
            )

    def hittest(self, obj):
        if math.fabs(self.y-obj.y) <= self.length/2 + obj.r and math.fabs(obj.x - self.x) <= self.length/2 + obj.r:
            return True
        else:
            return False

    def tic(self):
        self.time += 1

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450
        self.width = 7
        self.length = 35
        self.h = 0

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end1(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen, gun)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10
    def fire2_end2(self, event):
        global bullet, rects
        bullet += 1
        new_rect = Rect(self.screen, gun)
        new_rect.length += 5
        new_rect.width += 2
        self.an = self.an
        new_rect.vx = self.f2_power * math.cos(self.an)*2
        new_rect.vy = - self.f2_power * math.sin(self.an)*2
        rects.append(new_rect)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] - self.x != 0:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
            if event.pos[0] - self.x > 0:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x + 0.0000000001))
            else:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x + 0.0000000001))+math.pi
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.polygon(
            self.screen,
            self.color,
            [(self.x - self.width // 2 * math.sin(-self.an), self.y - self.width // 2 * math.cos(-self.an)),
             (self.x + self.length * math.cos(-self.an) - self.width // 2 * math.sin(-self.an),
              self.y - self.length * math.sin(-self.an) - self.width // 2 * math.cos(-self.an)),
             (self.x + self.length * math.cos(-self.an) + self.width // 2 * math.sin(-self.an),
              self.y - self.length * math.sin(-self.an) + self.width // 2 * math.cos(-self.an)),
             (self.x + self.width // 2 * math.sin(-self.an), self.y + self.width // 2 * math.cos(-self.an))]
        )
    def move_right(self):
        if self.x <= 760:
            self.x += 30
        else:
            self.x += 0
    def move_left(self):
        if self.x >= 40:
            self.x -= 30
        else:
            self.x += 0
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 70:
                self.f2_power += 1
                self.length += 1.5
            self.color = RED
        else:
            self.color = GREY
            self.length = 35


class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self, screen: pygame.Surface):
        self.points = 0
        self.new_target()
        self.screen = screen
        self.live = 1
        self.vx = rnd(-20, -5)
        self.vy = rnd(5, 20)

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 750)
        self.y = rnd(100, 550)
        self.r = rnd(2, 50)
        self.color = RED
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.x - self.r <= 0:
            self.vx = -self.vx
        if self.x + self.r >= WIDTH:
            self.vx = -self.vx
        if self.y + self.r >= HEIGHT:
            self.vy = -self.vy
        if self.y - self.r <= 0:
            self.vy = -self.vy

def print_text(message, x, y, font_color=(0, 0, 0), font_type='21028.ttf', font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))


pygame.display.set_caption('Пушка')
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
rects = []
scores = 0


clock = pygame.time.Clock()
gun = Gun(screen)
target = [Target(screen), Target(screen), Target(screen)]
finished = False
time = MAX_TIME

while not finished:
    screen.fill(WHITE)
    gun.draw()
    if time == MAX_TIME:
        for t in target:
            t.draw()
    for b in balls:
        b.draw()
        b.tic()
    for r in rects:
        r.draw()
        r.tic()
    print_text('' + str(scores), 10, 10)
    if time == MAX_TIME:
        bullet_1 = bullet
    if time < MAX_TIME:
        print_text('Вы уничтожили цель за ' + str(bullet_1) + 'выстрелов', 230, 250)
        bullet = 0
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and event. button == 1:
            gun.fire2_end1(event)
        elif event.type == pygame.MOUSEBUTTONUP and event. button == 3:
            gun.fire2_end2(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                gun.move_right()
            if event.key == pygame.K_LEFT:
                gun.move_left()
    for t in target:
        t.move()
    for r in rects:
        r.move()
        for t in target:
            if r.hittest(t) and t.live:
                time = 0
                t.live = 0
                t.hit()
                scores += 1
                t.new_target()
    for b in balls:
        b.move()
        for t in target:
            if b.hittest(t) and t.live:
                time = 0
                t.live = 0
                t.hit()
                scores += 1
                t.new_target()
    gun.power_up()
    if time < MAX_TIME:
        time += 1

pygame.quit()

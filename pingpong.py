#Создай собственный Шутер!
from pygame import *
import player
from constants import  *
from enemy import Enemy
from random import randint, random
import gamesprite
from time import time as timer

font.init()


window = display.set_mode((WIDTH,HEIGHT))
display.set_caption('Ping Pong')
player_l = player.Player('platform.png', 0, HEIGHT//2, 5, WIDTH_PLATFORM, 65)
player_r = player.Player('platform.png', WIDTH-WIDTH_PLATFORM, HEIGHT//2, 5, WIDTH_PLATFORM, 65)
ball = Enemy('ball.png', WIDTH//2, HEIGHT//2, 3, 20, 20, 3)

font_style = font.SysFont('Arial', 14)
font_style2 = font.SysFont('Times New Roman', 70)

clock = time.Clock()
game = True
finish = False
while game:
    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
    window.fill(WHITE)
    if not finish:
        player_l.update_l()
        player_r.update_r()
        player_l.reset(window)
        player_r.reset(window)
        ball.update()
        ball.reset(window)
        if sprite.collide_rect(player_l, ball):
            ball.speed_x *= -1
        if sprite.collide_rect(player_r, ball):
            ball.speed_x *= -1
        if 
    display.update()
    clock.tick(FPS)

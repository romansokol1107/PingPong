from random import randint
import pygame
from constants import *
import gamesprite


class Enemy(gamesprite.GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height, player_lost):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.lost = player_lost
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= HEIGHT:
            self.lost += 1
            self.rect.y = 0
            self.rect.x = randint(0, WIDTH - self.width)
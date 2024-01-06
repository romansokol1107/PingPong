from random import randint
import pygame
from constants import *
import gamesprite


class Enemy(gamesprite.GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height, player_speed_x):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.speed_x = player_speed_x
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed_x
        if self.rect.bottom >= HEIGHT or self.rect.y <= 0:
            self.speed *= -1
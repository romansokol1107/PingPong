from pygame import *
import gamesprite
from constants import *

class Player(gamesprite.GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y-self.speed >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.bottom+self.speed <= HEIGHT:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y-self.speed >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.bottom+self.speed <= HEIGHT:
            self.rect.y += self.speed

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,setting,screen):
        super().__init__()
        self.setting=setting
        self.screen=screen
        self.image=pygame.image.load("images/alien.bmp")
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height


    def update(self):

        self.rect.x+=self.setting.alien_speed_factor*self.setting.alien_moving_direction
        # print(self.setting.alien_moving_direction)


    def check_edges(self):
        if self.rect.right >= self.screen.get_rect().right:
            return True
        elif self.rect.left <= self.screen.get_rect().left:
            return True


    def blitme(self):
        self.screen.blit(self.image,self.rect)



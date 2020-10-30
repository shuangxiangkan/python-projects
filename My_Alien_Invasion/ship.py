import pygame


class Ship():

    def __init__(self, screen, setting):
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.setting = setting
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Set the location of ship
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # set the moving direction
        self.moving_right = False
        self.moving_left = False




    def update(self):
        # update the position of ship
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx += self.setting.ship_move_distance
        elif self.moving_left and self.rect.left >= self.screen_rect.left:
            self.rect.centerx -= self.setting.ship_move_distance


    def blitme(self):
        # draw the ship on the screen
        self.screen.blit(self.image,self.rect)

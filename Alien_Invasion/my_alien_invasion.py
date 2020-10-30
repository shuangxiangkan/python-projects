import sys
import pygame
import my_game_functions as mgf
from my_ship import my_Ship
from my_setting import Setting
from pygame.sprite import Group
from my_alien import Alien


def run_game():

    pygame.init()
    setting=Setting()
    screen=pygame.display.set_mode((setting.screen_width,setting.screen_height))
    pygame.display.set_caption("my_alien_invision")
    ship=my_Ship(screen)
    bullets=Group()
    aliens=Group()

    # Create the fleet of aliens
    mgf.create_fleet(setting,screen,ship,aliens)

    while True:
        mgf.check_events(ship,setting,screen,bullets)
        ship.update()
        mgf.update_bullets(aliens,bullets)
        mgf.update_aliens(setting,aliens)
        mgf.update_screen(screen,setting,ship,aliens,bullets)

run_game()
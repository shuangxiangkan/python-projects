import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from gamestats import GameStats
from alien import  Alien

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    setting = Settings()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_heigh))
    pygame.display.set_caption("My_Alien_Invasion")

    # Create a ship object
    ship = Ship(screen, setting)
    # Create a group object to store bullets
    bullets = Group()
    # Create a group object to store aliens
    aliens = Group()
    # Create a gamestats object
    gs=GameStats()

    # Create a alien fleet
    gf.create_fleet(setting,screen, aliens)

    while True:
        gf.check_events(setting, screen, ship, bullets)
        if not gs.Is_End:
            ship.update()
            bullets.update()
            gf.check_fleet_edges(setting, aliens)
            aliens.update()
            gf.update_bullets(setting,screen, bullets,aliens,gs)
            gf.judge_end(ship, aliens, screen, gs)
            gf.check_aliens_bottom(screen, aliens, gs)
        gf.update_screen(screen, setting, ship,bullets,aliens)



run_game()

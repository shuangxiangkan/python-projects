import sys

import  pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    # screen.set_caption("Alien Invasion")
    pygame.display.set_caption("Alien Invasion")
    # Set the background color
    # bg_color=(230,230,230)
    # Make a group to store bullets in

    # Make the Play button
    play_button=Button(ai_settings,screen,"Play")



    # Make a ship,a group of bullets, and a group of aliens
    ship=Ship(ai_settings,screen)
    # alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()


    # Create the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    # Create an instance to store game statistic and create a scoreboard.
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        # for event in pygame.event.get():
        #     if event.type==pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()

            # Redraw the screen during each pass through the loop
            # screen.fill(ai_settings.bg_color)
            # ship.blitme()

            # Get rid of bullets that have disappeared
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)


run_game()
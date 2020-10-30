import sys
import pygame
from my_bullet import My_bullet
from my_alien import Alien


def check_events(ship,setting,screen,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,setting,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def check_keydown_events(event,ship,setting,screen,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key==pygame.K_SPACE:
        if len(bullets)<setting.bullets_allowed:
            bullet=My_bullet(setting,ship,screen)
            bullets.add(bullet)
        # print(len(bullets))


def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(screen,setting,ship,aliens,bullets):
    screen.fill(setting.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip()

def update_bullets(aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for my bullets that have hit aliens
    # If so,get rid of the bullets and the alien
    collisons=pygame.sprite.groupcollide(bullets,aliens,True,True)

def create_fleet(ai_settings,screen,ship,aliens):
    # Create a full fleet of aliens
    # Create an alien and find the number of aliens in a row
    # Spacing bewteen each alien is equal to one alien width
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    number_aliens_x=get_number_aliens_x(ai_settings,alien_width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    # Create the first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_aliens_x(ai_settings,alien_width):
    # Determine the number of aliens that fit in a row
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    # Create an alien and place it in the row
    alien = Alien(ai_settings, screen)
    alien_width=alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    # Determine the number of rows of aliens that fit on the screen
    available_space_y=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space_y/(2*alien_height))
    return number_rows



def check_fleet_edges(ai_settings,aliens):
    # Respond appropriately if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    # Drop the entire fleet and change the fleet's direction
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1

def update_aliens(ai_settings,aliens):
    # Check if the fleet is at an edge and then update the positions of all aliens in the fleet
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

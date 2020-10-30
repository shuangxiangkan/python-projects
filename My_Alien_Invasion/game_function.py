import sys
import pygame
from bullet import Bullet
from  alien import Alien




def check_events(setting,screen,ship,bullets):
    # Wathch for keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key==pygame.K_SPACE:
                bullet=Bullet(setting,screen,ship)
                bullets.add(bullet)
        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right=False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_bullets(setting,screen,bullets,aliens,gs):
    # Delete the bullet from bullets which has been out of scope
    for bullet in bullets.copy():
        if bullet.rect.bottom<=screen.get_rect().top:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens
    # If so,get rid of the bullet and the alien
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)

    # for alien in collisions.values():
    #     print(10*len(alien))

    if len(aliens)==0 and setting.ships_limit>1 and not gs.Is_End:
        create_fleet(setting,screen,aliens)
        setting.ships_limit-=1



def create_fleet(setting,screen,aliens):
    alien=Alien(setting,screen)
    alien_x_numbers=int((screen.get_rect().width-2*alien.rect.width)/(2*alien.rect.width))
    alien_y_numbers=int((screen.get_rect().height-3*alien.rect.height)/(2*alien.rect.height))
    for x_number in range(alien_x_numbers):
        for y_number in range(alien_y_numbers):
            print()
            alien = Alien(setting,screen)
            alien.rect.x=alien.rect.width+x_number*2*alien.rect.width
            alien.rect.y=10+2*y_number*alien.rect.height
            aliens.add(alien)


def change_fleet_direction(setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=setting.alien_moving_down_distance

    # Change the direction of alien
    setting.alien_moving_direction*=-1


def check_fleet_edges(setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(setting,aliens)
            break

def judge_end(ship,aliens,screen,gs):
    if pygame.sprite.spritecollideany(ship,aliens):
        gs.Is_End=True


def check_aliens_bottom(screen,aliens,gs):
    for alien in aliens.sprites():
        if alien.rect.bottom>screen.get_rect().bottom:
            gs.Is_End=True





def update_screen(screen,setting,ship,bullets,aliens):
    # Set the background color
    screen.fill(setting.bg_color)
    ship.blitme()


    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien in aliens.sprites():
        alien.blitme()
    # Make the most recenty drawn screen visible
    pygame.display.flip()
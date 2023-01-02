import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, gun, bullets):
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # right
            if event.key == pygame.K_d:
                gun.mright = True
            # left
            elif event.key == pygame.K_a:
                gun.mleft = True
            # SPACE
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # right
            if event.key == pygame.K_d:
                gun.mright = False
            # left
            elif event.key == pygame.K_a:
                gun.mleft = False

def update(bg_color, screen, stats, sc, gun, inos, bullets):
    # update screen
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    # update position bullets
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        cheсk_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def gun_kill(stats, screen, sc, gun, inos, bullets):
    # clash of cannon with army
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, sc, gun, inos, bullets):
    # updates the position aliens
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_chek(stats, screen, sc, gun, inos, bullets)

def inos_chek(stats, screen, sc, gun, inos, bullets):
    # cheking if blood has reached the screen
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, inos, bullets)
            break

def create_army(screen, inos):
    # army aliens
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((640 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((640 - 64 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)

def cheсk_high_score(stats, sc):
    # cheking new records
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        # create bullet in position gun
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 6, 12)
        self.color = 139, 195, 74
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # moving bullet up
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # painting bullet on screen
        pygame.draw.rect(self.screen, self.color, self.rect)

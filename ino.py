import pygame

class Ino(pygame.sprite.Sprite):
    # class one ufo

    def __init__(self, screen):
        # initialize and set initial position
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/pixel1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        # displaying an alien
        self.screen.blit(self.image, self.rect)

    def update(self):
        # moves aliens
        self.y += 0.1
        self.rect.y = self.y


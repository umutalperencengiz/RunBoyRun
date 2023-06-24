import pygame
class fire(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("20290321_others/PNG/Mage/Fire_extra/fire_extra1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.rect.inflate_ip(-110, -120)
        self.speed = 6
    def update(self):
        self.rect.x += self.speed

import pygame
class walking() :
    def __init__(self):
        super().__init__()

        self.walkImages = []
        for j in range(1, 7):
            walkImage = pygame.image.load(f"20290321_others/PNG/Mage/Walk/walk{j}.png").convert_alpha()
            self.walkImages.append(walkImage)
        # walking animation
        self.walkImages_index = 0
        self.walkImage = self.walkImages[self.walkImages_index]
        self.is_walk = False
        self.rect = self.walkImage.get_rect()
        self.rect.center = (50, 70)

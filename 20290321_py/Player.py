import pygame
import Fire
class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []

        for i in range(1,14):
            image = pygame.image.load(f"20290321_others/PNG/Mage/Idle/idle{i}.png").convert_alpha()
            self.images.append(image)


        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.center = (50,70)
        #inflate image for interaction
        self.rect.inflate_ip(-100,-100)
        self.animation_timer = pygame.time.get_ticks()
        self.timer = pygame.time.get_ticks()
        self.delay = 700
        self.animation_delay = 200
        #speed
        self.speed = 4
        #fire



    def update(self, keys,screen,walking,player_group,fire_group):
        current_time = pygame.time.get_ticks()




        # Handle movement

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            walking.is_walk = True
            screen.blit(walking.walkImages[1], (self.rect.x, self.rect.y))
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            walking.is_walk = True
            screen.blit(walking.walkImages[2], (self.rect.x, self.rect.y))
            self.rect.x += self.speed

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            walking.is_walk = True
            screen.blit(walking.walkImages[4], (self.rect.x, self.rect.y))
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            walking.is_walk = True
            screen.blit(walking.walkImages[5], (self.rect.x, self.rect.y))
            self.rect.y += self.speed

        if keys[pygame.K_SPACE] and  current_time - self.timer > self.delay :
            self.fire = Fire.fire(self.rect.x+30, self.rect.y-10)
            fire_group.add(self.fire)
            self.timer = current_time
        # Constrain the player to the screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > 900:
            self.rect.right = 900
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.bottom > 650:
            self.rect.bottom = 650
        if self.rect.top <200:
            self.rect.top = 200

        #animations

            # Switch to the next image in the sequence

        if current_time - self.animation_timer > self.animation_delay and walking.is_walk == False:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.animation_timer = current_time

        walking.is_walk = False
    def reset(self):
        super().__init__()
        player()
        self.rect.center = (50,70)







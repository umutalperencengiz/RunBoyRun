import pygame
import random
class obstacles(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("20290321_others/PNG/Knight/Idle/idle7.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.inflate_ip(-57,-57)


    def generate_obstacles(obstacle_group,score):
        if(score<1000):
            num_obstacles = random.randint(4, 10)
        elif(score<2000):
            num_obstacles = random.randint(8,16)
        elif(score >=2000):
            num_obstacles = random.randint(10,20)

        # Generate each obstacle
        for i in range(num_obstacles):
            x = random.randint(300, 800)
            y = random.randint(200, 600)
            obstacle = obstacles(x, y)
            obstacle_group.add(obstacle)



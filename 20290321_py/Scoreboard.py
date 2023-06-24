import pygame


class scoreboard():
    def __init__(self,screen):
        self.font = pygame.font.Font("20290321_others/PNG/Game Over.otf", 40)
        self.score = 0
        self.scoreboard_screen_text = self.font.render(str(self.score),True,(255,255,255))
        self.timer = pygame.time.get_ticks()
        self.scoreTimer = pygame.time.get_ticks()
        self.delay = 1000

    def update(self,game_over):

        current_time = pygame.time.get_ticks()
        if(current_time - self.timer > self.delay) and game_over == False :
            self.score += 10
            self.timer = current_time
        self.scoreboard_screen_text = self.font.render(str(self.score), True, (255, 255, 255))
        if game_over :
            self.scoreTimer = pygame.time.get_ticks()
    def reset(self):
        self.score = 0


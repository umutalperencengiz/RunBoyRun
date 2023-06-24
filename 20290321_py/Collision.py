import pygame
class collision():
    def __init__(self,width,height,score):
        super().__init__()
        self.score = score
        self.font = pygame.font.Font("20290321_others/PNG/Game Over.otf",100)
        self.width = width
        self.height = height
        self.game_over_screen = pygame.surface.Surface((width,height))
        self.game_over_screen.fill((0, 0, 0))
        self.game_over_text = self.font.render("Game Over", True, (255, 255, 255))
        self.game_over_screen.blit(self.game_over_text, (250,100))
        self.restart_button = pygame.Rect(20,300,280,100)
        self.quit_button = pygame.Rect(600,300,200 ,100)
        pygame.draw.rect(self.game_over_screen, (255, 0, 0), self.restart_button)
        pygame.draw.rect(self.game_over_screen, (0, 255, 0), self.quit_button)
        self.restart_text = self.font.render("Restart", True, (255, 255, 255))
        self.quit_text = self.font.render("Quit", True, (255, 255, 255))
        self.game_over_screen.blit(self.restart_text,(20,200))
        self.game_over_screen.blit(self.quit_text,(600,200))
        #score

        self.score_text = self.font.render("SCORE:" + str(self.score), True, (255, 255, 255))
        self.game_over_screen.blit(self.score_text, (250, 500))
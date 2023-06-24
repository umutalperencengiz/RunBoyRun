
import pygame

import Obstacles
import Player
import Walking
import Collision
import Scoreboard


def main():
    # Initialize Pygame
    pygame.init()
    #add music
    pygame.mixer.music.load("20290321_others/Woodkid - Run Boy Run (Official HD Video).mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    def restart_music():
        pygame.mixer.music.rewind()
        pygame.mixer.music.play(-1)

        # Set the width and height of the screen
    screen_width = 900
    screen_height = 800

    screen = pygame.display.set_mode((screen_width, screen_height))
    #add background image

    bg = pygame.image.load("20290321_others/PNG/game_background_2/game_background_2.png").convert()

    bg = pygame.transform.scale(bg, (screen_width,screen_height))

    bg_speed =3
    bg_position = [0,0]
    #add player
    player = Player.player()
    player_group = pygame.sprite.Group()
    player_group.add(player)
    #add obstacles
    obstacle_group = pygame.sprite.Group()
    #add fire
    fire_group = pygame.sprite.Group()

    # Generate obstacles every 2 seconds
    ADD_OBSTACLE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ADD_OBSTACLE_EVENT, 100)


    #walking
    walking = Walking.walking()
    #game over screen
    game_over = False
    #scoreboard
    score = Scoreboard.scoreboard(screen)

    # Set the title of the game window
    pygame.display.set_caption("NO ESCAPE")
    running = True
    clock = pygame.time.Clock()
    while running :
        keys = pygame.key.get_pressed()
        #background adjusting

        bg_position[0] -= bg_speed
        if bg_position[0] < -bg.get_width():
            bg_position[0] = 0

        screen.blit(bg, (bg_position[0], 0))
        screen.blit(bg, (bg_position[0] + bg.get_width(), 0))
        screen.blit(score.scoreboard_screen_text,(0,0))
        score.update(game_over)
        #player adding to game and updating

        player_group.draw(screen)
        player_group.update(keys, screen, walking, player_group, fire_group)
        fire_group.draw(screen)
        fire_group.update()
        #add obstacles
        for event in pygame.event.get():
            if event.type == ADD_OBSTACLE_EVENT:
                Obstacles.obstacles.generate_obstacles(obstacle_group,score.score)
        obstacle_group.draw(screen)
        # update and draw obstacles
        for obstacle in obstacle_group:
            obstacle.rect.x -= bg_speed  # move obstacle towards player

            if obstacle.rect.right < 0:  # remove obstacle if it goes off-screen
                obstacle.kill()
        for fire in fire_group:
            if fire.rect.x > screen_width:
                fire.kill()
        #player obstacle interaction
        collisions1 = pygame.sprite.spritecollide(player, obstacle_group, False)

        if collisions1:
            # Handle collision
            game_over = True

        if game_over:
            screen.blit(Collision.collision(screen_width,screen_height,score.score).game_over_screen, (0,0))
            restart_music()

        # fire obstacle interaction
        collisions2 = pygame.sprite.groupcollide(fire_group,obstacle_group,False,False)
        if collisions2:
            collisions2_group = pygame.sprite.Group()
            collisions2_group.add(collisions2.values())
            if(game_over != True):
                score.score +=20
            for obstacle in collisions2_group:
                obstacle.kill()

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    if Collision.collision(screen_width,screen_height,score.score).restart_button.collidepoint(pygame.mouse.get_pos()):
                        # Restart the game
                        score.reset()
                        player.reset()
                        obstacle_group.empty()
                        game_over = False
                    elif Collision.collision(screen_width,screen_height,score.score).quit_button.collidepoint(pygame.mouse.get_pos()):
                        running = False

        pygame.display.update()



    pygame.quit()


main()

















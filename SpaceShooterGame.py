import pygame
import random
import time
from pygame.locals import *
from SpaceGameVariabies import *
from UserSpaceShip import *
from Levels import *

pygame.font.init()


def player_controls():
    global enemies
    global Guns_movement
    movement = 5
    controls = pygame.key.get_pressed()
    if controls[pygame.K_LEFT] and player.x - movement > 0 or controls[pygame.K_a] and player.x - movement > 0: 
        player.x -= movement # left and blocks me from going off the screen
    if controls[pygame.K_RIGHT] and player.x + movement + player.get_width() < WIDTH or controls[pygame.K_d] and player.x + movement + player.get_width() < WIDTH:
        player.x += movement # right and and blocks me from going off the screen
    if controls[pygame.K_UP] and player.y - movement > 0 or controls[pygame.K_w] and player.y - movement > 0:
        player.y -= movement # up and and blocks me from going off the screen
    if controls[pygame.K_DOWN] and player.y + movement + player.get_height() + 20 < HEIGHT or controls[pygame.K_s] and player.y + movement + player.get_height() + 20 < HEIGHT :
        player.y += movement # down and and blocks me from going off the screen
    if controls[pygame.K_SPACE]:
        player.shoot()

    player.move_lasers(-Guns_movement, enemies)

def StartGame():
    global enemies
    game_over = False
    lives = 3
    start_game = True
    lost_count = 0
    FPS = 60
    level = 0

    Clock = pygame.time.Clock()
    def redraw_window():
        font = pygame.font.SysFont("comicsans", 50)
        game_over_font = pygame.font.SysFont("Comicsans", 60)

        SCREEN.blit(BG, (0, 0))

        lives_label = font.render(f"Lives: {lives}", 1, (WHITE))
        level_label = font.render(f"Level: {level}", 1, (WHITE))

        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(SCREEN)

        for enemy in enemies:
            enemy.draw(SCREEN)

        if game_over == True:
            game_over_text = game_over_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(game_over_text, (WIDTH / 2 - level_label.get_width() / 2, 350))

        pygame.display.update()
    
    while start_game == True:
        Clock.tick(FPS)
        redraw_window()

        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                start_game = False
            
        player_controls()
        if lives <= 0 or player.health <= 0:
            game_over = True
            lost_count += 1
    
        if game_over == True:
            if lost_count > FPS * 3:
                start_game = False
            else:
                continue
        pygame.display.update()

        if len(enemies) == 0:
            level += 1
        if level == 1:
            level1(level)
        if level == 2:
            level2(level)
        if level == 3:
            level3(level)
        if level == 4:
            level4(level)
        if level == 5:
            level5(level)
    

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run_menu = True
    while run_menu == True:
        SCREEN.blit(BG, (0, 0))
        title_text = title_font.render("Press the mouse to begin... ", 1, (255, 255, 255))
        SCREEN.blit(title_text, (WIDTH / 2 - title_text.get_width()/2, 350))
        pygame.display.update()
        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                run_menu = False
            if window.type == pygame.MOUSEBUTTONDOWN:
                StartGame()
    pygame.quit()




main_menu()
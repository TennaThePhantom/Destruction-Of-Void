from os import remove
import pygame
import random
import time
from pygame.locals import *
from SpaceGameVariabies import *
from Levels import *

pygame.font.init()

def gamelevels(level):

    level1(level)

    level2(level)

    level3(level)

    level4(level)

    level5(level)

    level6(level)

    level7(level)

    level8(level)

    level9(level)

    level10(level)

    level11(level)

    level12(level)

    level13(level)

    level14(level)

    level15(level)

    level16(level)

    level17(level)

    level18(level)

    level19(level)

    level20(level)

    level21(level)

    level22(level)

    level23(level)

    level24(level)

    level25(level)

    level26(level)

    level27(level)

    level28(level)

    level29(level)

    level30(level)





def player_controls():
    global enemies
    global Guns_movement
    global movement
    controls = pygame.key.get_pressed()
    if controls[pygame.K_LEFT] and player.x - movement > 0 or controls[pygame.K_a] and player.x - movement > 0: 
        player.x -= movement # left and blocks me from going off the screen
    if controls[pygame.K_RIGHT] and player.x + movement + player.get_width() < WIDTH or controls[pygame.K_d] and player.x + movement + player.get_width() < WIDTH:
        player.x += movement # right and and blocks me from going off the screen
    if controls[pygame.K_UP] and player.y - movement > 0 or controls[pygame.K_w] and player.y - movement > 0:
        player.y -= movement # up and and blocks me from going off the screen
    if controls[pygame.K_DOWN] and player.y + movement + player.get_height() + 35 < HEIGHT or controls[pygame.K_s] and player.y + movement + player.get_height() + 35 < HEIGHT :
        player.y += movement # down and and blocks me from going off the screen
    if controls[pygame.K_SPACE]:
        player.shoot() 

    player.move_lasers(-Guns_movement, enemies)

def StartGame():
    global enemies
    game_over = False
    start_game = True
    lost_count = 0
    FPS = 60
    level = 0

    Clock = pygame.time.Clock()


    def redraw_window():
        SCREEN.blit(BG, (0, 0))

        font = pygame.font.SysFont("comicsans", 50)
        game_over_font = pygame.font.SysFont("Comicsans", 60)


        level_label = font.render(f"Level: {level}", 1, (WHITE))

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

        if player.health <= 0:
            game_over = True
            lost_count += 1

        if game_over == True:
            if lost_count > FPS * 3:
                start_game = False
            else:
                continue
            
        player_controls()
    
        if len(enemies) == 0:
            level += 1
        if level == 5:
            player.health = 600
            

        if level == 0:
            for enemy in enemies:
                enemies.remove(enemy)
            for lasers in player.lasers:
                player.lasers.remove(lasers)
        gamelevels(level)

        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                start_game = False
                level = 0
    





def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    goal_font =  pygame.font.SysFont("comicsans", 50)
    waves_harder_font = pygame.font.SysFont("comicsans", 50)
    ship_upgrades_font = pygame.font.SysFont("comicsans", 50)
    run_menu = True
    while run_menu == True:
        SCREEN.blit(BG, (0, 0))
        goal_text = goal_font.render("Your goal is to get to wave 30 without dieing", 1, WHITE)
        SCREEN.blit(goal_text, (WIDTH / 2 - goal_text.get_width()/2, 50))

        waves_text = waves_harder_font.render("as waves go up it will get harder", 1, WHITE)
        SCREEN.blit(waves_text, (WIDTH / 2 - waves_text.get_width()/2, 150))

        upgrades_text = ship_upgrades_font.render("Your ship will get upgrades as you play", 1, WHITE)
        SCREEN.blit(upgrades_text, (WIDTH / 2 - upgrades_text.get_width()/2, 259))

        title_text = title_font.render("Press the mouse to begin... ", 1, WHITE)
        SCREEN.blit(title_text, (WIDTH / 2 - title_text.get_width()/2, 350))


        pygame.display.update()
        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                run_menu = False
            if window.type == pygame.MOUSEBUTTONDOWN:
                StartGame()
    pygame.quit()



main_menu()

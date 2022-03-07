import pygame
import random
import time
import sys
import os
from pygame.locals import *
from Ships_Guns import *
from SpaceGameVariabies import *
from Levels import *




def player_controls():
    global player
    global Guns_movement
    global enemies
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

def StartGame():
    global player
    global lives
    global level
    global FPS
    global enemies
    Start = True

    font = pygame.font.SysFont("comicsans", 50)
    game_over_font = pygame.font.SysFont("Comicsans", 60)
    
    Clock = pygame.time.Clock()

    game_over = False
    lost_counter = 0

    def redraw_window():
        SCREEN.blit(BG, (0, 0))

        lives_label = font.render(f"Lives: {lives}", 1, (WHITE))
        level_label = font.render(f"Level: {level}", 1, (WHITE))

        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)    

        player.draw(SCREEN)



        if game_over == True:
            game_over_text = game_over_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(game_over_text, (WIDTH / 2 - level_label.get_width() / 2, 350))


        pygame.display.update()




    while Start == True:
        Clock.tick(FPS)
        redraw_window() 

        if lives <= 0 or player.health <= 0:
            game_over = True
            lost_count += 1


        if game_over == True:
            if lost_count > FPS * 3:
                Start = False
            else:
                continue


        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                Start = False

        level1()
        player_controls()





main_menu()
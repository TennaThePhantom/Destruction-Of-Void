import imp
import pygame
import random
import time
import sys
import os
from pygame.locals import *
from Ships_Guns import *



WHITE = (255, 255, 255)

pygame.font.init()

WIDTH = 1000
HEIGHT = 800

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Destruction-Of-Void")
ICON = pygame.display.set_icon(pygame.image.load(os.path.join("Images", "void.jpg")))

BG = pygame.transform.scale(pygame.image.load(os.path.join("Images", "space_background.jpg" )), (WIDTH, HEIGHT))


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
    Start = True
    FPS = 60
    level = 0
    lives = 3
    movement = 5
    Guns_movement = 4

    font = pygame.font.SysFont("comicsans", 50)
    
    wave_length = 5
    Clock = pygame.time.Clock()

    game_over = False
    lost_counter = 0

    def redraw_window():
        SCREEN.blit(BG, (0, 0))

        lives_label = font.render(f"Lives: {lives}", 1, (WHITE))
        level_label = font.render(f"Level: {level}", 1, (WHITE))

        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))



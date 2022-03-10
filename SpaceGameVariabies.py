import pygame
import sys
import os
from pygame.locals import *
from Ships_Guns_Enimies import *
from UserSpaceShip import *

WHITE = (255, 255, 255)

pygame.font.init()

WIDTH = 1000
HEIGHT = 800
lives = 3
level = 1
money = 0
FPS = 60
Guns_movement = 4
game_over = False
enemies = []




SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Destruction-Of-Void")
ICON = pygame.display.set_icon(pygame.image.load(os.path.join("Images", "void.jpg")))

BG = pygame.transform.scale(pygame.image.load(os.path.join("Images", "space_background.jpg" )), (WIDTH, HEIGHT))





def fps_counter():
    Clock = pygame.time.Clock()
    Clock.tick(FPS)



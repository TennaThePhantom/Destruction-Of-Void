import pygame
from pygame.locals import *
import random
import time
import sys
import os


WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Destruction-Of-Void")
ICON = pygame.display.set_icon(pygame.image.load(os.path.join("Images", "void.jpg")))


ENEMY_SPACE_SHIP1 = pygame.image.load(os.path.join("Images", "enemy_ship_1.png" ))
ENEMY_SPACE_SHIP2 = pygame.image.load(os.path.join("Images", "enemy_ship_2.png" ))
ENEMY_SPACE_SHIP3 = pygame.image.load(os.path.join("Images", "enemy_ship_3.png" ))

# player ship
USER_SPACE_SHIP = pygame.image.load(os.path.join("Images", "space_ship.png" ))


RED_lASER = pygame.image.load(os.path.join("Images", "laser_red.png" ))
GREEN_LASER = pygame.image.load(os.path.join("Images", "laser_green.png" ))
BLUE_LASER = pygame.image.load(os.path.join("Images", "laser_blue.png" ))
YELLOW_LASER = pygame.image.load(os.path.join("Images", "laser_yellow.png" ))


BG = pygame.image.load(os.path.join("Images", "space_background.jpg" ))



start_game = True

while start_game == True:
    for window in pygame.event.get():
        if window.type == pygame.QUIT:
            start_game = False
        
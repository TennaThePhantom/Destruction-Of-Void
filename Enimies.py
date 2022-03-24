import pygame
import os
from pygame.locals import *
from SpaceGameVariabies import *



ENEMY_SPACE_SHIP1 = pygame.image.load(os.path.join("Images", "Enemies", "enemy_ship_1.png" ))
ENEMY_SPACE_SHIP2 = pygame.image.load(os.path.join("Images","Enemies", "enemy_ship_2.png" ))
ENEMY_SPACE_SHIP3 = pygame.image.load(os.path.join("Images", "Enemies", "enemy_ship_3.png" ))

# player player
USER_SPACE_SHIP = pygame.image.load(os.path.join("Images", "space_ship.png" ))


RED_lASER = pygame.image.load(os.path.join("Images", "Guns", "laser_red.png" ))
GREEN_LASER = pygame.image.load(os.path.join("Images", "Guns", "laser_green.png" ))
BLUE_LASER = pygame.image.load(os.path.join("Images", "Guns", "laser_blue.png" ))
YELLOW_LASER = pygame.image.load(os.path.join("Images", "Guns", "laser_yellow.png" ))


BOSS_SHIP1 = pygame.image.load(os.path.join("Images", "Bosses", "boss_1.png" ))
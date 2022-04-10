import pygame
import sys
import os
from pygame.locals import *
from PlayerShip import *

WHITE = (255, 255, 255)

pygame.font.init()

WIDTH = 1200
HEIGHT = 750
Guns_movement = 4
game_over = False
enemies = []
movement = 5.5
Clock = pygame.time.Clock()


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Destruction-Of-Void")
ICON = pygame.display.set_icon(pygame.image.load(os.path.join("Images", "void.jpg")))

BG = pygame.transform.scale(pygame.image.load(os.path.join("Images", "space_background.jpg" )), (WIDTH, HEIGHT))





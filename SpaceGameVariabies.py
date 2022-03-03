import pygame
import random
import time
import sys
import os
from pygame.locals import *

WHITE = (255, 255, 255)

pygame.font.init()

WIDTH = 1000
HEIGHT = 800


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Destruction-Of-Void")
ICON = pygame.display.set_icon(pygame.image.load(os.path.join("Images", "void.jpg")))

BG = pygame.transform.scale(pygame.image.load(os.path.join("Images", "space_background.jpg" )), (WIDTH, HEIGHT))
import pygame
from pygame.locals import *
import random
import time
import sys




pygame.init()

screen = pygame.display.set_mode((1000, 800))


start_game = True

while start_game == True:
    for window in pygame.event.get():
        if window.type ==pygame.QUIT:
            start_game = False
        
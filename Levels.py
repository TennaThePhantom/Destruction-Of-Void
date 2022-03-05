import pygame
import random
import time
import sys
import os
from pygame.locals import *
from Enimies import *
from SpaceGameVariabies import *
from Ships_Guns import *



def level1():
    global End_Game
    global FPS
    start_level_1 = True
    enemies = []
    wave_length = 6
    Death_At_Level_1 = False
    while start_level_1 == True:

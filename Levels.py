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
    global enemies
    start_level_1 = True
    wave_length = 0
    Death_At_Level_1 = False
    enemies_movement = 5
    enemies_guns_speed = 2
    for enemy in enemies:
        enemy.move(enemies_movement)
        enemy.move_lasers(enemies_guns_speed, player)
        if random.randrange(0, 120) == 1:
            enemy.shoot()
        if collide(enemy, player):
            player.health -= 10
            enemies.remove(enemy)
        if len(enemies) == 0:
            level += 1
            wave_length += 6
            for enemy_amount in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)


        

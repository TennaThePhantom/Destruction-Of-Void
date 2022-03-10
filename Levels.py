import pygame
import random
import time
import os
from pygame.locals import *
from Enimies import *
from SpaceGameVariabies import *
from Ships_Guns_Enimies import *
from UserSpaceShip import *

def level1():
    global End_Game
    global FPS
    global enemies
    global level
    wave_length = 0
    enemies_movement = 2
    enemies_guns_speed = 4
    game_over = False
    if len(enemies) == 0:
        level += 1
        wave_length += 6
        for enemy_amount in range(wave_length):
            enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
            enemies.append(enemy)
    for enemy in enemies:
        enemy.move(enemies_movement)
        enemy.move_lasers(enemies_guns_speed, player)
        if random.randrange(0, 120) == 1:
            enemy.shoot()
        if collide(enemy, player):
            player.health -= 10
            enemies.remove(enemy)
    pygame.display.update()


        

import pygame
import random
import time
import os
from pygame.locals import *
from Enimies import *
from SpaceGameVariabies import *
from Ships_Guns_Enimies import *
from UserSpaceShip import *

def level1(level):
    global enemies
    wave_length = 4
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 1:
        if len(enemies) == 0:
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
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)

        pygame.display.update()



def level2(level):
    global enemies
    wave_length = 6
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 2:
        if len(enemies) == 0: 
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
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)

        pygame.display.update()


def level3(level):
    global enemies
    wave_length = 7
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 3:
        if len(enemies) == 0:
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
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)

        pygame.display.update()

def level4(level):
    global enemies
    wave_length_1 = 8
    wave_length_2 = 4
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 4:
        if len(enemies) == 0:
            for enemy_amount in range(wave_length_1):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)    
            for enemy_amount in range(wave_length_2):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1800, -1000), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)  
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)

        pygame.display.update()

def level5(level):
    global enemies
    wave_length_1 = 9
    wave_length_2 = 3
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 5:
        if len(enemies) == 0:
            for enemy_amount in range(wave_length_1):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)
            for enemy_amount in range(wave_length_2):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1700, -600), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)
            Boss = boss1(random.randrange(50, WIDTH - 100), random.randrange(-3000, -2500), random.choice(["Boss"]) )
            enemies.append(Boss)

        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)
            

        pygame.display.update()

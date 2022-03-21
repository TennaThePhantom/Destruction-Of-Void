from pickle import TRUE
from traceback import print_tb
from turtle import down
import wave
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
    wave_length = 5
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
    wave_length = 7
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
    wave_length = 10
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
    time_for_next_wave = 360
    wave_length_1 = 11
    wave_length_2 = 4
    enemies_movement = 1.5
    enemies_guns_speed = 4
    once = False
    wave2_Happen = False
    if level == 4:
        if len(enemies) == 0:
            for enemy_amount in range(wave_length_1):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)
        if len(enemies) <= 8 and wave2_Happen == True:
            wave_length_2 -= 4
            wave_length_1 -= 11
            print(wave_length_2)
        if len(enemies) == 6 and wave2_Happen == False:
            once = True
            if once == True and wave2_Happen == False:
                print("Starting wave two")
                for enemy_amount in range(wave_length_2):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                    enemies.append(enemy)
                print("wave two ends")
            return wave2_Happen == True

        
    
        print(len(enemies))

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


def level4_P2():
    global enemies
    wave_length_2 = 4
    enemies_movement = 1.5
    enemies_guns_speed = 4
    for enemy_amount in range(wave_length_2):
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


def level5(level):
    global enemies
    wave_length_1 = 8
    wave_length_2 = 6
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 5:
        if len(enemies) == 0:
            for enemy_amount in range(wave_length_1):
                start_next = wave_length_1 - 1
                print(start_next)
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)
        if len(enemies) == 4:
            for enemy_amount in range(wave_length_2):
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

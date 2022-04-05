import imp
import pygame
import random
import time
import os
from pygame.locals import *
from Enimies import *
from SpaceGameVariabies import *
from PlayerShip import *
from Regular_enimies import *
from Special_enimies import *
from Big_enimies import *
from Mega_enimies import * 
from Lasers_EnergyBalls import *

def level1(level):
    global enemies
    wave_length = 4
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 1:
        if len(enemies) == 0:
            for enemy_amount in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2"]))
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 5
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
                player.health -= 5
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
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 2", "Enemy 4", "Enemy 5"]))
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 5
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
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 2", "Enemy 4"]))
                enemies.append(enemy)    
            for enemy_amount in range(wave_length_2):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1800, -1000), random.choice(["Enemy 1", "Enemy 3", "Enemy 5"]))
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
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 5", "Enemy 4"]))
                enemies.append(enemy)
            for enemy_amount in range(wave_length_2):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1700, -900), random.choice(["Enemy 3", "Enemy 4"]))
                enemies.append(enemy)
            Speical_Enemy = Speical1(random.randrange(50, WIDTH - 100), random.randrange(-1500, -1400), random.choice(["Speical_Enemy"]))
            enemies.append(Speical_Enemy)
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


def level6(level):
    global enemies
    wave1_length = 8
    wave2_length = 5
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 6:    
        if len(enemies) == 0:
                for enemy_amount in range(wave1_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["Enemy 7", "Enemy 6", "Enemy 4", "Enemy 2", ]))
                    enemies.append(enemy)
                for enemy_amount in range(wave2_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1800, -1200), random.choice(["Enemy 7", "Enemy 3"]))
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

def level7(level):
    global enemies
    wave1_length = 10
    wave2_length = 7
    enemies_movement = 1.5
    enemies_guns_speed = 4
    if level == 7:    
        if len(enemies) == 0:
                for enemy_amount in range(wave1_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1800, -100), random.choice(["Enemy 7", "Enemy 6", "Enemy 4", "Enemy 2", ]))
                    enemies.append(enemy)
                for enemy_amount in range(wave2_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-2400, -1500), random.choice(["Enemy 7", "Enemy 3"]))
                    enemies.append(enemy)
                for speical_amount in range(2):
                    Speical_Enemy = Speical1(random.randrange(50, WIDTH - 100), random.randrange(-2200, -2000), random.choice(["Speical_Enemy"]))
                    enemies.append(Speical_Enemy)
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
            
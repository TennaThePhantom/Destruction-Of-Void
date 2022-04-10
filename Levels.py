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
    enemies_movement = 1.2
    enemies_guns_speed = 3.3
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
    enemies_movement = 1.2
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
    enemies_movement = 1.2
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
    enemies_movement = 1.2
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
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 5:
        if len(enemies) == 0:
            for enemy_amount in range(wave_length_1):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 5", "Enemy 4"]))
                enemies.append(enemy)
            for enemy_amount in range(wave_length_2):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1700, -900), random.choice(["Enemy 3", "Enemy 4"]))
                enemies.append(enemy)
            Speical_Enemy = Speical1(random.randrange(50, WIDTH - 100), random.randrange(-1500, -1400), random.choice(["Special_Enemy"]), 100, 19)
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
    enemies_movement = 1.2
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
    enemies_movement = 1.2
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
                    Speical_Enemy = Speical1(random.randrange(50, WIDTH - 100), random.randrange(-2200, -2000), random.choice(["Special_Enemy"]), 100, 22)
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

def level8(level):
    global enemies
    wave1_length = 9
    wave2_length = 7
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 8:    
        if len(enemies) == 0:
                for enemy_amount in range(wave1_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1400, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 6", "Enemy 5", ]))
                    enemies.append(enemy)
                for enemy_amount in range(wave2_length):
                    enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1400), random.choice(["Enemy 8", "Enemy 4"]))
                    enemies.append(enemy)
                for speical_amount in range(3):
                    Speical_Enemy = Speical1(random.randrange(50, WIDTH - 100), random.randrange(-1800, -1600), random.choice(["Special_Enemy"]), 100, 22)
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


def level9(level):
    global enemies
    wave1_length = 8
    wave2_length = 7
    special_enemies = 3
    special_enemie2 = 3
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 9:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1_length):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1400, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2_length):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1000), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(special_enemies):
                enemy = Speical1(random.randrange(50, WIDTH - 150), random.randrange(-1800, -1500), random.choice(["Special_Enemy"]),100, 22)
                enemies.append(enemy)
            for enemy_amount in range(special_enemie2):
                enemy = Speical2(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1700), random.choice(["Special_Enemy"]), 100, 27)
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


def level10(level):
    global enemies
    wave1_length = 10
    special_enemies = 3
    enemies_movement = 1.2
    enemies_guns_speed = 4
    speical_enemy3 = 4
    if level == 10:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1_length):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1800, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(special_enemies):
                enemy = Speical1(random.randrange(50, WIDTH - 150), random.randrange(-1600, -1200), random.choice(["Special_Enemy"]), 100, 20)
                enemies.append(enemy)
                enemy = Speical2(random.randrange(50, WIDTH - 150), random.randrange(-1800, -1200), random.choice(["Special_Enemy"]), 100, 19)
                enemies.append(enemy)
            for enemy_amount in range(speical_enemy3):
                enemy = Speical3(random.randrange(50, WIDTH - 150), random.randrange(-1400, -400), random.choice(["Special_Enemy"]), 100, 22)
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


def level11(level):
    global enemies
    wave1_length = 15
    wave2_length = 11
    fast_wave = 7
    special_enemy = 3
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 11:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1_length):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2_length):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-2800, -1500), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(fast_wave):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1600), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(special_enemy):
                enemy = Speical4(random.randrange(50, WIDTH - 150), random.randrange(-2500, -2100), random.choice(["Special_Enemy"]),100, 40)
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 20
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)


def level12(level):
    global enemies
    wave1_length = 15
    special_enemies = 4
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 12:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1_length):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(special_enemies):
                enemy = Speical5(random.randrange(50, WIDTH - 150), random.randrange(-1800, -100), random.choice(["Special_Enemy"]),100, 14)
                enemies.append(enemy)
                enemy = Speical6(random.randrange(50, WIDTH - 150), random.randrange(-1800, -100), random.choice(["Special_Enemy"]),100, 65)
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 20
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)


def level13(level):
    global enemies
    wave1_length = 11
    wave2_length = 8
    special_enemies = 5
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 13:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1_length):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2_length):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(special_enemies):
                enemy = Speical1(random.randrange(50, WIDTH - 150), random.randrange(-2000, -100), random.choice(["Special_Enemy"]),100, 20)
                enemies.append(enemy)
                enemy = Speical2(random.randrange(50, WIDTH - 150), random.randrange(-2000, -900), random.choice(["Special_Enemy"]),100, 25)
                enemies.append(enemy)
                enemy = Speical3(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1400), random.choice(["Special_Enemy"]),100, 22)
                enemies.append(enemy)
                enemy = Speical7(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1200), random.choice(["Special_Enemy"]),100, 38)
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 20
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)


def level14(level):
    global enemies
    wave1_length = 18
    wave2_length = 15
    wave3_length = 12
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 14:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1_length):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2_length):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-2900, -1700), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave3_length):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-3800, -2600), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 20
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)
    
def level15(level):
    global enemies
    special_enemies = 4
    enemies_movement = 1.2
    enemies_guns_speed = 4
    if level == 15:    
        if len(enemies) == 0:
            for enemy_amount in range(special_enemies):
                enemy = Speical1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]), 100, 20)
                enemies.append(enemy)
                enemy = Speical2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]), 100, 24)
                enemies.append(enemy)
                enemy = Speical3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]), 100, 28)
                enemies.append(enemy)
                enemy = Speical4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]), 100, 17)
                enemies.append(enemy)
                enemy = Speical5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]), 100, 50)
                enemies.append(enemy)
                enemy = Speical6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]), 100, 29)
                enemies.append(enemy)
                enemy = Speical7(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]), 100, 32)
                enemies.append(enemy)
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(enemies_guns_speed, player)
            if random.randrange(0, 120) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 20
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                enemies.remove(enemy)








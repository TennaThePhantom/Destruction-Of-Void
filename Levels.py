import imp
import pygame
import random
from pygame.locals import *
from Enemies import *
from SpaceGameVariabies import *
from PlayerShip import *
from Regular_enemies import *
from Special_enemies import *
from Big_enemies import *
from Mega_enimies import * 
from Lasers_EnergyBalls import *



def level1(level):
    global enemies
    wave1 = 4
    enemies_movement = 1.2
    enemies_guns_speed = 3.3
    if level == 1:
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
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
    wave1 = 6
    enemies_movement = 1.2
    enemies_guns_speed = 3.3
    if level == 2:
        if len(enemies) == 0: 
            for enemy_amount in range(wave1):
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
    wave1 = 7
    enemies_movement = 1.2
    enemies_guns_speed = 3.3
    if level == 3:
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
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
    wave1 = 8
    wave2 = 4
    enemies_movement = 1.2
    enemies_guns_speed = 3.3
    if level == 4:
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 2", "Enemy 4"]))
                enemies.append(enemy)    
            for enemy_amount in range(wave2):
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
    wave1 = 9
    wave2 = 3
    enemies_movement = 1.2
    enemies_guns_speed = 3.3
    if level == 5:
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 5", "Enemy 4"]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1700, -900), random.choice(["Enemy 3", "Enemy 4"]))
                enemies.append(enemy)
            Special_Enemy = Special1(random.randrange(50, WIDTH - 100), random.randrange(-1500, -1400), random.choice(["Special_Enemy"]))
            enemies.append(Special_Enemy)
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
    wave1 = 8
    wave2 = 5
    enemies_movement = 1.3
    enemies_guns_speed = 3.5
    if level == 6:    
        if len(enemies) == 0:
                for enemy_amount in range(wave1):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["Enemy 7", "Enemy 6", "Enemy 4", "Enemy 2", ]))
                    enemies.append(enemy)
                for enemy_amount in range(wave2):
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
    wave1 = 10
    wave2 = 7
    specialwave = 2
    enemies_movement = 1.3
    enemies_guns_speed = 3.5
    if level == 7:    
        if len(enemies) == 0:
                for enemy_amount in range(wave1):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1800, -100), random.choice(["Enemy 7", "Enemy 6", "Enemy 4", "Enemy 2", ]))
                    enemies.append(enemy)
                for enemy_amount in range(wave2):
                    enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-2400, -1500), random.choice(["Enemy 7", "Enemy 3"]))
                    enemies.append(enemy)
                for enemy_amount in range(specialwave):
                    enemy = Special1(random.randrange(50, WIDTH - 100), random.randrange(-2200, -2000), random.choice(["Special_Enemy"]))
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

def level8(level):
    global enemies
    wave1 = 9
    wave2 = 7
    specialwave = 3
    enemies_movement = 1.3
    enemies_guns_speed = 3.5
    if level == 8:    
        if len(enemies) == 0:
                for enemy_amount in range(wave1):
                    enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1400, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 6", "Enemy 5", ]))
                    enemies.append(enemy)
                for enemy_amount in range(wave2):
                    enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1400), random.choice(["Enemy 8", "Enemy 4"]))
                    enemies.append(enemy)
                for enemy_amount in range(specialwave):
                    enemy = Special1(random.randrange(50, WIDTH - 100), random.randrange(-1800, -1600), random.choice(["Special_Enemy"]))
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


def level9(level):
    global enemies
    wave1 = 8
    wave2 = 7
    specialwave = 3
    enemies_movement = 1.3
    enemies_guns_speed = 3.5
    if level == 9:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1400, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1000), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-1800, -1500), random.choice(["Special_Enemy"]))
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1700), random.choice(["Special_Enemy"]))
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
    wave1 = 10
    specialwave = 3
    enemies_movement = 1.3
    enemies_guns_speed = 3.5
    if level == 10:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1800, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-1600, -1200), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-1800, -1200), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-1400, -400), random.choice(["Special_Enemy"]))
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
    wave1 = 15
    wave2 = 11
    specialwave = 5
    enemies_movement = 1.3
    enemies_guns_speed = 3.6
    if level == 11:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-2800, -1500), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-2500, -2100), random.choice(["Special_Enemy"]))
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
    wave1 = 15
    specialwave = 4
    enemies_movement = 1.3
    enemies_guns_speed = 3.6
    if level == 12:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-1800, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-1800, -100), random.choice(["Special_Enemy"]))
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
    wave1 = 11
    wave2 = 8
    specialwave = 5
    enemies_movement = 1.3
    enemies_guns_speed = 3.6
    if level == 13:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-2000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-2000, -900), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1400), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1200), random.choice(["Special_Enemy"]))
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
    wave1 = 18
    wave2 = 15
    wave3_length = 12
    enemies_movement = 1.3
    enemies_guns_speed = 3.6
    if level == 14:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
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
    specialwave = 4
    enemies_movement = 1.3
    enemies_guns_speed = 3.6
    if level == 15:    
        if len(enemies) == 0:
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
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


def level16(level):
    global enemies
    wave1 = 16
    wave2 = 10
    wave3 = 9
    specialwave = 1
    Bigwave = 3
    enemies_movement = 1.4
    enemies_guns_speed = 3.7
    if level == 16:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-3600, -1800), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave3):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-4000, -3000), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1500), random.choice(["Big_Enemy"]))
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



def level17(level):
    global enemies
    wave1 = 25
    wave2 = 10
    specialwave = 2
    Bigwave = 3
    enemies_movement = 1.4
    enemies_guns_speed = 3.7
    if level == 17:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-3500, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-3600, -1800), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy2(random.randrange(50, WIDTH - 150), random.randrange(-500, -100), random.choice(["Big_Enemy"]))
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




def level18(level):
    global enemies
    wave1 = 8
    wave2 = 10
    wave3 = 12
    wave4 = 26
    Bigwave = 4
    enemies_movement = 1.4
    enemies_guns_speed = 3.7
    if level == 18:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-2000, -1300), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave3):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-3500, -2100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave4):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-4200, -1500), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy3(random.randrange(50, WIDTH - 150), random.randrange(-3700, -2900), random.choice(["Big_Enemy"]))
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




def level19(level):
    global enemies
    wave1 = 14
    wave2 = 18
    Bigwave = 3
    enemies_movement = 1.4
    enemies_guns_speed = 3.7
    if level == 19:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-2900, -1300), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy4(random.randrange(50, WIDTH - 150), random.randrange(-2500, -1700), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy5(random.randrange(50, WIDTH - 150), random.randrange(-2800, -2300), random.choice(["Big_Enemy"]))
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



def level20(level):
    global enemies
    wave1 = 10
    specialwave = 5
    Bigwave = 2
    enemies_movement = 1.4
    enemies_guns_speed = 3.7
    if level == 20:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-1700, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-4000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-4000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-4000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-4000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-4000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy6(random.randrange(50, WIDTH - 150), random.randrange(-2800, -2300), random.choice(["Big_Enemy"]))
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


def level21(level):
    global enemies
    wave1 = 40
    wave2 = 35
    Megawave = 3
    enemies_movement = 1.6
    enemies_guns_speed = 4.1
    if level == 21:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-4000, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(Megawave):
                enemy = Mega1(random.randrange(50, WIDTH - 150), random.randrange(-5000, -3000), random.choice(["Mega_Enemy"]))
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




def level22(level):
    global enemies
    wave1 = 30
    Megawave = 3
    Bigwave = 3
    specialwave = 5
    enemies_movement = 1.6
    enemies_guns_speed = 4.1
    if level == 22:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-4000, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy2(random.randrange(50, WIDTH - 150), random.randrange(-1000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy4(random.randrange(50, WIDTH - 150), random.randrange(-4000, -2000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Megawave):
                enemy = Mega2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Mega_Enemy"]))
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




def level23(level):
    global enemies
    wave1 = 30
    Megawave = 4
    Bigwave = 4
    specialwave = 3
    enemies_movement = 1.6
    enemies_guns_speed = 4.2
    if level == 23:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-4000, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy5(random.randrange(50, WIDTH - 150), random.randrange(-1000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Megawave):
                enemy = Mega3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -2000), random.choice(["Mega_Enemy"]))
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



def level24(level):
    global enemies
    wave1 = 15
    Megawave = 3
    Bigwave = 3
    specialwave = 6
    enemies_movement = 1.6
    enemies_guns_speed = 4.2
    if level == 24:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy2(random.randrange(50, WIDTH - 150), random.randrange(-1000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Megawave):
                enemy = Mega4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Mega_Enemy"]))
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


def level25(level):
    global enemies
    Bigwave = 4
    specialwave = 5
    enemies_movement = 1.7
    enemies_guns_speed = 4.4
    if level == 25:    
        if len(enemies) == 0:
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -1000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
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



def level26(level):
    global enemies
    specialwave = 3
    Bigwave = 8
    enemies_movement = 1.8
    enemies_guns_speed = 4.7
    if level == 26:    
        if len(enemies) == 0:
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy1(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy2(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy3(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy4(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy5(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy6(random.randrange(50, WIDTH - 150), random.randrange(-3000, -100), random.choice(["Big_Enemy"]))
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





def level27(level):
    global enemies
    wave1 = 60
    wave2 = 40
    enemies_movement = 1.8
    enemies_guns_speed = 4.6
    if level == 27:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)      
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-8000, -3000), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
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



def level28(level):
    global enemies
    wave1 = 55
    Megawave = 4
    enemies_movement = 1.9
    enemies_guns_speed = 4.8
    if level == 28:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(Megawave):
                enemy = Mega1(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega2(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega3(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega4(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
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



def level29(level):
    global enemies
    Megawave = 10
    Bigwave = 15
    enemies_movement = 1.9
    enemies_guns_speed = 4.9
    if level == 29:    
        if len(enemies) == 0:
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy1(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy2(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy3(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy4(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy5(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy6(random.randrange(50, WIDTH - 150), random.randrange(-5000, -100), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Megawave):
                enemy = Mega1(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega2(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega3(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega4(random.randrange(50, WIDTH - 50), random.randrange(-5000, -1000), random.choice(["Mega_Enemy"]))
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




def level30(level):
    global enemies
    Megawave = 5
    Bigwave = 8
    specialwave = 10
    wave1 = 60
    wave2 = 50
    enemies_movement = range(1, 2 + 1)
    enemies_guns_speed = range(4, 5 + 1)
    if level == 30:    
        if len(enemies) == 0:
            for enemy_amount in range(wave1):
                enemy = Enemy(random.randrange(50, WIDTH - 150), random.randrange(-6000, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(wave2):
                enemy = Enemy2(random.randrange(50, WIDTH - 150), random.randrange(-10000, -4000), random.choice(["Enemy 1", "Enemy 2", "Enemy 3", "Enemy 4", "Enemy 5", "Enemy 6", "Enemy 7", "Enemy 8",]))
                enemies.append(enemy)
            for enemy_amount in range(specialwave):
                enemy = Special1(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special2(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special3(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special4(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special5(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special6(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
                enemy = Special7(random.randrange(50, WIDTH - 150), random.randrange(-6000, -2000), random.choice(["Special_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Bigwave): 
                enemy = BigEnemy1(random.randrange(50, WIDTH - 150), random.randrange(-8000, -4000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy2(random.randrange(50, WIDTH - 150), random.randrange(-8000, -4000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy3(random.randrange(50, WIDTH - 150), random.randrange(-8000, -4000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy4(random.randrange(50, WIDTH - 150), random.randrange(-8000, -4000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy5(random.randrange(50, WIDTH - 150), random.randrange(-8000, -4000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
                enemy = BigEnemy6(random.randrange(50, WIDTH - 150), random.randrange(-8000, -4000), random.choice(["Big_Enemy"]))
                enemies.append(enemy)
            for enemy_amount in range(Megawave):
                enemy = Mega1(random.randrange(50, WIDTH - 50), random.randrange(-10000, -5000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega2(random.randrange(50, WIDTH - 50), random.randrange(-10000, -5000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega3(random.randrange(50, WIDTH - 50), random.randrange(-10000, -5000), random.choice(["Mega_Enemy"]))
                enemies.append(enemy)
                enemy = Mega4(random.randrange(50, WIDTH - 50), random.randrange(-10000, -5000), random.choice(["Mega_Enemy"]))
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









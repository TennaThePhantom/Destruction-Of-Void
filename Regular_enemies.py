import pygame
import os
from pygame.locals import * 
from Enemies import *
from SpaceGameVariables import *
from Lasers_EnergyBalls import *

WIDTH = 1200
HEIGHT = 750


class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    
    def move(self, movement):
        self.y += movement

    def off_screen(self, height):
        return not (self.y < height and self.y >= 0)

    def collision(self, hit):
        return collide(self, hit)



class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100, damage=10):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.laser_countdown = 0
        self.damage = damage

    def draw(self, window):
        window.blit(self.ship_img,(self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
    
    def move_lasers(self, movement, Object):
        self.cooldown()
        for laser in self.lasers:
            laser.move(movement)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(Object):
                Object.health -= self.damage
                self.lasers.remove(laser)


    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self): 
        return self.ship_img.get_height()

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1
    
    def cooldown(self):
        if self.laser_countdown >= self.COOLDOWN:
            self.laser_countdown = 0
        elif self.laser_countdown > 0:
            self.laser_countdown += 1



class Ship2:
    COOLDOWN = 30

    def __init__(self, x, y, health=100, damage=18):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.laser_countdown = 0
        self.damage = damage

    def draw(self, window):
        window.blit(self.ship_img,(self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
    
    def move_lasers(self, movement, Object):
        self.cooldown()
        for laser in self.lasers:
            laser.move(movement)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(Object):
                Object.health -= self.damage
                self.lasers.remove(laser)


    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self): 
        return self.ship_img.get_height()

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1
    
    def cooldown(self):
        if self.laser_countdown >= self.COOLDOWN:
            self.laser_countdown = 0
        elif self.laser_countdown > 0:
            self.laser_countdown += 1



class Enemy(Ship):
    ENEMY_MAP = {
            "Enemy 1": (ENEMY_SPACE_SHIP1, BLUE_LASER),
            "Enemy 2": (ENEMY_SPACE_SHIP2, BLUE_LASER),
            "Enemy 3": (ENEMY_SPACE_SHIP3, BLUE_LASER),
            "Enemy 4": (ENEMY_SPACE_SHIP4, BLUE_LASER),            
            "Enemy 5": (ENEMY_SPACE_SHIP5, BLUE_LASER),
            "Enemy 6": (ENEMY_SPACE_SHIP6, BLUE_LASER),
            "Enemy 7": (ENEMY_SPACE_SHIP7, BLUE_LASER),
            "Enemy 8": (ENEMY_SPACE_SHIP8, BLUE_LASER),
            }
    def __init__(self, x, y, color, health=100, damage=10):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1



class Enemy2(Ship):
    ENEMY_MAP = {
            "Enemy 1": (ENEMY_SPACE_SHIP1, GREEN_LASER),
            "Enemy 2": (ENEMY_SPACE_SHIP2, GREEN_LASER),
            "Enemy 3": (ENEMY_SPACE_SHIP3, GREEN_LASER),
            "Enemy 4": (ENEMY_SPACE_SHIP4, GREEN_LASER),            
            "Enemy 5": (ENEMY_SPACE_SHIP5, GREEN_LASER),
            "Enemy 6": (ENEMY_SPACE_SHIP6, GREEN_LASER),
            "Enemy 7": (ENEMY_SPACE_SHIP7, GREEN_LASER),
            "Enemy 8": (ENEMY_SPACE_SHIP8, GREEN_LASER),
            }
    def __init__(self, x, y, color, health=100, damage=18):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1



def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None
import pygame
import os
from pygame.locals import * 
from Enemies import *
from SpaceGameVariabies import *
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



class Laser2:
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



class Laser3:
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



class MegaEnemies1:
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




class MegaEnemies2:
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

class MegaEnemies3:
    COOLDOWN = 3

    def __init__(self, x, y, health=100, damage=80):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.laser_img2 = None
        self.laser_img3 = None
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
            laser2 = Laser2(self.x, self.y, self.laser_img2)
            self.lasers.append(laser2)
            laser3 = Laser3(self.x, self.y, self.laser_img3)
            self.lasers.append(laser3)
            self.laser_countdown = 1

    def cooldown(self):
        if self.laser_countdown >= self.COOLDOWN:
            self.laser_countdown = 0
        elif self.laser_countdown > 0:
            self.laser_countdown += 1



class MegaEnemies4:
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
            laser2 = Laser2(self.x, self.y, self.laser_img2)
            self.lasers.append(laser2)
            self.laser_countdown = 1

    def cooldown(self):
        if self.laser_countdown >= self.COOLDOWN:
            self.laser_countdown = 0
        elif self.laser_countdown > 0:
            self.laser_countdown += 1

class Mega1(MegaEnemies1):

    COLOR_MAP = {
            "Mega_Enemy": (MEGA_ENEMY1, PURPLE_FLAME_ENERGY_BALL),
            }
    def __init__(self, x, y, color, health=100, damage=160):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self. mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x + 85, self.y + 140, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1


class Mega2(MegaEnemies2):

    COLOR_MAP = {
            "Mega_Enemy": (MEGA_ENEMY2, GOLD_ENERGY_BALL),
            }
    def __init__(self, x, y, color, health=100, damage=200):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self. mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x + 100, self.y + 160, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1


class Mega3(MegaEnemies3):

    COLOR_MAP = {
            "Mega_Enemy": (MEGA_ENEMY3, SPARKING_ENERGY_BALL, SPARKING_ENERGY_BALL, SPARKING_ENERGY_BALL),
            }
    def __init__(self, x, y, color, health=100, damage=150):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img, self.laser_img2, self.laser_img3 = self.COLOR_MAP[color]
        self. mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x + 30, self.y + 100, self.laser_img)
            self.lasers.append(laser)
            laser2 = Laser(self.x - 70, self.y + 100, self.laser_img2)
            self.lasers.append(laser2)
            laser3 = Laser(self.x + 120, self.y + 100, self.laser_img3)
            self.lasers.append(laser3)
            self.laser_countdown = 1


class Mega4(MegaEnemies4):

    COLOR_MAP = {
            "Mega_Enemy": (MEGA_ENEMY4, DARKBLUE_LIGHT_LASER, DARKBLUE_LIGHT_LASER),
            }
    def __init__(self, x, y, color, health=100, damage=180):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img, self.laser_img2 = self.COLOR_MAP[color]
        self. mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x + 150 , self.y + 150, self.laser_img)
            self.lasers.append(laser)
            laser2 = Laser(self.x + 20, self.y + 150, self.laser_img2)
            self.lasers.append(laser2)
            self.laser_countdown = 1
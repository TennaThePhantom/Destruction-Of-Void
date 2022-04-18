import pygame
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



class SpecialEnemies1:
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



class SpecialEnemies2:
    COOLDOWN = 5

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



class SpecialEnemies3:
    COOLDOWN = 30

    def __init__(self, x, y, health=100, damage=10):
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



class SpecialEnemies4:
    COOLDOWN = 90

    def __init__(self, x, y, health=100, damage=50):
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



class SpecialEnemies5:
    COOLDOWN = 1

    def __init__(self, x, y, health=100, damage=10):
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
            self.laser_countdown = 1

    def cooldown(self):
        if self.laser_countdown >= self.COOLDOWN:
            self.laser_countdown = 0
        elif self.laser_countdown > 0:
            self.laser_countdown += 1



class SpecialEnemies6:
    COOLDOWN = 100

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



class SpecialEnemies7:
    COOLDOWN = 140

    def __init__(self, x, y, health=100, damage=10):
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
            self.laser_countdown = 1

    def cooldown(self):
        if self.laser_countdown >= self.COOLDOWN:
            self.laser_countdown = 0
        elif self.laser_countdown > 0:
            self.laser_countdown += 1



class Special1(SpecialEnemies1):

    ENEMY_MAP = {
            "Special_Enemy": (SPECIAL_SHIP1, RED_lASER),
            }
    def __init__(self, x, y, color, health=100, damage=25):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x, self.y + 35, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1



class Special2(SpecialEnemies2):

    ENEMY_MAP = {
            "Special_Enemy": (SPECIAL_SHIP4, RED_lASER),
            }
    def __init__(self, x, y, color, health=100, damage=28):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x, self.y + 35, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1



class Special3(SpecialEnemies3):


    ENEMY_MAP = {
            "Special_Enemy": (SPECIAL_SHIP2, RED_lASER, RED_lASER, RED_lASER),
            }
    def __init__(self, x, y, color, health=100, damage=19):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img, self.laser_img2, self.laser_img3 = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x, self.y + 50, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1
            laser2 = Laser2(self.x - 40, self.y + 70, self.laser_img2)
            self.lasers.append(laser2)
            laser3 = Laser3(self.x + 40, self.y + 70, self.laser_img3)
            self.lasers.append(laser3)
            self.laser_countdown = 1



class Special4(SpecialEnemies4):

    ENEMY_MAP = {
            "Special_Enemy": (SPECIAL_SHIP3, BLUE_AND_DARKBLUE_lASER),
            }
    def __init__(self, x, y, color, health=100, damage=35):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x + 15, self.y + 50, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1



class Special5(SpecialEnemies5):

    ENEMY_MAP = {
            "Special_Enemy": (SPECIAL_SHIP5, BLUE_LASER, BLUE_LASER, BLUE_LASER),
            }
    def __init__(self, x, y, color, health=100, damage=17):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img, self.laser_img2, self.laser_img3 = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x, self.y + 50, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1
            laser2 = Laser2(self.x + 40, self.y + 50, self.laser_img2)
            self.lasers.append(laser2)
            laser3 = Laser3(self.x - 40, self.y + 50, self.laser_img3)
            self.lasers.append(laser3)
            self.laser_countdown = 1



class Special6(SpecialEnemies6):

    ENEMY_MAP = {
            "Special_Enemy": (SPECIAL_SHIP6, ENERGY_STAR_BALL),
            }
    def __init__(self, x, y, color, health=100, damage=32):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x - 30, self.y, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1



class Special7(SpecialEnemies7):

    ENEMY_MAP = {
            "Special_Enemy": (SPECIAL_SHIP7, BLUE_AND_DARKBLUE_lASER, RED_lASER, RED_lASER),
            }
    def __init__(self, x, y, color, health=100, damage=35):
        super().__init__(x, y, health, damage)
        self.ship_img, self.laser_img, self.laser_img2, self.laser_img3 = self.ENEMY_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x + 20, self.y + 50, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1
            laser2 = Laser2(self.x + 40, self.y + 50, self.laser_img2)
            self.lasers.append(laser2)
            laser3 = Laser3(self.x - 40, self.y + 50, self.laser_img3)
            self.lasers.append(laser3)
            self.laser_countdown = 1





















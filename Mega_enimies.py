import pygame
import os
from pygame.locals import * 
from Enimies import *
from SpaceGameVariabies import *
from Lasers_EnergyBalls import *


HEIGHT = 800
WIDTH = 1200


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

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.laser_countdown = 0

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
                Object.health -= 10
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

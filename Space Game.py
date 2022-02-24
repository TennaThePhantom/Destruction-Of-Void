import pygame
from pygame.locals import *
import random
import time
import sys
import os

WHITE = (255, 255, 255)

pygame.font.init()


WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Destruction-Of-Void")
ICON = pygame.display.set_icon(pygame.image.load(os.path.join("Images", "void.jpg")))


ENEMY_SPACE_SHIP1 = pygame.image.load(os.path.join("Images", "enemy_ship_1.png" ))
ENEMY_SPACE_SHIP2 = pygame.image.load(os.path.join("Images", "enemy_ship_2.png" ))
ENEMY_SPACE_SHIP3 = pygame.image.load(os.path.join("Images", "enemy_ship_3.png" ))

# player player
USER_SPACE_SHIP = pygame.image.load(os.path.join("Images", "space_ship.png" ))


RED_lASER = pygame.image.load(os.path.join("Images", "laser_red.png" ))
GREEN_LASER = pygame.image.load(os.path.join("Images", "laser_green.png" ))
BLUE_LASER = pygame.image.load(os.path.join("Images", "laser_blue.png" ))
YELLOW_LASER = pygame.image.load(os.path.join("Images", "laser_yellow.png" ))


BG = pygame.transform.scale(pygame.image.load(os.path.join("Images", "space_background.jpg" )), (WIDTH, HEIGHT))


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.lazer_countdown = 0

    def draw(self, window):
        window.blit(self.ship_img,(self.x, self.y))
    
    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self): 
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = USER_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img) # collusion
        self.max_health = health 
    


class Enemy(Ship):
    COLOR_MAP = {
            "Enemy 1": (ENEMY_SPACE_SHIP1, RED_lASER),
            "Enemy 2": (ENEMY_SPACE_SHIP2, BLUE_LASER),
            "Enemy 3": (ENEMY_SPACE_SHIP3, GREEN_LASER)}
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self. mask = pygame.mask.from_surface(self.ship_img)
    
    def move(self, movemoment):
        self.y += movemoment


def StartGame():
    Start = True
    FPS = 60
    level = 0
    lives = 3
    movement = 5 
    font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 10
    enemies_movement = 1
    player = Player(300, 650)

    Clock = pygame.time.Clock()


    game_over = False


    def redraw_window():
        SCREEN.blit(BG, (0,0))

        lives_label = font.render(f"Lives: {lives}", 1, (WHITE))
        level_label = font.render(f"Level: {level}", 1, (WHITE))


        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)


        player.draw(SCREEN)
        
        pygame.display.update()


    while Start == True:
        Clock.tick(FPS)

        if lives <= 0 or player.health <= 0:
            game_over = True
        

        if len(enemies) == 0:
            level += 1
            wave_length += 9
            for enemy_amount in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH - 100), random.randrange(-1200, -100), random.choice(["Enemy 1", "Enemy 2", "Enemy 3"]))
                enemies.append(enemy)
    

        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                Start = False
        controls = pygame.key.get_pressed()
        if controls[pygame.K_LEFT] and player.x - movement > 0 or controls[pygame.K_a] and player.x - movement > 0: 
            player.x -= movement # left and blocks me from going off the screen
        if controls[pygame.K_RIGHT] and player.x + movement + player.get_width() < WIDTH or controls[pygame.K_d] and player.x + movement + player.get_width() < WIDTH:
            player.x += movement # right and and blocks me from going off the screen
        if controls[pygame.K_UP] and player.y - movement > 0 or controls[pygame.K_w] and player.y - movement > 0:
            player.y -= movement # up and and blocks me from going off the screen
        if controls[pygame.K_DOWN] and player.y + movement + player.get_height() < HEIGHT  or controls[pygame.K_s] and player.y + movement + player.get_height() < HEIGHT:
            player.y += movement # down and and blocks me from going off the screen

        for enemy in enemies:
            enemy.move(enemies_movement)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
        redraw_window()


StartGame()
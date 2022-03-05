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


ENEMY_SPACE_SHIP1 = pygame.image.load(os.path.join("Images", "Enemies", "enemy_ship_1.png" ))
ENEMY_SPACE_SHIP2 = pygame.image.load(os.path.join("Images","Enemies", "enemy_ship_2.png" ))
ENEMY_SPACE_SHIP3 = pygame.image.load(os.path.join("Images", "Enemies", "enemy_ship_3.png" ))

# player player
USER_SPACE_SHIP = pygame.image.load(os.path.join("Images", "space_ship.png" ))


RED_lASER = pygame.image.load(os.path.join("Images", "Guns", "laser_red.png" ))
GREEN_LASER = pygame.image.load(os.path.join("Images", "Guns", "laser_green.png" ))
BLUE_LASER = pygame.image.load(os.path.join("Images", "Guns", "laser_blue.png" ))
YELLOW_LASER = pygame.image.load(os.path.join("Images", "Guns", "laser_yellow.png" ))


BG = pygame.transform.scale(pygame.image.load(os.path.join("Images", "space_background.jpg" )), (WIDTH, HEIGHT))

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

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = USER_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img) # collusion
        self.max_health = health 

    def move_lasers(self, movement, Objects):
        self.cooldown()
        for laser in self.lasers:
            laser.move(movement)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for object in Objects:
                    if laser.collision(object):
                        Objects.remove(object)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)
    
    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


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

    def shoot(self):
        if self.laser_countdown == 0:
            laser = Laser(self.x - 20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.laser_countdown = 1


def collide(object1, object2):
    offset_x = object2.x - object1.x
    offset_y = object2.y - object1.y
    return object1.mask.overlap(object2.mask, (offset_x, offset_y)) != None


def StartGame():
    global FPS
    Start = True
    level = 0
    lives = 3
    movement = 5 
    laser_movement = 4

    font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 10
    enemies_movement = 1
    player = Player(300, 650)

    Clock = pygame.time.Clock()


    game_over = False

    lost_count = 0


    def redraw_window():
        SCREEN.blit(BG, (0,0))

        lives_label = font.render(f"Lives: {lives}", 1, (WHITE))
        level_label = font.render(f"Level: {level}", 1, (WHITE))


        SCREEN.blit(lives_label, (10, 10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(SCREEN)


        player.draw(SCREEN)
        

        if game_over == True:
            lost_text = lost_font.render("You Lost!!", 1, (255, 255, 255))
            SCREEN.blit(lost_text, (WIDTH / 2 - level_label.get_width() / 2, 350))

        pygame.display.update()



    while Start == True:
        Clock.tick(FPS)
        redraw_window()


        if lives <= 0 or player.health <= 0:
            game_over = True
            lost_count += 1


        if game_over == True:
            if lost_count > FPS * 3:
                Start = False
            else:
                continue
        

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
        if controls[pygame.K_DOWN] and player.y + movement + player.get_height() + 20 < HEIGHT or controls[pygame.K_s] and player.y + movement + player.get_height() + 20 < HEIGHT :
            player.y += movement # down and and blocks me from going off the screen
        if controls[pygame.K_SPACE]:
            player.shoot()

        
        for enemy in enemies:
            enemy.move(enemies_movement)
            enemy.move_lasers(laser_movement, player)

            if random.randrange(0, 120) == 1:
                enemy.shoot()
            
            
            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_movement, enemies)



def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run_menu = True
    while run_menu == True:
        SCREEN.blit(BG, (0, 0))
        title_text = title_font.render("Press the mouse to begin... ", 1, (255, 255, 255))
        SCREEN.blit(title_text, (WIDTH / 2 - title_text.get_width()/2, 350))
        pygame.display.update()
        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                run_menu = False
            if window.type == pygame.MOUSEBUTTONDOWN:
                StartGame()
    pygame.quit()


main_menu()
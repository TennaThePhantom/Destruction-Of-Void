import pygame
from pygame.locals import *
from SpaceGameVariables import *
from Levels import *


pygame.mixer.init()

pygame.font.init()

MUSIC = pygame.mixer.music.load('SpaceShootermusic.ogg')



def gamelevels(level):

    level1(level)

    level2(level)

    level3(level)

    level4(level)

    level5(level)

    level6(level)

    level7(level)

    level8(level)

    level9(level)

    level10(level)

    level11(level)

    level12(level)

    level13(level)

    level14(level)

    level15(level)

    level16(level)

    level17(level)

    level18(level)

    level19(level)

    level20(level)

    level21(level)

    level22(level)

    level23(level)

    level24(level)

    level25(level)

    level26(level)

    level27(level)

    level28(level)

    level29(level)

    level30(level)





def player_controls():
    global enemies
    global Guns_movement
    global movement
    controls = pygame.key.get_pressed()
    if controls[pygame.K_LEFT] and player.x - movement > 0 or controls[pygame.K_a] and player.x - movement > 0: 
        player.x -= movement # left and blocks me from going off the screen
    if controls[pygame.K_RIGHT] and player.x + movement + player.get_width() < WIDTH or controls[pygame.K_d] and player.x + movement + player.get_width() < WIDTH:
        player.x += movement # right and and blocks me from going off the screen
    if controls[pygame.K_UP] and player.y - movement > 0 or controls[pygame.K_w] and player.y - movement > 0:
        player.y -= movement # up and and blocks me from going off the screen
    if controls[pygame.K_DOWN] and player.y + movement + player.get_height() + 35 < HEIGHT or controls[pygame.K_s] and player.y + movement + player.get_height() + 35 < HEIGHT :
        player.y += movement # down and and blocks me from going off the screen
    if controls[pygame.K_SPACE]:
        player.shoot() 

    player.move_lasers(-Guns_movement, enemies)


def StartGame():
    global enemies
    global movement
    global Guns_movement
    game_over = False
    start_game = True
    won_game = False
    lost_count = 0
    won_count = 0
    FPS = 60
    level = 0
    pygame.mixer.music.play(-1)


    Clock = pygame.time.Clock()


    def redraw_window():
        SCREEN.blit(BG, (0, 0))

        font = pygame.font.SysFont("comicsans", 50)
        game_over_font = pygame.font.SysFont("Comicsans", 60)
        won_game_font = pygame.font.SysFont("Comicsans", 55)


        level_label = font.render(f"Level: {level}", 1, (WHITE))

        SCREEN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(SCREEN)


        for enemy in enemies:
            enemy.draw(SCREEN)

        if game_over == True:
            game_over_text = game_over_font.render("You Lost!!", 1, WHITE)
            SCREEN.blit(game_over_text, (WIDTH / 2 - level_label.get_width() / 2, 350))

        if won_game == True:
            won_game_text = won_game_font.render("You survived all 30 waves congratulations !!", 1, WHITE)
            SCREEN.blit(won_game_text, (WIDTH / 2 - level_label.get_width() / 2 - 450, 350))

        pygame.display.update()


    
    while start_game == True:
        Clock.tick(FPS)
        redraw_window()

        if player.health <= 0:
            game_over = True
            lost_count += 1

        if game_over == True:
            if lost_count > FPS * 3:
                start_game = False
                player.max_health = 250
                player.health = 250
            for enemy in enemies:
                enemies.remove(enemy)
            for lasers in player.lasers:
                player.lasers.remove(lasers)
            else:
                continue

        if level == 31:
            won_game = True
            won_count += 1
        if won_game == True:
            if won_count > FPS * 4:
                start_game = False
                pygame.mixer.music.stop()
            else:
                continue


        player_controls()
    
        if len(enemies) == 0:
            level += 1
            if level == 1:
                Guns_movement = 4
                movement = 5.5
                player.health = 250
                player.max_health = 250
                player.ship_img = USER_SPACE_SHIP
                player.laser_img = YELLOW_LASER
            if level == 5:
                player.health += 150
                player.max_health += 150
                movement = 5.8
                Guns_movement = 4.1
                player.COOLDOWN = 28
            if level == 8:
                player.laser_img = RED_lASER
            if level == 10:
                player.health += 200
                player.max_health += 200
                movement = 5.9
                Guns_movement = 4.4
                player.COOLDOWN = 26
                player.ship_img = USER_SPACE_SHIP2
            if level == 13:
                player.health += 250
                player.max_health += 250
                movement = 6.1
                Guns_movement = 4.5
            if level == 15:
                player.laser_img = BLUE_AND_DARKBLUE_lASER
                player.health += 150
                player.max_health += 150

            if level == 17:
                player.health = 900
                player.max_health = 900
                movement = 6.3
                Guns_movement = 4.6
            if level == 20:
                movement = 6.5
                Guns_movement = 4.5
                player.COOLDOWN = 21
                player.health += 175
                player.max_health += 175
                player.ship_img = USER_SPACE_SHIP3
            if level == 22:
                player.laser_img = RED_ENERGY_BLAST
            if level == 23:
                movement = 6.7
                Guns_movement = 4.8
                player.COOLDOWN = 18
            if level == 24: 
                player.health = 1400
                player.max_health = 1400
            if level == 25:
                movement = 7
                Guns_movement = 5
                player.COOLDOWN = 15
            if level == 27:
                player.health += 100
                player.max_health += 100
            



        if level == 0:
            for enemy in enemies:
                enemies.remove(enemy)
            for lasers in player.lasers:
                player.lasers.remove(lasers)
        gamelevels(level)

        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                start_game = False
                level = 0
                pygame.mixer.music.stop()
    





def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)
    goal_font =  pygame.font.SysFont("comicsans", 50)
    waves_harder_font = pygame.font.SysFont("comicsans", 50)
    ship_upgrades_font = pygame.font.SysFont("comicsans", 50)
    run_menu = True
    while run_menu == True:
        SCREEN.blit(BG, (0, 0))
        goal_text = goal_font.render("Your goal is to get to wave 30 without dieing", 1, WHITE)
        SCREEN.blit(goal_text, (WIDTH / 2 - goal_text.get_width()/2, 50))

        waves_text = waves_harder_font.render("as waves go up it will get harder", 1, WHITE)
        SCREEN.blit(waves_text, (WIDTH / 2 - waves_text.get_width()/2, 150))

        upgrades_text = ship_upgrades_font.render("Your ship will get upgrades as you play", 1, WHITE)
        SCREEN.blit(upgrades_text, (WIDTH / 2 - upgrades_text.get_width()/2, 259))

        title_text = title_font.render("Press the mouse to begin... ", 1, WHITE)
        SCREEN.blit(title_text, (WIDTH / 2 - title_text.get_width()/2, 350))


        pygame.display.update()
        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                run_menu = False
            if window.type == pygame.MOUSEBUTTONDOWN:
                StartGame()
    pygame.quit()



main_menu()

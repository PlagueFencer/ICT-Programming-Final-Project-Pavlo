import random
import os
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT


# Alustaa Pygame-kirjaston
pygame.init()

FPS = pygame.time.Clock()

# Määrittää ikkunan korkeuden ja leveyden
HEIGHT = 900
WIDTH = 900

# Määrittää fontin
FONT = pygame.font.SysFont('Verdana', 20)

# Määrittää värit
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)

# Luo pääikkunan
main_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Lataa taustakuvan ja skaalaa sen ikkunan kokoa vastaavaksi
bg = pygame.transform.scale(pygame.image.load('JamScrollsBG.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3


# Määrittää polun pelaajan kuville
IMAGE_PATH = "goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

# Määrittää pelaajan koon ja lataa pelaajan kuvan
player_size = (20, 20)
player = pygame.image.load('player.png').convert_alpha()
player_rect = player.get_rect()
player_rect.center = main_display.get_rect().center

# Määrittää pelaajan liikkeet

# player_speed = [1, 1]
player_move_down = [0, 4]
player_move_up = [0, -4]
player_move_right = [4, 0]
player_move_left = [-4, 0]


# Luo vihollisen
def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha() # pygame.Surface(enemy_size)
    enemy_rect = pygame.Rect(WIDTH,
                            random.randint(enemy.get_height(), HEIGHT - enemy.get_height()), 
                            *enemy.get_size())
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]

# Luo bonuksen
def create_bonus():
    bonus = pygame.image.load('bonus.png').convert_alpha() # pygame.Surface(bonus_size)
    bonus_width = bonus.get_width()
    bonus_rect = pygame.Rect(random.randint(bonus_width, WIDTH - bonus_width),
                            -bonus.get_height(),
                            *bonus.get_size())
    bonus_move = [0, random.randint(4, 8)]
    return [bonus, bonus_rect, bonus_move]

# Asettaa tapahtumat vihollisen ja bonusten luomiselle ja kuvan vaihtamiselle
CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 3000)

CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)


# Luo listat vihollisille ja bonuksille
enemies = []

bonuses = []

# Asettaa pisteet nollaan
score = 0

# Asettaa alkuindeksin pelaajan kuville
image_index = 0

# Asettaa pelin käyntiin
playing = True


# Pääsilmukka
while playing:
    FPS.tick(60) # Asettaa FPS arvoksi 60
    
    for event in pygame.event.get(): # Käy läpi kaikki tapahtumat
        if event.type == QUIT: # Jos tapahtuma on QUIT, lopettaa pelin
            playing = False
        if event.type == CREATE_ENEMY: # Jos tapahtuma on CREATE_ENEMY, lisää uuden vihollisen
            enemies.append(create_enemy())
        if event.type == CREATE_BONUS: # Jos tapahtuma on CREATE_BONUS, lisää uuden bonuksen
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE: # Jos tapahtuma on CHANGE_IMAGE, vaihtaa pelaajan kuvan
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
            image_index += 1
            if image_index >= len(PLAYER_IMAGES): # Jos indeksin arvo ylittää kuvien määrän, nollaa indeksin
                image_index = 0
            
    # Siirtää taustakuvaa        
    bg_X1 -= bg_move
    bg_X2 -= bg_move
    
    if bg_X1 < -bg.get_width(): # Jos taustakuva ylittää ikkunan leveyden, nollaa X1
        bg_X1 = bg.get_width()
        
    if bg_X2 < -bg.get_width(): # Jos taustakuva ylittää ikkunan leveyden, nollaa X2
        bg_X2 = bg.get_width()
    
    main_display.blit(bg, (bg_X1, 0)) # Piirtää taustakuvan
    main_display.blit(bg, (bg_X2, 0))
    
    keys = pygame.key.get_pressed() # Tarkistaa painetut näppäimet
    
    if keys[K_DOWN] and player_rect.bottom < HEIGHT: # Jos K_DOWN on painettu ja pelaaja ei ylitä ikkunan alareunaa, siirtää pelaajaa alaspäin
        player_rect = player_rect.move(player_move_down)
        
    if keys[K_UP] and player_rect.top > 0: # Jos K_UP on painettu ja pelaaja ei ylitä ikkunan yläreunaa, siirtää pelaajaa ylöspäin
        player_rect = player_rect.move(player_move_up)
        
    if keys[K_RIGHT] and player_rect.right < WIDTH: # Jos K_RIGHT on painettu ja pelaaja ei ylitä ikkunan oikeaa reunaa, siirtää pelaajaa oikealle
        player_rect = player_rect.move(player_move_right)
        
    if keys[K_LEFT] and player_rect.left > 0: # Jos K_LEFT on painettu ja pelaaja ei ylitä ikkunan vasenta reunaa, siirtää pelaajaa vasemmalle
        player_rect = player_rect.move(player_move_left)
        
    for enemy in enemies: # Käy läpi kaikki viholliset
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
        
        if player_rect.colliderect(enemy[1]): # Jos pelaaja törmää viholliseen, lopettaa pelin
            playing = False
        
    for bonus in bonuses: # Käy läpi kaikki bonukset
        bonus[1] = bonus[1].move(bonus[2])
        main_display.blit(bonus[0], bonus[1])
        
        if player_rect.colliderect(bonus[1]): # Jos pelaaja törmää bonukseen, lisää pisteen ja poistaa bonuksen
            score += 1
            bonuses.pop(bonuses.index(bonus))
        
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20)) # Piirtää pisteet näytölle
    main_display.blit(player, player_rect) # Piirtää pelaajan näytölle
    
    pygame.display.flip() # Päivittää näytön
    
    for enemy in enemies:  # Käy läpi kaikki viholliset
        if enemy[1].right < 0: # Jos vihollinen ylittää ikkunan vasemman reunan, poistaa vihollisen
            enemies.pop(enemies.index(enemy))
            
    for bonus in bonuses: # Käy läpi kaikki bonukset
        if bonus[1].top > HEIGHT: # Jos bonus ylittää ikkunan alareunan, poistaa bonuksen
            bonuses.pop(bonuses.index(bonus))
    
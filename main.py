import pygame as pg
import sys
from player import *
from raycasting import *


size = RES_X, RES_Y
MAP_SIZE = 20
TILE_SIZE = int((RES_X / 2) / MAP_SIZE)

window = pg.display.set_mode((size))


# map = [
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#     [1,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,1],
#     [1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
#     [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
#     [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,2,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,1],
#     [1,0,0,2,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
#     [1,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,1],
#     [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#     ]

map =  [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1],
    [1,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,1],
    [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]




# initialisation
pg.init()
pg.mouse.set_visible(False)
pg.event.set_grab(True)    #Pour que la souris ne sorte pas de l'écran


# Sortie et fin de jeu
clock = pg.time.Clock()

player = Player(8,11)



while True :
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
    
    window.fill((0,0,0))

    frame_time = clock.tick()
    player.movement(frame_time, map)
    raycasting(window, map, player)      
    pg.display.flip()
    # pg.display.update()
    pg.display.set_caption("GAME STUDIO FPS : " + str(int(clock.get_fps())))


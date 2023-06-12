import pygame as pg
import math as m
from constants import *

g_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]       
]

pg.init()
screen = pg.display.set_mode(SCREEN)
clock = pg.time.Clock()

def draw_map():
    global PLAYER_X,PLAYER_Y,TILE_SIZE,PLAYER_ANGLE,FOV

    for row in range(10):
        for col in range(10):
            
            if g_map[row][col] == 1:
                pg.draw.rect(screen,(150,0,0),(col*TILE_SIZE,row*TILE_SIZE,TILE_SIZE-2,TILE_SIZE-2))
            else:
                pg.draw.rect(screen,(255,0,0),(col*TILE_SIZE,row*TILE_SIZE,TILE_SIZE-2,TILE_SIZE-2))


    pg.draw.circle(screen,(255,255,0),(int(PLAYER_X),int(PLAYER_Y)),8)
    # pg.draw.line(screen,(0,0,255),(PLAYER_X,PLAYER_Y),(PLAYER_X - m.sin(PLAYER_ANGLE)*50,PLAYER_Y - m.cos(PLAYER_ANGLE)*50),3)
    # pg.draw.line(screen,(0,0,255),(PLAYER_X,PLAYER_Y),(PLAYER_X - m.sin(PLAYER_ANGLE - FOV)*50,PLAYER_Y - m.cos(PLAYER_ANGLE - FOV)*50),3)
    # pg.draw.line(screen,(0,0,255),(PLAYER_X,PLAYER_Y),(PLAYER_X - m.sin(PLAYER_ANGLE + FOV)*50,PLAYER_Y - m.cos(PLAYER_ANGLE + FOV)*50),3)

def cast_ray():
    global PLAYER_X,PLAYER_Y,TILE_SIZE,PLAYER_ANGLE,FORWARD,FOV,STEP_ANGLE,MAX_DEPTH,SCREEN_HEIGHT,SCREEN_WIDTH

    start_angle = PLAYER_ANGLE - FOV

    for ray in range(RAYS):
        for depth in range(MAX_DEPTH):
            target_x = PLAYER_X - m.sin(start_angle) * depth
            target_y = PLAYER_Y + m.cos(start_angle) * depth
            col = int(target_x/TILE_SIZE)
            row = int(target_y/TILE_SIZE)
            if g_map[row][col] == 1:
                pg.draw.rect(screen,(0,255,0),(col*TILE_SIZE,row*TILE_SIZE,TILE_SIZE-2,TILE_SIZE-2))

                pg.draw.line(screen,(0,0,255),(int(PLAYER_X),int(PLAYER_Y)),(target_x,target_y))


                color = 50 / (1 + depth * depth * 0.0001)  

                depth *= math.cos(PLAYER_ANGLE - start_angle)

                wall_height = 21000 / (depth + 0.0001)

                if wall_height > SCREEN_HEIGHT :
                    wall_height = SCREEN_HEIGHT
                    pg.draw.rect(screen,(color,color,color),(SCREEN_HEIGHT + ray * SCALE ,SCREEN_HEIGHT/2 - wall_height/2 , SCALE , wall_height))
                    break

        start_angle += STEP_ANGLE
     
def check_events():
    global PLAYER_X,PLAYER_Y,TILE_SIZE,PLAYER_ANGLE,FORWARD

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                PLAYER_ANGLE -= 0.1
            if event.key == pg.K_d:
                PLAYER_ANGLE += 0.1
            if event.key == pg.K_w:
                FORWARD = True
                PLAYER_X += -m.sin(PLAYER_ANGLE)*5
                PLAYER_Y +=  m.cos(PLAYER_ANGLE)*5

            if event.key == pg.K_s:
                FORWARD = False
                PLAYER_X += -m.sin(PLAYER_ANGLE)*5
                PLAYER_Y +=  m.cos(PLAYER_ANGLE)*5

def projection():
    global PLAYER_X,PLAYER_Y,TILE_SIZE,PLAYER_ANGLE,FORWARD
    print(PLAYER_X)
    col = int(PLAYER_X / TILE_SIZE)
    row = int(PLAYER_Y / TILE_SIZE)
 

    if g_map[row][col] == 1:
            if FORWARD == True:
                PLAYER_X -= -math.sin(PLAYER_ANGLE) * 5
                PLAYER_Y -= math.cos(PLAYER_ANGLE) * 5
            else:
                PLAYER_X += -math.sin(PLAYER_ANGLE) * 5
                PLAYER_Y += math.cos(PLAYER_ANGLE) * 5
 
     
          
    pg.draw.rect(screen,(0,0,0),(0,0,SCREEN_HEIGHT,SCREEN_HEIGHT))
    pg.draw.rect(screen,(100,0,0),(480,SCREEN_HEIGHT / 2,SCREEN_HEIGHT,SCREEN_HEIGHT))
    pg.draw.rect(screen,(200,0,0),(480,-SCREEN_HEIGHT / 2,SCREEN_HEIGHT,SCREEN_HEIGHT))      
    
while True:
    screen.fill('black')
    # draw_map()
    cast_ray()

    projection()
    check_events()
    pg.display.update()



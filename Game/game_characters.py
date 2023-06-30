import pygame as pg
from game_settings import *
from game_map import *
import math

class Player():
    def __init__(self,game):
        pg.init()
        self.x,self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.game =game


    def movement(self):
        dx = PLAYER_SPEED * math.cos(self.angle) * self.game.delta_time
        dy = PLAYER_SPEED * math.sin(self.angle)* self.game.delta_time

        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_w:
                self.move_or_not(dx,dy)
            if event.type == pg.KEYDOWN and event.key == pg.K_d:
                self.move_or_not(-dy,dx)
            if event.type == pg.KEYDOWN and event.key == pg.K_s:
                self.move_or_not(-dx,-dy)
            if event.type == pg.KEYDOWN and event.key == pg.K_a:
                self.move_or_not(dy,-dx)
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                self.angle -=  PLAYER_ROT_SPEED * self.game.delta_time
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                self.angle +=  PLAYER_ROT_SPEED * self.game.delta_time
        

        self.angle %= math.tau

    def update(self):
        self.movement()
    
    def check_collision_walls(self,x,y):
        return (x,y) not in self.game.map.world_map
    
    def move_or_not(self,dx,dy):
        
        if (self.check_collision_walls(int(self.x + dx),int(self.y))):
            self.x += dx
            
        if (self.check_collision_walls(int(self.x),int(self.y + dy))):
            self.y += dy
    
    def draw(self):
        pg.draw.circle(self.game.screen,'blue',(WIDTH + self.x*MAP_TILE,self.y*MAP_TILE),8)

    @property
    def pos(self):
        return self.x,self.y 
    
    @property
    def map_pos(self):
        return int(self.x),int(self.y) 
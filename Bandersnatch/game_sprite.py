import pygame as pg
from settings import *
import math
class Sprite:
    def __init__(self,game):
        self.game = game
        self.x,self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx,dy = 0,0
        speed = PLAYER_SPEED * self.game.delta_time

        speed_sin = speed*sin_a
        speed_cos = speed*cos_a

        



    def draw(self):
        pg.draw.rect(self.game.screen,self.block_clr,pg.Rect(self.x*self.rect,self.y*self.rect, self.rect, self.rect),2)

    def update(self):
        for event in pg.event.get():
            # checking if keydown event happened or not
            if event.type == pg.KEYDOWN:
                # checking if key "W" was pressed
                if (event.key == pg.K_w and self.w_update):
                    self.y -= self.speed 
                # checking if key "A" was pressed
                if (event.key == pg.K_a and self.a_update):
                    self.x -= self.speed
                # checking if key "S" was pressed
                if (event.key == pg.K_s and self.s_update):
                    self.y += self.speed
                # checking if key "D" was pressed
                if (event.key == pg.K_d and self.d_update):
                    self.x += self.speed

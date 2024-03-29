import pygame as pg
from game_settings import *

mini_map = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1],
        [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1]]
        # [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1],
        # [1,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1],
        # [1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1],
        # [1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1],
        # [1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1],
        # [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1],
        # [1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,1],
        # [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

class Map():
    def __init__(self,game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.gen_world_map()

    def gen_world_map(self):
        for i,row in enumerate(mini_map):
            for j,value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value

    def draw(self):
        for pos in self.world_map:  
            pg.draw.rect(self.game.screen,'red',pg.Rect(WIDTH + pos[0]*MAP_TILE,pos[1]*MAP_TILE, MAP_TILE, MAP_TILE),5) 


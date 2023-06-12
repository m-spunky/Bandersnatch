import pygame as pg


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

# pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))

class Map:
    def __init__(self,game):
        self.game = game
        self.g_map = g_map
        self.world_map = {}
        self.block_clr = (255,0,0)
        self.gen_world_map()
        self.rect = 50

    def draw_rect(self):
        [pg.draw.rect(self.game.screen,self.block_clr,pg.Rect(pos[0]*self.rect, pos[1]*self.rect, self.rect, self.rect),2) for pos in self.world_map]

    def gen_world_map(self):
        for a,row in enumerate(self.g_map):
            for b,value in enumerate(row):
                if (value==1):
                    self.world_map[(a,b)] = value

    

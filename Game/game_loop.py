import pygame as pg
from game_settings import *
from game_map import *
from game_characters import *
from game_engine import *
from game_renderer import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.obj_renderer = ObjectRenderer(self) 
        self.engine = Raycaster(self)
        

    def update(self):
        self.player.update()
        self.engine.update()
        
        pg.display.flip()        
        self.delta_time = self.clock.tick(FPS)
        

    def draw(self):
        # self.screen.fill((0,0,255/(1+self.engine.depth ** 3 * 0.00002)),(0,HALF_HIGHT,WIDTH,HALF_HIGHT))
        # self.screen.fill((0,255/(1+self.engine.depth ** 3 * 0.00002),0),(0,0,WIDTH,HALF_HIGHT))
        # self.screen.fill('black',(WIDTH,0,F_WIDTH-WIDTH,HEIGHT))
        self.screen.fill('black',(0,0,F_WIDTH,HEIGHT))
        self.obj_renderer.draw()
        # self.map.draw()
        # self.player.draw()


    def run(self):
        while True:
            self.update()
            self.draw()

g = Game()
g.run()




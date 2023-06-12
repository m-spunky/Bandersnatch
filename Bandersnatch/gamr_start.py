import pygame as pg
import sys
from settings import *
from game_map import *
from game_sprite import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.sprite = Sprite(self)

    def update(self):
        pg.display.update()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps()}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw_rect()
        self.sprite.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
    
    def check_collisions(self):
        pass
        


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.sprite.update()
            self.check_collisions()



game = Game()
game.run()









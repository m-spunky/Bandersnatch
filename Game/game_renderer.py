import pygame as pg
from game_settings import *

class ObjectRenderer:
    def __init__(self,game):
        pg.init()
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_object()

    def render_object(self):
        list_objects = self.game.engine.object_to_render
        for depth , wall_strip , wall_pos in list_objects:
            self.screen.blit(wall_strip,wall_pos)



        

    @staticmethod
    def get_texture(path,res=(TEXTURE_SIZE,TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture,res)
    
    def load_wall_textures(self):
        return {1:self.get_texture('textures/1.jpg')
            # ,2:self.get_texture('textures/2.png')
            # ,3:self.get_texture('textures/3.png')
            # ,4:self.get_texture('textures/4.png')
            }


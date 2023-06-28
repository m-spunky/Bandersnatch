import pygame as pg
from game_settings import *

class Raycaster:
    def __init__(self,game):
        pg.init()
        self.game = game
        self.depth = 1

    def update(self):
        self.raycast()

    def raycast(self):
        ox,oy = self.game.player.pos
        x_map,y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.00001
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

        # Horizontal intersect
            y_hor , dy = (y_map+1,1) if sin_a > 0 else (y_map- 1e-6,-1)            
            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor *cos_a
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a
            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor),int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth



        # Vertical intersect
            x_vert , dx = (x_map+1,1) if cos_a > 0 else (x_map- 1e-6,-1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert *sin_a
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a
            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert),int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth


        # Optimum Depth 
            if depth_vert>depth_hor:
                depth = depth_hor
            else:
                depth = depth_vert

        # Fishbowl correction
            self.depth = depth
            depth *= math.cos(self.game.player.angle - ray_angle)
        
        # Projected Height
            proj_height = SCREEN_DIST / depth
            f = 255 - (depth * 7)
            color = (f,f,f)
            
        # Draw Walls
            pg.draw.rect(self.game.screen,color,pg.Rect(ray*SCALE , HALF_HIGHT - proj_height//WALL_Y_OFFSET,SCALE,proj_height + WALL_HEIGHT_OFFSET ))
            pg.draw.line(self.game.screen,'yellow',(WIDTH + MAP_TILE*ox,MAP_TILE*oy),(WIDTH + MAP_TILE * ox + MAP_TILE * depth * cos_a,MAP_TILE * oy + MAP_TILE * depth * sin_a),3)

        # Next Angle
            ray_angle += DELTA_ANGLE




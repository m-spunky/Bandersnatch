import pygame as pg
from game_settings import *

class Raycaster:
    def __init__(self,game):
        pg.init()
        self.game = game
        self.depth = 1
        self.raycast_results = []
        self.object_to_render = []
        self.textures = self.game.obj_renderer.wall_textures
        
    def update(self):
        self.raycast()
        self.get_object_to_render()

    def get_object_to_render(self):
        self.object_to_render = []
        for ray,value in enumerate(self.raycast_results):
            
            depth , proj_height, texture , offset = value

            wall_strip = self.textures[texture].subsurface(
                offset * (TEXTURE_SIZE - SCALE),0,SCALE,TEXTURE_SIZE
            )
            wall_strip = pg.transform.scale(wall_strip,(SCALE,int(proj_height+ WALL_HEIGHT_OFFSET )))
            
            
            wall_pos = (ray *SCALE,HALF_HIGHT-proj_height//WALL_Y_OFFSET)
            self.object_to_render.append((depth,wall_strip,wall_pos))
            
# (ray*SCALE , HALF_HIGHT - proj_height//WALL_Y_OFFSET,SCALE,proj_height + WALL_HEIGHT_OFFSET )

    def raycast(self):
        self.raycast_results = []
        ox,oy = self.game.player.pos
        x_map,y_map = self.game.player.map_pos
        tex_vert , tex_hor = 1,1

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
                    tex_hor = self.game.map.world_map[tile_hor]
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
                    tex_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth


        # Optimum Depth 
            if depth_vert>depth_hor:
                depth,texture = depth_hor,tex_hor
                x_hor %= 1
                offset = (1-x_hor) if sin_a>0 else x_hor
            else:
                depth,texture = depth_vert,tex_vert
                y_vert %= 1
                offset = y_vert if cos_a>0 else (1-x_vert)

        # Fishbowl correction
            self.depth = depth
            depth *= math.cos(self.game.player.angle - ray_angle)
        
        # Projected Height
            proj_height = SCREEN_DIST / depth
            color = [255/(1+depth ** 5 * 0.00002)] * 3
            
        
            
        # Draw Walls
            # print(ray*SCALE)
            # pg.draw.rect(self.game.screen,'red',(ray*SCALE , HALF_HIGHT - proj_height//WALL_Y_OFFSET,SCALE,proj_height + WALL_HEIGHT_OFFSET ),int(1))

            pg.draw.line(self.game.screen,'yellow',(WIDTH + MAP_TILE*ox,MAP_TILE*oy),(WIDTH + MAP_TILE * ox + MAP_TILE * depth * cos_a,MAP_TILE * oy + MAP_TILE * depth * sin_a),3)

            # 
            self.raycast_results.append((depth , proj_height, texture , offset))
            # print(depth , proj_height, texture , offset)
        # Next Angle
            
            ray_angle += DELTA_ANGLE



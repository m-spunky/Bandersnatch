import math

FULL_RES = (F_WIDTH,F_HEIGHT) = (1250,600)

RES = (WIDTH,HEIGHT) = (600,400)
HALF_WIDTH , HALF_HIGHT = WIDTH//2 , HEIGHT//2
FPS = 0

MAP_TILE = 20

PLAYER_POS = 1,1
PLAYER_ANGLE = 45
PLAYER_SPEED = 0.04
PLAYER_ROT_SPEED = 0.02


FOV = math.pi / 3
HALF_FOV = FOV / 2

NUM_RAYS = WIDTH // 2 
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20


SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH //NUM_RAYS

WALL_Y_OFFSET = 2.3
WALL_HEIGHT_OFFSET = 60



TEXTURE_SIZE = 256
import pygame
import os
import random

WIDTH_SCREEN = 500
HEIGHT_SCREEN = 800

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('img','pipe.png')))
FLOOR_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('img','bg.png')))
BACKGROUD = pygame.transform.scale2x(pygame.image.load(os.path.join('img','base.png')))
BIRDS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('img','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img','bird3.png'))),
]

pygame.font.init()
POINTS_FONTS = pygame.font.SysFont('robot',50)

class Bird:
    IMGS = BIRDS
    # animação da rotação do passaro 
    MAX_ROTATION = 25 
    MAX_SPEED = 20
    TIME_ANIMATION = 5
    
    def __init__(self,x,y):
        #  
        self.x = x
        self.y = y
        self.tilt = 0
        self.velocity = 0
        self.height = self.y
        self.time = 0
        self.image_count = 0
        self.image = IMGS[0]
        
        
class Pipe:
    pass

class floor:
    pass

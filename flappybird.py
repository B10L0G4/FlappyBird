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
    pass

class Pipe:
    pass

class floor:
    pass

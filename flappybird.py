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
        self.image = self.IMGS[0]
 #cima = -y  baixa = +y  esquerda =-x  direita = +x
    
    def jump(self):
        self.velocity = -10.5
        self.time = 0
        self.height = self.y
    
    def move(self):
        #calcular deslocamento 
        

        self.time += 1
        displacement = self.velocity * self.time + 1.5 * self.time ** 2 # 1.5 * (self.time ** 2) + self.velocity * self.time

           
        # restringir o deslocamento
        if displacement >= 16:
            displacement = 16
        elif displacement < 0: #testar sem depois , torna o jogo mais facil e dinamico
            displacement -= 2
        self.y = self.y + displacement
        
        # angulo do passaro   
        if displacement < 0 or self.y < (self.height + 50): #testar sem parenteses #posição para inclinação da animação do passaro
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90: #rotacionado para baixo, queda
                self.tilt -= self.MAX_ROTATION
                
                # ----
        # self.image_count += 1
        # if self.image_count < self.TIME_ANIMATION:
        #     self.image = self.IMGS[0]
        # elif self.image_count < self.TIME_ANIMATION * 2:
        #     self.image = self.IMGS[1]
    def drawing(self,screen):
        #definir imagem 
        self.image_count += 1
        if self.image_count < self.TIME_ANIMATION:
            self.image = self.IMGS[0]
        elif self.image_count < self.TIME_ANIMATION * 2:
            self.image = self.IMGS[1]
        elif self.image_count < self.TIME_ANIMATION * 3:
            self.image = self.IMGS[2]
        elif self.image_count < self.TIME_ANIMATION * 4:
            self.image = self.IMGS[1]
        elif self.image_count >= self.TIME_ANIMATION * 4 + 1:
            self.image = self.IMGS[0]
            self.image_count = 0
    
        # quando cair, para de bater asa 
        
        if self.tilt <= -80:
            self.image = self.IMGS[1]
            self.image_count = self.TIME_ANIMATION * 2
        
        #desenhae a imahgem
        
        image_rotate = pygame.transform.rotate(self.image, self.tilt)
        post_image_center= self.image.get_rect(topleft=(self.x,self.y)).center
        rectangle = pygame.Rect(center=post_image_center)
        screen.blit(image_rotate,rectangle.topleft)
        
    def gat_mask(self):
        pygame.mask.from_surface(self.image)
        
            
                                                   
            
        
class Pipe:
    pass
    
class floor:
    pass

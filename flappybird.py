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
    DISTANCE = 200
    VELOCITY = 5 
    
    def __init__(self,x):
        self.x = x
        self.height = 0 #random.randrange(50,450)
        self.top = 0 #self.height - PIPE_IMAGE.get_height()
        self.bottom = 0 #self.height + PIPE_IMAGE.get_height()
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE,False,True)
        self.PIPE_BOTTOM = PIPE_IMAGE
        self.PIPE_pass = False
        self.define_height()
    def define_height(self):
        self.height = random.randrange(50,450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.DISTANCE.get_height()
        
    def movePipe(self):
        self.x -= self.VELOCITY
    def drawPipe(self, screen):
        screen.blit(self.PIPE_TOP, (self.x, self.top))
        screen.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
        
    def collide(self,bird):
        bird_mask = bird.gat_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        top_point = bird_mask.overlap(top_mask,top_offset)
        base_point = bird_mask.overlap(bottom_mask,bottom_offset)
        
        if top_point or base_point:
            return True
        else:
            return False
        
        
class floor:
    VELOCITY = 50
    WIDTH_SCREEN = FLOOR_IMAGE.get_width()
    IMAGE = FLOOR_IMAGE
    
    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH_SCREEN
    
    def move_to(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY
        
        if self.x1 + self.WIDTH_SCREEN < 0:
            self.x1 = self.x1 + self.WIDTH_SCREEN
        if self.x2 + self.WIDTH_SCREEN < 0:
            self.x2 = self.x2 + self.WIDTH_SCREEN
            
    def draw_floor(self, screen):
        screen.blit(self.IMAGE, (self.x1, self.y))
        screen.blit(self.IMAGE, (self.x2, self.y))
        
def draw_screen(screen, bird,pipe, floor, points):
    screen.blit(BACKGROUD,(0,0))
    for birds in bird:
        birds.move()
        birds.drawing(screen)
    for pipes in pipe:
        pipes.drawPipe(screen)
    text = POINTS_FONTS.render(f'Point {points}',1, (255,255,255))
    screen.blit(text, (WIDTH_SCREEN -10 -text.get_width(),10))
    floor.draw(screen)
    pygame.display.update()
    
    
def main ():
    bird =[Bird(230,350)]
    flooor =[Flooor(730)]
    pipe =[Pipe(700)]
    screen = pygame.display.set_mode(WIDTH_SCREEN, HEIGHT_SCREEN)
    points = 0
    clock = pygame.time.Clock()

    start = True
    while start:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for birds in bird:
                        birds.jump()
                        
                
        draw_screen(screen, bird, pipe, floors,points)
      
    
    
    
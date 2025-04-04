import pygame
import os
import random

# Inicialização do Pygame
pygame.init()

WIDTH_SCREEN = 500 #tela largura
HEIGHT_SCREEN = 800 # tela altura 

PIPE_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('img','pipe.png'))) # imagem do cano 
FLOOR_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join('img','base.png'))) #imagem do chao 
BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('img','bg.png'))) # imagens do passaro 
BIRDS_IMAGE = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('img','bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img','bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('img','bird3.png'))),
]

pygame.font.init()
POINTS_FONTS = pygame.font.SysFont('robot', 50)

class Bird: # classe do passaro 
    '''
    Função para criar o passaro, definir a imagem ,velocidade e a animação 
    '''
    IMGS = BIRDS_IMAGE
    # # animação da rotação do passaro 
    MAX_ROTATION = 25 
    MAX_SPEED = 20 # valor padrao 20 
    TIME_ANIMATION = 5 # valor padrao 5 
    
    def __init__(self, x, y):
        self.x = x # posição do passaro em relação a tela
        self.y = y # altura do passaro em relação a tela
        self.tilt = 0 # angulo
        self.velocity = 0 # velocidade do passaro
        self.height = self.y # altura de y em 
        self.time = 0
        self.image_count = 0
        self.image = self.IMGS[0]
    
    def jump(self):
        self.velocity = -10.5 # velocidade padrão -10.5
        self.time = 0
        self.height = self.y
    
    def move(self):
        # calcular o deslocamento 
        self.time += 1 # faz com que o tempo aumente
        displacement = 1.5 * (self.time**2) + self.velocity * self.time # desloacamento do passaro em relação ao tempo
        #print('Deslocamento calculo',displacement)
        #restringir o deslocamento 
        if displacement > 16: # padra 16
            displacement = 14 #padrao 16
        elif displacement < -10: # padrao -10
            displacement -= -10 # padrao -10
        self.y += displacement
        
        #angulo do passaro 
        if displacement < 0 or self.y < (self.y + 50):
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.MAX_ROTATION
    
    def drawing(self, screen):
    #     #definir qual imagem o passaro vai usar 
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
    #      # se o passaro tiver caindo eu não vou bater asa
    
        if self.tilt <= -80:
            self.image = self.IMGS[1]
            self.image_count = self.TIME_ANIMATION * 2

    #     #desenhando a imagem 
        image_rotate = pygame.transform.rotate(self.image, self.tilt)
        post_image_center = self.image.get_rect(topleft=(self.x, self.y)).center
        rectangle = image_rotate.get_rect(center=post_image_center)
        screen.blit(image_rotate, rectangle.topleft)
        
    def get_mask(self): # 
        return pygame.mask.from_surface(self.image)      # 
        
class Pipe:
    '''
    Função para criar os canos, definir a altura e a velocidade do cano
    '''
    DISTANCE = 200 # distancia entre os canos
    VELOCITY = 5 # velocidade do cano
    
    def __init__(self, x):
        self.x = x # posição do cano
        self.height = 0 # altura do cano
        self.top = 0 # posição do cano de cima
        self.bottom = 0 # posição do cano de baixo
        
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMAGE, False, True) # imagem do cano de cima
        self.PIPE_BOTTOM = PIPE_IMAGE # imagem do cano de baixo
        self.PIPE_pass = False #
       # self.passed = False # variavel para verificar se o cano passou pelo passaro
        self.define_height() # define a altura do cano
    
    def drawPipe(self, screen):
        screen.blit(self.PIPE_TOP, (self.x, self.top))
        #print(f"Pipe top position: ({self.x}, {self.top})")
        screen.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
    
    def define_height(self): # define a altura do cano
        self.height = random.randrange(10, 750) # altura aleatoria do cano
        self.top = self.height - self.PIPE_TOP.get_height() # altura do cano em relação a tela de cima
        self.bottom = self.height + self.DISTANCE # altura do cano em relação a tela de baixo
        
    # def movePipe(self):
    #     self.x -= self.VELOCITY
    #     if self.x + self.PIPE_TOP.get_width() < 0:
    #         self.PIPE_pass = True
    #         return False
    #     return True
            

        
    # def collide(self, bird):
    #     bird_mask = bird.get_mask()
    #     top_mask = pygame.mask.from_surface(self.PIPE_TOP)
    #     bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
    #     top_offset = (self.x - bird.x, (self.top - round(bird.y))) #distancia do topo
    #     bottom_offset = (self.x - bird.x, (self.bottom - round(bird.y))) #distancia da base 
        
    #     print(f"Bird position: ({bird.x}, {bird.y})")
    #     print(f"Pipe top position: ({self.x}, {self.top})")
    #     print(f"Pipe bottom position: ({self.x}, {self.bottom})")
    #     print(f"Top offset: {top_offset}")
    #     print(f"Bottom offset: {bottom_offset}")
        
    #     top_point = bird_mask.overlap(top_mask, top_offset)
    #     base_point = bird_mask.overlap(bottom_mask, bottom_offset)

    #     print(f"Top point: {top_point}")
    #     print(f"Base point: {base_point}")
        
    #     if top_point or base_point:
    #         return True
    #     else:
    #         return False
        
class Floor:
    '''
    Função para criar o cenarios de fundo, chão e movimento do cenário/chão
    '''
    VELOCITY = 5 # velocidade de movimento do cenario
    WIDTH_SCREEN = FLOOR_IMAGE.get_width()
    IMAGE = FLOOR_IMAGE #define a imagem do chão
    
    def __init__(self, y): 
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH_SCREEN
    
    def move_to(self):
        # move o chao para a esquerda
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY
        
        # ajusta a repeticao do chao ,  quando o x1 é = a x2 ele repete o cenario e quando x2 é = 0 repete o cenario
        if self.x1 + self.WIDTH_SCREEN < 0: 
            self.x1 = self.x2 + self.WIDTH_SCREEN
        if self.x2 + self.WIDTH_SCREEN < 0:
            self.x2 = self.x1 + self.WIDTH_SCREEN
            
    def draw_floor(self, screen):
        # desenha o chão na tela
        screen.blit(self.IMAGE, (self.x1, self.y))
        screen.blit(self.IMAGE, (self.x2, self.y))
        
def draw_screen(screen,floor,points, pipe, bird):
    screen.blit(BACKGROUND, (0, 0)) # desenha o fundo na tela
    for birds in bird:
        birds.move()
        birds.drawing(screen)
    for pipes in pipe: # desenha os canos na tela
        pipes.drawPipe(screen) # desenha os canos na tela
        
    text = POINTS_FONTS.render(f'Point {points}', 1, (255, 255, 255))
    # escreve o texto na tela 
    
    screen.blit(text, (WIDTH_SCREEN - 10 - text.get_width(), 10))
    # screen.blit define a imagem na tela
    
    floor.draw_floor(screen)
    # define a imagem do fundo na tela
    
    pygame.display.update() #atualiza a tela
    
    
def main():
    '''
    função de inicialização do jogo
    '''
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN)) # define o tamanho da tela
    bird = [Bird(230, 350)] # define a posição do passaro na tela 
    pygame.display.set_caption('Flappy Bird') # define o nome do jogo na tela
    floor = Floor(730) # define a altura do chão , 730 é a altura do chão
    pipe = [Pipe(300)] # define a posição do cano na tela (padrao 700)
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
                        
        # for birds in bird:
        #     birds.move()
        # floor.move_to()
        # add_pipe = False
        # remove_pipe = []
        
        # for pipes in pipe:
        #     for i, birds in enumerate(bird):
        #         print(f"Bird {i} position: ({birds.x}, {birds.y})")
        #         if pipes.collide(birds):
        #             bird.pop(i)
        #             new_bird = Bird(230, 350)
        #             bird.append(new_bird)
        #     if not pipes.passed and birds.x > pipes.x:
        #         pipes.passed = True
        #         add_pipe = True
        #     if not pipes.movePipe():
        #         remove_pipe.append(pipes)
                
        # if add_pipe:
        #     points += 1
        #     pipe.append(Pipe(600))
        #     bird.append(Bird(230, 350)) # provavelmente ira duplicar os passaros , verificar mais a frente 

        # for pipes in remove_pipe:
        #     pipe.remove(pipes)
        
        #bird.append(Bird(230, 350)) # teste debug 
        pipe.append(Pipe(500)) # teste debug 
        #points += 1 # teste debug 
        floor.move_to() # teste debug  
        
        draw_screen(screen, floor, points, pipe, bird) 
      
if __name__ == '__main__':
    main()

from math import atan2, degrees, pi
import math
import pygame
from random import *
from PIL import Image
import os
import time
# import matplotlib.pyplot as plt
# import scipy


font_name = pygame.font.match_font('arial')



def satellite(distance, RADIUS, CENTER,vector): # Calcula a posição para fazer o blit no braço
    if distance > 0:
        scalar = RADIUS / distance
        satelliteCenter = (
            int(round( CENTER[0] + vector[0]*scalar )) - h/2,
            int(round( CENTER[1] + vector[1]*scalar )) -w/2)
        return satelliteCenter

def calculateDistance(xA,yA,xB,yB): # calcula as distâncias entre pontos
    vector = (xA-xB, yA-yB)
    distance = (vector[0]**2 + vector[1]**2)**(0.5)
    return distance, vector

def calculateAngle(A,B): # Calcula o angulo entre dois pontos
    xA = A[0]
    yA = A[1]
    xB = B[0]
    yB = B[1]
    degs = 0

    dx = xB - xA
    dy = yB - yA
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads) 

    return degs

def calculateSpeed(angle,distance,variable_speed): # Calcula a velocidade (X e Y) dependendo do angulo
    speed = (0.08)*distance
    if speed < 20 and variable_speed:
        speed = 20
    
    if variable_speed == False:
        speed = 30
    vx = speed*math.cos((angle/180)*math.pi)
    # vx *=(-1)
    vy = speed*math.sin((angle/180)*math.pi)
    if vy < 0 and vy > -0.5:
        vy -=  0.3
    elif vy > 0 and vy < 0.5:
        vy += 0.3
    vy *= -1
    return [vx,vy]

class balls(pygame.sprite.Sprite): # Colasse bolas do tipo sprite para colidir cok blocos
    def __init__(self, angle, xy, VxVy, wh):
        pygame.sprite.Sprite.__init__(self)
        self.speed_x = VxVy[0]
        self.speed_y = VxVy[1]
        self.screen_width = wh[0]
        self.screen_height = wh[1]

        self.image = pygame.image.load('Images/ball.png')
        self.rect = self.image.get_rect()
        self.img_height = self.image.get_height()
        self.img_width = self.image.get_width()
        

        self.x= xy[0] + (self.img_width) + 3.5

        self.y = xy[1] + self.img_height + 3.5

        self.rect.topleft = [self.x, self.y] # put the ball in the top left corner
        # print("A diferença entre satelite e o centro é : x = {0} e y = {1}".format( xy[0] - self.rect.center[0] ,xy[1] - self.rect.center[1] ))
        



    def draw(self, tela): # desenha a imagem na tela 
        tela.blit(self.image, self.rect)

    def update (self):
        self.next_x = self.x + self.speed_x
        self.next_y = self.y + self.speed_y

        # Rebate a bola nas paredes
        if self.next_x - self.img_width/2 > self.screen_width or self.next_x + self.img_width/2 < 0:
            self.speed_x = -self.speed_x
            
        if self.next_y < 0:
            self.speed_y = -self.speed_y
            

        if self.rect.midbottom[1] + (self.img_height)>= self.screen_height:
            self.speed_y = 0
            self.speed_x = 30
            self.y = self.screen_height - self.img_height

        if self.rect.bottomleft[0] + 5 >= self.screen_width and self.y == self.screen_height - self.img_height:
            self.kill()
            
        self.x += self.speed_x
        self.y += self.speed_y
        # self.y = self.screen_height

        self.NEXT_X = self.x + 2*(self.speed_x)
        self.NEXT_Y = self.y + 2*(self.speed_y)

        self.rect.topleft = [self.x,self.y]
        



class player(pygame.sprite.Sprite):
    def  __init__(self,  wh):
        pygame.sprite.Sprite.__init__(self)
        

        self.screen_width = wh[0]
        self.screen_height = wh[1]
        
        self.speedx = 0

        self.character = pygame.image.load("Images/First_characters2.png")
        
        self.height = self.character.get_height()
        self.width = self.character.get_width()
        scale = 1
        self.character = pygame.transform.scale(self.character, (int(self.width*scale), int(self.height*scale)))

        self.height = self.character.get_height()
        self.width = self.character.get_width()
        self.pos_x = self.screen_width/2 - (self.width)/2
        self.pos_y = self.screen_height - (self.height)

        self.rect = self.character.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y ]
        self.radius = 10
        self.offset_x = 77
        self.offset_y = 112
        center = (self.pos_x + self.offset_x,self.pos_y + self.offset_y)
        # self.arm = arm(center,self.radius,scale,0,self.radius)
        # self.arm.Image_arm("braco2.png")


    def draw (self,tela):
        tela.blit(self.character, self.rect.topleft)
        # tela.blit(self.arm.image_rotate,(self.arm.satelliteCenter_x,self.arm.satelliteCenter_y))
    def update(self,deltaX):
     
    # Move o player se alguma das teclas forem apertadas  
        
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > self.screen_width:
            self.rect.right =  self.screen_width
        if self.rect.left < 0:
            self.rect.left = 0
        self.speedx = 0



class menu(pygame.sprite.Sprite):
    def __init__(self,xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/menu.png")
        self.pos_x = xy[0]
        self.pos_y = xy[1]
    def draw(self,tela):
        tela.blit(self.image, (self.pos_x,self.pos_y))



class Background(pygame.sprite.Sprite):
    def __init__(self, img, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.back = pygame.image.load(img)
        self.rect = self.back.get_rect()
        self.rect.left, self.rect.top = location


class Blocks (pygame.sprite.Sprite):
    
    def __init__(self,xy, Initial_points):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/bloc_reserva.png")
        self.image_original = self.image
        self.image_height = self.image.get_height()
        self.rect = self.image.get_rect()
        xy = [(xy[0])*BLOCKSIZE,(xy[1])*BLOCKSIZE]

        self.rect.topleft = xy
        self.points = Initial_points
        self.next_pos = [self.rect.topleft[0], self.rect.topleft[1] + self.image_height]
        self.end = False
        self.font_name = pygame.font.match_font('arial') 
        self.font_size = 30

    def down (self):
        self.rect.topleft = (self.rect.topleft[0],self.rect.topleft[1]+ self.rect.height)
        
        if self.rect.topleft[1] + 2*self.image_height >= SCREEN_HEIGHT:
            self.end = True
        else:
            self.end = False


    def update(self):
        # pass
        text_rect = Images_points[self.points][1]
        text_rect.center = self.rect.center
        screen.blit(Images_points[self.points][0], text_rect )
        # if self.points <= 5:
        #     self.image = self.image_green
        pontos  = self.points
        while pontos >120:
            pontos -= 120
        self.image = lista_imagens[pontos]


    def collide(self):
        self.points -= 1
        if Playing_sound == True:
            block_sound.play()
            block_sound.set_volume(0.1)
        
        # print(self.points)
        if self.points <= 0:
            self.kill()
            #expl_sound.play()


    def draw_text(self,surf): #escrever na tela
        font = pygame.font.Font(self.font_name, self.font_size)
        text_surface = font.render(str(self.points), True, (255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        # print(font_name,self.font_size, self.points, self.text_rect.center, self.rect.center)
        surf.blit(text_surface, text_rect)

class Buttons (pygame.sprite.Sprite):
    
    def __init__(self,x,y,Image_name,New_image,func):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/"+Image_name)
        self.original = self.image
        self.new_image = pygame.image.load("Images/"+New_image)
        self.function = func
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def verify_click(self, mouse_position):
        if mouse_position[0]>= self.rect.topleft[0] and mouse_position[0]<= self.rect.topright[0] \
             and mouse_position[1]>= self.rect.topleft[1] and mouse_position[1]<= self.rect.bottomleft[1]:
           self.change_image()
           return self.function
        else:
            return False

    def change_image(self):
        hold = self.image
        self.image = self.new_image
        self.new_image = hold
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
    def draw(self,tela):
        tela.blit(self.image, self.rect)
    def rect_topleft(self,h,w):
        self.rect.topright = [w,h]


class Points_up (pygame.sprite.Sprite):
    
    def __init__(self,xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Plus_balls.png")
        self.rect = self.image.get_rect()
        self.rect.center = [xy[0]+46, xy[1]+46]
    def draw(self,tela):

        tela.blit(self.image, self.rect)
    
    def update(self):
        self.rect.topleft = (self.rect.topleft[0],self.rect.topleft[1]+ BLOCKSIZE)
        if self.rect.midbottom[1]  >= SCREEN_HEIGHT:
            self.kill()

def Gera_imagens_pontos(lista,name,font_size):
    size = len(lista)
    index = size -1
    font_name = pygame.font.match_font(name) 
    font = pygame.font.Font(font_name,font_size)
    text_surface = font.render(str(size), True, (255,255,255))
    text_rect = text_surface.get_rect()
    lista.append([text_surface, text_rect])
    return lista

def Gera_número_de_bolas(lista,name,font_size):
    size = len(lista)
    index = size -1
    font_name = pygame.font.match_font(name)
    # font_name.set_bold(font_name)
    font = pygame.font.Font(font_name,font_size)
    font.set_bold(True)
    text = str(size) + "x"
    text_surface = font.render(text, True, (255,229,114))
    text_rect = text_surface.get_rect()
    lista.append([text_surface, text_rect])
    return lista


def gera_SCORE (lista):
    tamanho = len(lista)
    font_size = 20
    font = pygame.font.Font(font_name,font_size)
    font.set_bold(True)
    text_surface = font.render("SCORE: {0}".format(tamanho), True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = [1000 -250/2, 200]
    lista.append([text_surface,text_rect])
    return lista

def gera_HIGHSCORE (lista):
    tamanho = len(lista)
    font_size = 20
    font = pygame.font.Font(font_name,font_size)
    font.set_bold(True)
    text_surface = font.render("HIGHSCORE: {0}".format(tamanho), True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = [1000 -250/2, 270]
    lista.append([text_surface,text_rect])
    return lista

def Points_to_color(points):
    r = 0
    g = 0
    b =0
    if points < 20:
        r= 255
        g = 255 - points*12.75
    elif points >= 20 and points <40:
        value = points -20
        r= 255 - value*12.75
        g = value*12.75
    elif points >= 40 and points <=60:
        value = points -40
        g= 255 - value*12.75
        b = value*12.75
    

    elif points >= 60 and points <80:
        value = points -60
        b= 255 - value*12.75
        g = value*12.75
    elif points >= 80 and points <100:
        value = points -80
        g= 255 - value*12.75
        r = value*12.75
    elif points >= 100:
        g= 255
        r = 255 - points*12.75
    


    if r>255:
        r = 255
    if g>255:
        g = 255
    if b>255:
        b = 255
    if r<0:
        r = 0
    if g<0:
        g = 0
    if b<0:
        b = 0
    return [int(r),int(g),int(b),255]

def colorBlock(filename,lista_imagens):
    points = len(lista_imagens)
    image = Image.open(filename)
    r,g,b,value = Points_to_color(points)
    size = width, height = image.size
    pixel_access_object = image.load()
    for x in range(width):
        for y in range(height):
            if pixel_access_object[x,y][3] != 0: # Se o pixel da imagen não é transparente mude ele de cor
                pixel_access_object[x,y] = (r,g,b,value)
    image.save("Images/Modified_block.png")
    lista_imagens.append(pygame.image.load("Images/Modified_block.png"))
    return lista_imagens
def Perdeu():
    screen.fill((0,0,0))
    pygame.mixer.music.set_volume(0)
    if Playing_sound == True:
        go_sound.play()
        go_sound.set_volume(0.3)
    font_name = pygame.font.match_font('arial') 
    font = pygame.font.Font(font_name,90)
    font.set_bold(True)
    text_surface = font.render("Você perdeu!", True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    screen.blit(text_surface,text_rect)
    font = pygame.font.Font(font_name,30)
    text_surface = font.render("CLIQUE NA TELA PARA CONTINUAR", True, (255,190,0))
    font.set_bold(True)
    text_rect = text_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 70)
    screen.blit(text_surface,text_rect)



def in_game (mouse_position,screen_size):
    if mouse_position[0]>= screen_size:
        return False
    else:
        return True  


pygame.init()
pygame.font.init()
    

Images_points =[] # gera uma lista de imagens com pontos correspondentes
Ball_points = [] # gera uma lista de imagens com pontos correspondentes
lista_imagens = []
lista_score = []
lista_highscore = []
Max_num_of_images = 250

for pontos in range(0,250):
    Images_points = Gera_imagens_pontos(Images_points,'arial',30)
    Ball_points = Gera_número_de_bolas(Ball_points,'arial',20)
    lista_score = gera_SCORE(lista_score)
    lista_highscore = gera_HIGHSCORE(lista_highscore)
for x in range(0,121):
    lista_imagens =  colorBlock("Images/bloc_reserva.png",lista_imagens)
os.remove("Images/Modified_block.png")

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
MENU = 250

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pytan")

CENTER_X = 375
CENTER_Y = 630
CENTER = (CENTER_X, CENTER_Y)
RADIUS = 5

BLOCKSIZE = 94

FPS = 30

running = True
braço = pygame.image.load('Images/braco.png')


satelliteCenter = (CENTER[0]+RADIUS, CENTER[1])
current_angle = 0

#SPRITES
MENU_POS = (SCREEN_WIDTH-MENU,0)
main_menu = menu(MENU_POS)

with open("high_score.txt","r") as save:
    high_score = save.read()
if high_score != "":
    scores = [int(high_score)]
else:
    scores = []

clock = pygame.time.Clock()

button_group_menu = pygame.sprite.Group()
xyz = Buttons(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,"jogo_novo.png","jogo_novo2.png","Start_playing")
abc = Buttons(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100,"Instructions.png", "Instructions2.png", "Entrar_instrução")
button_group_menu.add(xyz)
button_group_menu.add(abc)


close_instr_menu= Buttons(SCREEN_WIDTH/2  + 380, 40, "close.png", "close.png", "Sair_instrução")
# close_instr_menu.rect_topleft(SCREEN_WIDTH - 20  ,100)



# lista_bg = ['Images/bg1.jpg','Images/bg2.jpg','Images/bg3.jpg','Images/bg4.jpg','Images/bg5.jpg']
# bg = choice(lista_bg)
BackGround = pygame.image.load('Images/Space.jpg')
Img_Instruções = pygame.image.load('Images/Instruções_do_jogo.png')
Instruções_rect = Img_Instruções.get_rect()
Instruções_rect.center = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2]
pygame.mixer.music.load('Music/fundo.mp3')
# pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.8)


shoot_sound = pygame.mixer.Sound('Music/tiro.ogg')
block_sound = pygame.mixer.Sound('Music/block.ogg')
expl_sound = pygame.mixer.Sound('Music/expl.ogg')
go_sound = pygame.mixer.Sound('Music/game over.ogg')

Playing_sound = True
preto = False

Instruções = False
Menu_inicial = True
while Menu_inicial:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Menu_inicial = False
            running = False
            print("Bye")
        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(0.1)
            print("foi")

            buttons_clicked = []
            for buttons in button_group_menu:
                buttons_clicked.append(buttons.verify_click(pygame.mouse.get_pos()))
            
            if buttons_clicked != []:
                for items in buttons_clicked:
                    if items == "Start_playing":
                        Menu_inicial = False
                    if items == "Stop_menu":
                        running = False
                        Menu_inicial = False
                    if items == "Entrar_instrução":
                        Instruções = True


 
    screen.blit(BackGround,[0,0])
    button_group_menu.draw(screen)

    clock.tick(FPS)
    pygame.display.update()
    if Menu_inicial == False or Instruções == True:
        time.sleep(0.15)

    


    while Instruções == True:
        screen.blit(Img_Instruções, Instruções_rect)
        close_instr_menu.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Menu_inicial = False
                running = False
                Instruções = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                time.sleep(0.1)
    
                if close_instr_menu.verify_click(pygame.mouse.get_pos()) == "Sair_instrução":
                    Instruções = False

                    for botoes in button_group_menu:
                        if botoes.original != botoes.image:
                            original = botoes.image # vai dar errado
                            botoes.new_image = original
                            botoes.image = botoes.original
                            
                        pass
        pygame.display.update()
        clock.tick(FPS)
        
               




braço_rot = braço
ball_original = None
launch = False
numberBall = 0

ball_group = pygame.sprite.Group()
new_ball = False

block_group = pygame.sprite.Group()
new_block = None

button_group = pygame.sprite.Group()
first_button = Buttons(SCREEN_WIDTH - MENU/2,50,"speaker.png","mute.png","Stop_music")
button_group.add(first_button)

points_group = pygame.sprite.Group()
first_point = Points_up([1*BLOCKSIZE,1*BLOCKSIZE])
points_group.add(first_point)




bolas_lançadas =0

listablocos = []
num_blocos = randint(1,6)
for x in range(num_blocos):
    rnd = randint(0,7)
    a = True
    while a == True:
        if rnd in listablocos: 
            rnd = randint(0,7)
        if rnd not in listablocos: 
            a = False
    listablocos.append(rnd)
    bloco_novo = Blocks([rnd,0],1)
    block_group.add(bloco_novo)

Bender = player((SCREEN_WIDTH - MENU ,SCREEN_HEIGHT))

colliding = {}

current_balls = 0
max_balls = 1
down = False

current_time = 0
wait_time = 3

bolas_lançadas = 0
score = 2

# current_balls = 0
# previous_num_balls =  current_balls
holding_ball = 0 # Quantas bolas o jogador ganhou
mouse = 0
Game  = True


# variaveis para iniciar o jogo

shoot = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Game = True
            if Playing_sound == True:
                pygame.mixer.music.set_volume(0.8)
            for items in block_group:
                if items.end == True:
                    items.end= False
            # Resetando as variaveis
            
            ball_original = None

            launch = False

            ball_group = pygame.sprite.Group()
            new_ball = False
            bolas_lançadas =0
            numberBall = 0

            block_group = pygame.sprite.Group()
            new_block = None

            points_group = pygame.sprite.Group()
            TEST = Points_up([1*BLOCKSIZE,1*BLOCKSIZE])
            points_group.add(TEST)


            listablocos = []
            num_blocos = randint(1,6)
            for x in range(num_blocos):
                rnd = randint(0,7)
                a = True
                while a == True:
                    if rnd in listablocos: 
                        rnd = randint(0,7)
                    if rnd not in listablocos: 
                        a = False
                listablocos.append(rnd)
                bloco_novo = Blocks([rnd,0],1)
                block_group.add(bloco_novo)


            colliding = {}
            running = True

            current_balls = 0
            max_balls = 1
            down = False

            current_time = 0

            bolas_lançadas = 0
            score = 2

            holding_ball = 0
            mouse = 0

    while Game == True:
        buttons_clicked = []
        for event in pygame.event.get():
            keystate = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                


                running = False
                Game = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                in_screen = in_game(pygame.mouse.get_pos(),SCREEN_WIDTH-MENU)

                if in_screen == True:
                    if current_balls == 0:
                        launch = True

                buttons_clicked = []
                for buttons in button_group:
                    buttons_clicked.append(buttons.verify_click(pygame.mouse.get_pos()))
 

                    Previous_mouse = mouse
                    Previous_angle = current_angle

            if keystate[pygame.K_k] and launch == False:
                ball_group.empty()


        if buttons_clicked != []:
            for items in buttons_clicked:
                if items == "Stop_music":
                    Playing_sound =  not Playing_sound
                    if Playing_sound == True:
                        pygame.mixer.music.set_volume(0.8)
                    else:
                        pygame.mixer.music.set_volume(0)

        CENTER = (Bender.rect.topleft[0] + Bender.offset_x,Bender.rect.topleft[1] + Bender.offset_y)
        mouse = pygame.mouse.get_pos()
        


        if launch == True:
            current_angle = Previous_angle 
            mouse = Previous_mouse
            shoot = True
        else:
            current_angle = calculateAngle(CENTER,mouse)
        
        if current_angle >=  175 or current_angle <= 5:
            launch = False      
            mouse = pygame.mouse.get_pos()
            current_angle = calculateAngle(CENTER,mouse)

        if shoot == True and Playing_sound == True and launch == True:
            shoot_sound.play(0)
            shoot_sound.set_volume(0.1)
            shoot = False

        distance_mouse, vector = calculateDistance(mouse[0],mouse[1],CENTER[0],CENTER[1])
        braço_rot = pygame.transform.rotate(braço, current_angle)

        w = braço_rot.get_width()
        h = braço_rot.get_height()
        satelliteCenter = satellite(distance_mouse, RADIUS, CENTER,vector)

        screen.fill((0,0,0))
        #screen.blit(BackGround.back, BackGround.rect)

        points_group.draw(screen)
        block_group.update()
        block_group.draw(screen)

        Bender.draw(screen)
        screen.blit(Ball_points[max_balls-bolas_lançadas][0], [Bender.rect.topleft[0] +95 , Bender.rect.topleft[1] + 120])
        #Imprime o número de bolas do jogador
         

        Bender.update(0)
        # Se clicou mouse, cria bola
        if current_time >= wait_time or current_balls == 0 :

            current_time = 0

            if bolas_lançadas < max_balls and launch == True:

                ball_original = balls(current_angle,satelliteCenter,calculateSpeed(current_angle,distance_mouse,False), (SCREEN_WIDTH-MENU, SCREEN_HEIGHT))
                if bolas_lançadas < max_balls:
                    ball_group.add(ball_original)
                    new_ball = True
                    bolas_lançadas +=1

        
        current_balls = len(ball_group.sprites())


        if bolas_lançadas >= max_balls and launch == True :
            launch = False
            down = True
        
        if current_balls == 0:
            bolas_lançadas = 0
            max_balls += holding_ball
            holding_ball = 0

        if down == True and current_balls == 0: # avança os blocos para baixo
            for quadrados in block_group:
                quadrados.down()
            # cria quantidade e posições de blocos aleatórios
            rnd = randint(0,7)
            # bloco_novo = Blocks([rnd,0],score)
            rnd2 = randint(0,7)
            listablocos = []
            num_blocos = randint(1,6) # Quantos blocos tem na linha
            for x in range(num_blocos):
                rnd = randint(0,7)
                a = True
                while a == True:
                    if rnd in listablocos: 
                        rnd = randint(0,7)
                    if rnd not in listablocos: 
                        a = False
                listablocos.append(rnd)
                bloco_novo = Blocks([rnd,0],score)
                block_group.add(bloco_novo)

            while rnd2 in listablocos:
                rnd2 = randint(0,7)

            TEST = Points_up([rnd2*BLOCKSIZE,-BLOCKSIZE])
            points_group.add(TEST)
            
            points_group.update()
            down = False
            score+=1
            
            if score + 50 == Max_num_of_images:
                Max_num_of_images = Max_num_of_images +250
                for pontos in range(0,250):
                    Images_points = Gera_imagens_pontos(Images_points,'arial',30)
                    Ball_points = Gera_número_de_bolas(Ball_points,'arial',20)
                    lista_score = gera_SCORE(lista_score)
                    lista_highscore = gera_HIGHSCORE(lista_highscore)



        # Se tem bola, pinta ela e avança
        if ball_group.has() == True or new_ball == False:
            screen.blit(braço_rot, satelliteCenter)
            if ball_original != None:
                ball_group.update()
                ball_group.draw(screen)
        else:
            if ball_original != None:
                ball_group.update()
                ball_group.draw(screen)
            screen.blit(braço_rot, satelliteCenter)
            new_ball = False

        




        colliding = pygame.sprite.groupcollide( ball_group , block_group, False, False)
        if colliding != {}:
            for colliding_ball in colliding:
                for colliding_block in colliding[colliding_ball]:
                    # print("Bola {0} colidiu com bloco {1}".format(colliding_ball.rect, colliding_block.rect))
                    colliding_block.collide()
                    
                    # Volta para trás na direção y e testa colisão. (Ou seja, andou apenas em x.)
                    colliding_ball.rect.topleft = (colliding_ball.x, colliding_ball.y - colliding_ball.speed_y)
                    if pygame.sprite.collide_rect(colliding_ball, colliding_block):
                        # Se colidiu, é porque colidiu andando em x.
                        colliding_ball.speed_x = -colliding_ball.speed_x
                    else:
                        # Caso contrário, é porque colidiu andando em y.
                        colliding_ball.speed_y = -colliding_ball.speed_y
                    colliding_ball.rect.topleft = (colliding_ball.x, colliding_ball.y)
        colliding_points = pygame.sprite.groupcollide( ball_group , points_group, False, True)
        if colliding_points  != {}: 
            # print("NEW BALL")
            holding_ball+=1
        
        main_menu.draw(screen)
        button_group.draw(screen)
        screen.blit(lista_score[score-1][0],lista_score[score-1][1])
        screen.blit(lista_highscore[max(scores)][0],lista_highscore[max(scores)][1])
        save = False

        if score > scores[0]:
            scores = [score-1]
            save = True

        for items in block_group:
            if items.end == True:
                Perdeu()
                with open("high_score.txt","w") as save:
                    if score > max(scores) or save == True:
                        scores.append(score)
                    save.writelines(str(score-2))
                Game = False
        

        pygame.display.update()
        current_time +=1
        clock.tick(FPS)
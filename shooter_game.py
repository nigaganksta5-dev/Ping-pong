
#Создай собственный Шутер!
from pygame import *
from random import * 
from time import time as tm

font.init()
mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()
# mixer.music.set_volume(0.3)
# shoot = mixer.Sound('fire.ogg')
#создай окно игры
window = display.set_mode((800,400))
display.set_caption('Пинг-понг')
background = transform.scale(image.load('phon.jpg'),(800,400))
y1 = 350
y2 = 350
x1 = 100
x2 = 300
font0 = font.SysFont('Arial', 40)
win = font0.render('Ты убил всех хлебом', True, (255,215, 0))
loss = font0.render('Ты потратил слишком много хлеба', True,(255,215,0))
font1 = font.SysFont('Arial',20)
points = 0
loser = 0

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed,w,h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w,h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

    
bread = Gamesprite('bread.png', 400,200,0,50,50)  
player_l = Player('Hero.png.png', 0,200, 10,80,50)
player_r = Player('Hero2.png', 720,200, 10, 80, 50)

speed_x = 5
speed_y = 5

clock = time.Clock()
FPS = 60
speed = 10
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        
                        
    if finish != True:
        window.blit(background,(0,0))
        player_l.update_l()
        player_l.reset()
        player_r.update_r()
        player_r.reset()
        bread.rect.x += speed_x
        bread.rect.y += speed_y
        bread.reset()
        if bread.rect.y > 350 or bread.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player_l,bread) or sprite.collide_rect(player_r,bread):
            speed_x *= -1



    display.update()
    clock.tick(FPS)

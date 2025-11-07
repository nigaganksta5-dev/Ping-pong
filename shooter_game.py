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
window = display.set_mode((500,900))
display.set_caption('Шутер')
background = transform.scale(image.load('phon.jpg'),(500,900))
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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 420:
            self.rect.x += self.speed
    
    
player = Player('Hero.png.png', 250,850, 10,80,50)

num_fire = 0
rel_time = False

clock = time.Clock()
FPS = 60
speed = 10
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire <= 5 and rel_time == False:
                    player.fire()
                    shoot.play() 
                    num_fire += 1
                if num_fire > 5 and rel_time == False:
                    rel_time = True
                    start = tm()
                        
    if finish != True:
        window.blit(background,(0,0))
        player.update()
        player.reset()
        

    display.update()
    clock.tick(FPS)

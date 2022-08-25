from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (50, 50))
        self.speed = player_speed
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
 
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
 
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
 
class Wall(sprite.Sprite):
    def __init__(self, col1, col2, col3, x, y, width, height):
        self.col1 = col1
        self.col2 = col2
        self.col3 = col3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = Surface(size=(self.width, self.height))
        self.image.fill((col1, col2, col3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)

font.init()
font = font.Font(None, 50)
lose = font.render("GAME OVER", True, (180, 0, 0))
win = font.render("YOU WIN! GAME OVER", True, (225, 215, 0))

w1 = Wall(col1=154, col2=205, col3=50, x=100, y=20, width=450, height=10)
w2 = Wall(154, 205, 50, 100, 480, 430, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 100, 10, 380)
w5 = Wall(154, 205, 50, 300, 20, 10, 380)
w6 = Wall(154, 205, 50, 400, 100, 10, 380)
w7 = Wall(154, 205, 50, 500, 20, 10, 380)
 
game = True
finish = False
clock = time.Clock()
FPS = 60
 
#music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
 
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        final.reset()
 
        w1.draw()
        w2.draw()
        w3.draw()
        w4.draw()
        w5.draw()
        w6.draw()
        w7.draw()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            window.blit(lose, (200,200))
            finish = True

        if sprite.collide_rect(player, final):
            window.blit(win, (200, 200))
            finish = True
 
    display.update()
    clock.tick(FPS)

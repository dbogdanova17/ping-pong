from pygame import*
window = display.set_mode((700,500))
display.set_caption('ping pong')

class GameSprite(sprite.Sprite):
    def __init__(self, player_name, speed, x, y, sx, sy):
        super().__init__()
        self.image = transform.scale(image.load(player_name),(sx,sy))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<450:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<450:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, image, speedx, speedy, x, y, sizex, sizey):
        super().__init__(image, speedx, x, y, sizex, sizey)
        self.speed2 = speedy

    def update(self, r1, r2):
        self.rect.x += self.speed
        self.rect.y += self.speed2
        if sprite.collide_rect(self, r1) or sprite.collide_rect(self, r2):
            self.speed *= -1
        if self.rect.y<0 or self.rect.bottom> 490:
            self.speed2 *= -1


ball = Ball('ball.png', 5, 5, 350, 255, 55, 50)
player_l = Player('racket.png', 10, 10, 200, 20, 100)
player_r = Player('racket.png', 10, 640, 200, 20, 100)
font.init()
font1 = font.Font(None, 40)

clock = time.Clock()
FPS = 60
finish = False
game = True
while game:    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if not finish:
            if ball.rect.x < 0:
                text = font1.render('правый выйграл!' ,1, (0, 255, 0), (0,0,0))
            if ball.rect.x > 700:
                text2 = font1.render('левый выйграл!' ,1, (0, 255, 0), (0,0,0))
    window.fill((192, 192, 192))
    player_r.update_r()
    player_r.reset()
    player_l.update_l()
    player_l.reset()
    ball.reset()
    ball.update(player_l, player_r)
    display.update()
    clock.tick(FPS)
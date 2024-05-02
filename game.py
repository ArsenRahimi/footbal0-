from pygame import*
init()
width = 1000
hight = 700
mw = display.set_mode((width,hight))

pbg = image.load('images.jpg')
bg = transform.scale(pbg, (width, hight))

class rocket(): 
    def __init__(self, image_sprite, img_x, img_y, w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_sprite),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = img_x
        self.rect.y = img_y
    def show_s(self):
        mw.blit(self.image,(self.rect.x , self.rect.y))

class Player(rocket):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < width -380:
            self.rect.y += self.speed

class vorota(rocket):
    naprav = "down"
    def update(self):
        if self.rect.y <= -10:
            self.naprav = 'up'
        if self.rect.y >= width - 550:
            self.naprav = 'down'
       
        if self.naprav == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
             







mixer.init()
mixer.music.load('zvuk-futbola-igra-v-futbol-25641.mp3')
mixer.music.play()


vora = vorota('1677932914_bogatyr-club-p-futbolnie-vorota-foni-pinterest-20.png',800, 0, 150,300, 2)
playe = Player('6633babde1793_1714666255_6633babde1788.png',10, 350, 150, 200, 2)
ball = rocket('png-transparent-soccer-ball-football-animation-football-ball-love-game-sport-removebg-preview.png',500, 350, 110, 110, 5)
fps = time.Clock()
run = True
sm =1
sk =1

win = 0
lost = 0










while run:

    for i in event.get():
        if i.type == QUIT:
            run = False
    mw.blit(bg,(0,0))
    playe.show_s()
    playe.update()
    ball.show_s()
    ball.rect.x -= sm
    ball.rect.y -= sk
    if  ball.rect.x  < 10 or ball.rect.y < 10:
        sk*=-1

    if  ball.rect.x  > width -100 or ball.rect.y > hight -100:
        sm*=-1
        sk*=-1

    if sprite.collide_rect(playe,ball):
        sm*=-1
        sk*=-1
        




       
    if sprite.collide_rect(vora,ball):
        sm = sm * 1.25
        sm*=-1
        win+=1







    if ball.rect.x > width -100:
        lost +=1
        ball.rect.x = 500
        ball.rect.y = 350

        


    vora.show_s()
    vora.update()
    
    
    text = font.SysFont(None, 70).render("Попал - "+str(win), True, (255,255,255))
    text2 = font.SysFont(None, 70).render("Мимо - "+str(lost), True, (255,255,255))
    mw.blit(text, (430, 10))
    mw.blit(text2, (430, 50))
    display.update()
    fps.tick()
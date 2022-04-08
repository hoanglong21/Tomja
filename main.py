import pygame
from pygame import mixer
import random
pygame.init()
health=health1=400
healthh=health2=130
healthbar=5
xscreen,yscreen=1920,1080
linkblnv="katana1.png"
linkblnv1='bullet.png'
linkbg='bg1.jpg'
linknv2='mt1.png'
linknv3="mt2.png"
linknv4="mt3.png"
linknv5="mt4.png"
linknv1='right.png'
linkbl='suriken.png'
linkbl1="virus.png"
linkbl2="virus1.png"
linkbl3="virus2.png"
linkbl4="virus3.png"
linkhealth="health.png"
linkhealthbar="healthbar.png"
screen=pygame.display.set_mode((xscreen,yscreen))
pygame.display.set_caption("Team 2 - Japan Fight")
bg=pygame.image.load(linkbg)
run=True
#nv1
xsizenv1=80#chieu cao
ysizenv1 =60   #chieu rong
xnv1=xscreen/6
ynv1=yscreen-150
vnv1=20
#nv2
xsizenv2=80#chieu cao
ysizenv2 =60   #chieu rong
xnv2=xscreen-800
ynv2=yscreen-190
vnv2=4
vbl=30
numberbl1=15
numberbl2=12
listbl1=[]
listbl2=[]
xsizebl=25
ysizebl=25
xsizebl1=25
ysizebl1=25
chx_nv1=0
chx_nv2=5
chy_nv1=5
chy_nv2=5
state=1
def show_winner( x, y, winner, size):  # Hiển thị winner
    font = pygame.font.SysFont("comicsansms", size)
    winner = font.render(str(winner), True, (0,0,0))
    screen.blit(winner, (x, y))
def music( url):  # Âm thanh bắn
    bulletSound = mixer.Sound(url)
    bulletSound.play()
music("bg.wav")
def image_draw( url, xLocal, yLocal, xImg, yImg):  # In ra người hình ảnh
    Img = pygame.image.load(url)
    Img = pygame.transform.scale(Img, (xImg, yImg))  # change size image
    screen.blit(Img, (xLocal, yLocal))
def bullet():
    #nv1
    for count, i in enumerate(listbl1):
        xBullet = i["xBullet"]
        yBullet = i["yBullet"]
        image_draw(linkbl, xBullet, yBullet, xsizebl,ysizebl)  # In ra bullet
        listbl1[count]["xBullet"] = xBullet +vbl # Tiến x vè phía trước
        if xBullet >= xscreen: listbl1.remove(listbl1[count]) # nếu toạn độ x phía ngoai nàm hình thì xóa
    #nv2
    for count, i in enumerate(listbl2):
        xBullet = i["xBullet"]
        yBullet = i["yBullet"]
        image_draw(linkbl1, xBullet, yBullet, xsizebl1,ysizebl1)  # In ra bullet
        listbl2[count]["xBullet"] = xBullet -vbl # Tiến y vè phía trước
        if xBullet <=0: listbl2.remove(listbl2[count]) # nếu toạn độ x phía ngoai nàm hình thì xóa
while run:
    image_draw(linkbg,0,0,xscreen,yscreen)
    show_winner(800, 140,'JS_FIGHT', 80)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.KEYUP:  # sự kiện tha phim
            if event.key == pygame.K_SPACE:
                music("hit.wav")
            if event.key == pygame.K_KP_ENTER:
                music("hit.wav")
            if event.key == pygame.K_LEFT:
                chx_nv1=0
            if event.key == pygame.K_RIGHT:
                chx_nv1=0
            if event.key==pygame.K_UP:
                chy_nv1=+15
        if event.type == pygame.KEYDOWN:  # sự kiện có phím nhấn xuống
            if event.key == pygame.K_SPACE:
                if (len(listbl1)<numberbl1):
                    listbl1.append({"xBullet": xnv1+200 ,"yBullet": ynv1+20})
            if event.key == pygame.K_LEFT:
                chx_nv1=-10
            if event.key == pygame.K_RIGHT:
                chx_nv1=10
            if event.key==pygame.K_UP:
                chy_nv1=-20
        if (len(listbl2)<numberbl2):
            listbl2.append({"xBullet": xnv2-60 ,"yBullet": ynv2+ysizenv2//2+(state*12)/2})
        heatlthbar=random.randint(1,10)
        for countBullet, bulletIteam in enumerate(listbl1):
            xBullet = bulletIteam["xBullet"]
            yBullet = bulletIteam["yBullet"]
            # Kiểm tra bullet có nằm giữa Enemy theo trục x không
            isInX = xnv2-30 <= xBullet <= xnv2 + xsizenv2+30
            # Kiểm tra bullet có nằm giữa Enemy theo trục y không
            isInY = ynv2-30<= yBullet <= ynv2 + ysizenv2+30
            if (isInX and isInY):  # nếu nằm giữa
                music("bullet.wav")
                listbl1.remove(listbl1[countBullet])  # Xóa Bullet
                health2 -= healthbar  # tru mau
                break
        for countBullet, bulletIteam in enumerate(listbl2):
            xBullet = bulletIteam["xBullet"]
            yBullet = bulletIteam["yBullet"]
            # Kiểm tra bullet có nằm giữa Enemy theo trục x không
            isInX = xnv1-30 <= xBullet <= xnv1 + xsizenv1+30
            # Kiểm tra bullet có nằm giữa Enemy theo trục y không
            isInY = ynv1-30 <= yBullet <= ynv1 + ysizenv1+30
            if (isInX and isInY):  # nếu nằm giữa
                music("bullet.wav")
                listbl2.remove(listbl2[countBullet])  # Xóa Bullet
                health1 -= healthbar  # tru mau
                break
        if health2<=180 and health2 % 5==0 : ynv2-=random.randint(7,20)
        if (health2<=0):
            state+=1
            xsizenv2+=50
            ysizenv2+=50
            ynv2 -= 50
            health2=healthh=state*100
            numberbl1+=1
            if (state==2): linknv2="mt3.png";linkbl1='virus2.png';vbl+=1.5;vnv2+=2;linkbl=linkblnv1;xsizebl+=3;ysizebl+=3;xsizebl1+=2;ysizebl1+=2
            if (state == 3): linknv2='mt4.png';linkbl1='virus3.png';vbl+=1.5;vnv2+=3;linkbl=linkblnv;xsizebl+=7;ysizebl+=7;xsizebl1+=5;ysizebl1+=5
        if health1>=0: winner="WINNER"
        if health1<=0: winner="GAMEOVER"
        if(health1<=0 or state==4):
            newGame=False
            music("gameover.wav")
            while (True):
                for event in pygame.event.get():  # Nếu nhấn
                    if event.type == pygame.QUIT:  # Thoát
                        run = False
                        newGame = True
                        break
                    if event.type == pygame.KEYDOWN:  # Thoát
                        newGame = True
                        break
                if (newGame == True):  # Thoát vòng while để vào game mới
                    break
                show_winner(680, 460,winner, 100)  # In Thông báo ket qua
                pygame.display.update()
            listbl1 = []
            listbl2 = []
    xnv1 += chx_nv1
    ynv1 += chy_nv1
    xnv2 += chx_nv2
    ynv2 += random.randint(2, 10)
    if (xnv1 >= xscreen-800): xnv1 = xscreen-800
    if (xnv2 >= xscreen-480-state*50): xnv2 = xscreen-480-state*50;chx_nv2*=-1
    if (ynv1 >= yscreen - 220): ynv1 = yscreen - 220
    if (xnv1 <= 300): xnv1 = 300
    if (ynv1 <=330): ynv1 = 330
    if (xnv2 <= 1000): xnv2 = 1000;chx_nv2*=-1
    if (ynv2<=330): ynv2=330
    if (ynv2>=yscreen-150-state*50-20): ynv2=yscreen-150-state*50-10
    image_draw(linkhealthbar, 300,180,health,60)
    image_draw(linkhealth, 300, 180, health1, 60)
    image_draw(linkhealthbar, 1640-healthh-20, 180,  healthh,60)
    image_draw(linkhealth, 1640-healthh-20,180,health2,60)
    image_draw(linknv1, xnv1, ynv1, xsizenv1, ysizenv1)
    image_draw(linknv2, xnv2, ynv2, xsizenv2, ysizenv2)
    bullet()
    pygame.display.update()  # Update
    clock = pygame.time.Clock()
    clock.tick(70*state)
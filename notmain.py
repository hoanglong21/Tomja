import pygame,sys,math,random,time
# phổ biến luật chơi:
'''điều khiển nhân vật để nhặt các đồ trên map,nhân vật phải tránh quái,nếu đụng phỉa quái sẽ mất mạng và con quái cũng sẽ 
biến mất(người chơi có thể lợi dụng điều này để hi sinh một vài mạng để làm giảm độ khó của game) nv có tối đa 3 mạng,hết mạng là thua.
 người chơi phải ăn dc hết số đồ quy định và không bị hết mạng trong thời gian cho phép,nếu ăn dc 13/15 đồ thời gian sẽ chạy ngược về giây thứ 50
 sau đó phải tìm cách ăn dc thứ 14 rồi quay về cổng thì mới win,nếu trong thời gian còn 0 s mà chưa ăn đủ 13/15 đồ thì thua(lưu ý: đồ có thể sẽ 
 trùng màu với nền hay ở vị trí không nhìn ra trong map,người chơi cân nhắc đi tìm đồ và để ý thời gian:))'''
import pygame,sys,math,random,time
from pygame.locals import *
from pygame import mixer
pygame.init()
FPS = 60
health1=30
healthbar=15
health2=45
fpsClock = pygame.time.Clock()
pygame.display.set_caption('hello')
screen = pygame.display.set_mode((1920,1080))
WHITE = (255, 255, 255)
background = pygame.image.load('anh1.jpg')
backgroundimg = pygame.transform.scale(background,(1100,800))
nen = pygame.image.load('4256096.jpg')
nenimg = pygame.transform.scale(nen,(1920,1080))
linkmt="mt.png"
#player
linkmt='mt4.png'
xsizemt=30
ysizemt=30
js='right.png'

playeri= pygame.image.load('left.png')
playerimg = pygame.transform.scale(playeri,(30,30))
playerX = 150+450
playerY = 600+100
changex = 0
changey = 0
#phitieu
phitieui=pygame.image.load('shuriken.png')
phitieuimg = pygame.transform.scale(phitieui,(20,20))
#door
cua = pygame.image.load('door (2).png')
cuaX = random.randint(20+450,1000+450)
cuaY = random.randint(10+100,800)

# cau hoi
cauhoi1a=pygame.image.load("Slide1.PNG")
cauhoi1 = pygame.transform.scale(cauhoi1a,(1100,900))
cauhoi2a=pygame.image.load("Slide2.PNG")
cauhoi2 = pygame.transform.scale(cauhoi2a,(1100,900))
cauhoi3a=pygame.image.load("Slide3.PNG")
cauhoi3 = pygame.transform.scale(cauhoi3a,(1100,900))
cauhoi4a=pygame.image.load("Slide4.PNG")
cauhoi4 = pygame.transform.scale(cauhoi4a,(1100,900))
cauhoi5a=pygame.image.load("Slide5.PNG")
cauhoi5 = pygame.transform.scale(cauhoi5a,(1100,900))
cauhoi6a=pygame.image.load("Slide6.PNG")
cauhoi6 = pygame.transform.scale(cauhoi6a,(1100,900))
cauhoi7a=pygame.image.load("Slide7.PNG")
cauhoi7 = pygame.transform.scale(cauhoi7a,(1100,900))
cauhoi8a=pygame.image.load("Slide8.PNG")
cauhoi8 = pygame.transform.scale(cauhoi8a,(1100,900))
cauhoi9a=pygame.image.load("Slide9.PNG")
cauhoi9 = pygame.transform.scale(cauhoi9a,(1100,900))
cauhoi10a=pygame.image.load("Slide10.PNG")
cauhoi10 = pygame.transform.scale(cauhoi10a,(1100,900))
cauhoi11a=pygame.image.load("Slide11.PNG")
cauhoi11 = pygame.transform.scale(cauhoi11a,(1100,900))
cauhoi12a=pygame.image.load("Slide12.PNG")
cauhoi12 = pygame.transform.scale(cauhoi12a,(1100,900))
cauhoi13a=pygame.image.load("Slide13.PNG")
cauhoi13 = pygame.transform.scale(cauhoi13a,(1100,900))
cauhoi14a=pygame.image.load("Slide14.PNG")
cauhoi14 = pygame.transform.scale(cauhoi14a,(1100,900))
cauhoi15a=pygame.image.load("Slide14.PNG")
cauhoi15 = pygame.transform.scale(cauhoi15a,(1100,900))
#dovat
dovati= pygame.image.load('katana.png')
dovatx =random.randint(20+450,1100+400)
dovaty = random.randint(15+100,900-50)
dovata1= pygame.image.load('fan.png')
dovat1 = pygame.transform.scale(dovata1,(40,40))
dovatx1 =random.randint(450,1100+400)
dovaty1 = random.randint(100,900-50)
dovata2= pygame.image.load('sakura.png')
dovat2 = pygame.transform.scale(dovata2,(50,50))
dovatx2 =random.randint(20+450,1100+400)
dovaty2= random.randint(15+100,900-50)
dovata3 = pygame.image.load('scythe.png')
dovat3 = pygame.transform.scale(dovata3,(40,40))
dovatx3 = random.randint(450,1550-50)
dovaty3 = random.randint(100,900-50)
dovata4=pygame.image.load('shuriken.png')
dovat4 = pygame.transform.scale(dovata4,(40,40))
dovatx4 = random.randint(450,1550-50)
dovaty4 = random.randint(100,900-50)
dovata5 = pygame.image.load('katana (1).png')
dovat5 = pygame.transform.scale(dovata5,(50,50))
dovatx5 = random.randint(450,1550-50)
dovaty5 = random.randint(100,900-50)
dovata6 = pygame.image.load('ninja-shuriken.png')
dovat6 = pygame.transform.scale(dovata6,(40,40))
dovatx6 = random.randint(450,1550-50)
dovaty6 = random.randint(100,900-50)
dovata7 = pygame.image.load('daruma.png')
dovat7 = pygame.transform.scale(dovata7,(40,40))
dovatx7 = random.randint(450,1550-50)
dovaty7 = random.randint(100,900-50)
dovat8 = pygame.transform.scale(dovata7,(40,40))
dovatx8 = random.randint(450,1550-50)
dovaty8 = random.randint(100,900-50)
dovat9 = pygame.transform.scale(dovat1,(40,40))
dovatx9 = random.randint(450,1550-50)
dovaty9 = random.randint(100,900-50)
dovat10 = pygame.transform.scale(dovata2,(40,40))
dovatx10 = random.randint(450,1550-50)
dovaty10 =random.randint(100,900-50)
dovat11 = pygame.transform.scale(dovat3,(40,40))
dovatx11 = random.randint(450,1550-50)
dovaty11 = random.randint(100,900-50)
dovat12 = pygame.transform.scale(dovat4,(40,40))
dovatx12= random.randint(450,1550-50)
dovaty12 = random.randint(100,900-50)
dovat13 = pygame.transform.scale(dovat5,(40,40))
dovatx13 = random.randint(450,1550-50)
dovaty13 = random.randint(100,900-50)
dovat14 = pygame.transform.scale(dovata6,(40,40))
dovatx14 = random.randint(450,1550-50)
dovaty14 = random.randint(100,900-50)
#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10+450
testY = 10+100
#time
time_value = 200
font1= pygame.font.Font('freesansbold.ttf',28)
textx1 = 500+450
texty1 =10+100
#game over

font2= pygame.font.Font('freesansbold.ttf',60)
textx2 =500+450
texty2 =400+100
#game win
font3= pygame.font.Font('freesansbold.ttf',60)
textx3 = 500+450
texty3 =400+100
#mang
mang = pygame.image.load('heart.png')
somang = 3
#restart
restart = pygame.font.Font('freesansbold.ttf',60)
textx4 = 450+450
texty4 = 350+100




# ma tran
tile_size = 50
world_data = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
        [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
        [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],



]
tile_list = []
listmt=[{"xght":0+450,"xghp":70+450,"xmt":10+450,"ymt":110+100,"vmt":2},{"xght":850+450,"xghp":1075+450,"xmt":850+450,"ymt":110+100,"vmt":2},{"xght":850+450,"xghp":1075+450,"xmt":1075+450,"ymt":110+100,"vmt":-2},{"xght":995+450,"xghp":1080+430,"xmt":1080+300,"ymt":610+100,"vmt":-2},{"xght":595+450,"xghp":1015+450,"xmt":1015+450,"ymt":265+100,"vmt":-2},{"xght":595+450,"xghp":1015+450,"xmt":595+450,"ymt":265+100,"vmt":2},{"xght":295+450,"xghp":570+450,"xmt":290+450,"ymt":200+100,"vmt":4},{"xght":351+450,"xghp":452+450,"xmt":452+450,"ymt":10+100,"vmt":2}]
dirt_img = pygame.image.load('brick-wall.png')
abg = pygame.image.load('codfish.png')
row_count = 2
for row in world_data:
        col_count = 9
        for tile in row:
            if tile == 1:
                img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                screen.blit(img, img_rect)

                tile_list.append(tile)
            if tile == 2:
                img = pygame.transform.scale(abg, (tile_size, tile_size))
                img_rect = img.get_rect()
                img_rect.x = col_count * tile_size
                img_rect.y = row_count * tile_size
                tile = (img, img_rect)
                tile_list.append(tile)
            col_count += 1
        row_count += 1

def image_draw( url, xLocal, yLocal, xImg, yImg):  # In ra người hình ảnh
    Img = pygame.image.load(url)
    Img = pygame.transform.scale(Img, (xImg, yImg))  # change size image
    screen.blit(Img, (xLocal, yLocal))
def mov():
    #monters
    for count, i in enumerate(listmt):
        xmt = i["xmt"]
        ymt = i["ymt"]
        xghp= i["xghp"]
        xght= i["xght"]
        vmt= i["vmt"]
        if (count == 6):
            image_draw(linkmt, xmt, ymt, xsizemt+10, ysizemt+10)
            if (xmt >= xghp): vmt = -4
            if (xmt <= xght): vmt = 4
            listmt[count]["xmt"] = xmt + vmt
            listmt[count]["vmt"] = vmt
        else :
            image_draw(linkmt, xmt, ymt, xsizemt,ysizemt)  # In ra monster
            listmt[count]["xmt"] = xmt +vmt # Tiến y vè phía trước
            if (xmt >= xghp ): vmt =-2
            if ( xmt <= xght):vmt=2
            listmt[count]["vmt"]=vmt
def player(x,y):
    screen.blit(playerimg,(x,y))
def dovat(v,x,y):
     screen.blit(v,(x,y))
def khoangcach(a,b,c,d):
    distance = math.sqrt(math.pow((a-c),2)+math.pow((b-d),2))
    if distance < 20:
        return True
    else:
        return False
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False
def show_score(x, y):
    score = font.render("Score : " + str(score_value)+"/15", True, (255, 255, 255))
    screen.blit(score, (x, y))
def show_time(x,y):
    time = font.render("Time :"+ str(int(time_value)),True,(255,255,255))
    screen.blit(time,(x,y))
def show_gameover(x,y):
    gameover = font.render("GAME OVER",True,(255,255,255))
    screen.blit(gameover,(x,y))
def show_win(x,y):
    win = font.render("WIN",True,(255,255,255))
    screen.blit(win,(x,y))

def music( url):
    Sound = mixer.Sound(url)
    Sound.play()
soundbackground=mixer.Sound("Gettin-Down-with-the-Ancients.mp3")
soundbackground.play(-1)
def mangplayer(x,y):
    screen.blit(mang,(x,y))
def canhcua(x,y):
    screen.blit(cua,(x,y))
def show_restart(x,y):
    screen.blit(restart,(x,y))


running = True
while running:

    state=0
    screen.blit(nenimg,(0,0))
    screen.blit(backgroundimg, (450,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            soundbackground.stop()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                 js = 'left.png'
                 playeri = pygame.image.load(js)
                 playerimg = pygame.transform.scale(playeri, (45, 45))
                 changex=- 7
            if event.key == pygame.K_RIGHT:
                 js = 'right.png'
                 playeri = pygame.image.load(js)
                 playerimg = pygame.transform.scale(playeri, (45, 45))
                 changex= 7
            if event.key == pygame.K_UP:
                 changey=-16
                 music("mixkit-quick-jump-arcade-game-239.wav")



        if event.type == KEYUP:
            if event.key == pygame.K_LEFT:
                 changex= 0
            if event.key == pygame.K_RIGHT:
                 changex= 0
            if event.key == pygame.K_UP:
                 changey = 0
            if event.key == pygame.K_DOWN:
                changey= 0




    playerX += changex
    playerY += changey


    if playerX-15 <= 450:
        playerX = 17+450
    elif playerX >= 1100+450:
        playerX = 1100+450-20
    if playerY <= 12+100:
        playerY =12+100
    elif playerY + 50>= 800+100:
        playerY = 900 -50

    changey+=2

#check collíion
    for tile in tile_list:
        if tile[1].colliderect(playerX+changex,playerY,30,30):
            if changex <0:
                changex = tile[1].right-playerX
            elif changex >=0:
                changex = tile[1].left -(playerX+30)


        if tile[1].colliderect(playerX, playerY + changey, 30, 30):
            if changey <0:
                changey =tile[1].bottom - (playerY-10)
            elif changey>=0:
                changey =0
        if tile[1].colliderect(dovatx, dovaty, 64, 64):
            dovatx= random.randint(20+450,1100+450-50)
            dovaty = random.randint(15+100,800)
        if tile[1].colliderect(dovatx1, dovaty1, 64, 64):
            dovatx1= random.randint(20+450,1100+450-50)
            dovaty1 = random.randint(115,800)

        if tile[1].colliderect(dovatx2, dovaty2, 64, 64):
            dovatx2= random.randint(450, 1550-50)
            dovaty2 = random.randint(100, 800)
        if tile[1].colliderect(dovatx3, dovaty3, 64, 64):
            dovatx3= random.randint(450, 1550-50)
            dovaty3 = random.randint(100, 800)
        if tile[1].colliderect(dovatx4, dovaty4, 64, 64):
            dovatx4= random.randint(450, 1550-50)
            dovaty4 = random.randint(100, 800)
        if tile[1].colliderect(dovatx5, dovaty5, 64, 64):
            dovatx5= random.randint(450, 1550-50)
            dovaty5 = random.randint(100, 800)
        if tile[1].colliderect(dovatx6, dovaty6, 40, 40):
            dovatx6= random.randint(450, 1550-50)
            dovaty6 = random.randint(100, 800)
        if tile[1].colliderect(dovatx7, dovaty7, 40, 40):
            dovatx7= random.randint(450, 1550-50)
            dovaty7 = random.randint(100, 800)
        if tile[1].colliderect(dovatx8, dovaty8, 40, 40):
            dovatx8= random.randint(450, 1550-50)
            dovaty8 = random.randint(100, 800)
        if tile[1].colliderect(dovatx9, dovaty9, 40, 40):
            dovatx9= random.randint(450, 1550-50)
            dovaty9 = random.randint(100, 800)
        if tile[1].colliderect(dovatx10, dovaty10, 40, 40):
            dovatx10= random.randint(450, 1550-50)
            dovaty10 = random.randint(100, 800)
        if tile[1].colliderect(dovatx11, dovaty11, 40, 40):
            dovatx11= random.randint(450, 1550-50)
            dovaty11 = random.randint(100, 800)
        if tile[1].colliderect(dovatx12, dovaty12, 40, 40):
            dovatx12= random.randint(450, 1550-50)
            dovaty12 = random.randint(100, 800)
        if tile[1].colliderect(dovatx13, dovaty13, 40, 40):
            dovatx13= random.randint(450, 1550-50)
            dovaty13 = random.randint(100, 800)
        if tile[1].colliderect(dovatx14, dovaty14, 40, 40):
            dovatx14= random.randint(450, 1550-50)
            dovaty14 = random.randint(100, 800)
        if tile[1].colliderect(cuaX,cuaY,64,64):
            cuaX = random.randint(20+450,1000+450-50)
            cuaY = random.randint(10+100,800)

    # kiem tra va cham

    a = khoangcach(playerX,playerY,dovatx,dovaty)
    s = khoangcach(playerX,playerY,dovatx1,dovaty1)
    d = khoangcach(playerX,playerY,dovatx2,dovaty2)
    f = khoangcach(playerX,playerY,dovatx3,dovaty3)
    g = khoangcach(playerX,playerY,dovatx4,dovaty4)
    h = khoangcach(playerX,playerY,dovatx5,dovaty5)
    j = khoangcach(playerX,playerY,dovatx6,dovaty6)
    k = khoangcach(playerX,playerY,dovatx7,dovaty7)
    l = khoangcach(playerX,playerY,dovatx8,dovaty8)
    z = khoangcach(playerX,playerY,dovatx9,dovaty9)
    x = khoangcach(playerX,playerY,dovatx10,dovaty10)
    c = khoangcach(playerX,playerY,dovatx11,dovaty11)
    v = khoangcach(playerX,playerY,dovatx12,dovaty12)
    b = khoangcach(playerX,playerY,dovatx13,dovaty13)
    n = khoangcach(playerX,playerY,dovatx14,dovaty14)
    # toa do chuot

    for tile in tile_list:
        screen.blit(tile[0],tile[1])
    canhcua(cuaX,cuaY)

    player(playerX, playerY)
    sl = [250,290,330]
    for i in range(somang):
        mangplayer(i*32+250+450,4+100)

    dovat(dovati, dovatx, dovaty)
    dovat(dovat1, dovatx1, dovaty1)
    dovat(dovat2, dovatx2, dovaty2)
    dovat(dovat3, dovatx3, dovaty3)
    dovat(dovat4, dovatx4, dovaty4)
    dovat(dovat5, dovatx5, dovaty5)
    dovat(dovat6, dovatx6, dovaty6)
    dovat(dovat7, dovatx7, dovaty7)
    dovat(dovat8, dovatx8, dovaty8)
    dovat(dovat9, dovatx9, dovaty9)
    dovat(dovat10, dovatx10, dovaty10)
    dovat(dovat11, dovatx11, dovaty11)
    dovat(dovat12, dovatx12, dovaty12)
    dovat(dovat13, dovatx13, dovaty13)
    dovat(dovat14, dovatx14, dovaty14)
    choice1=0
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if a:

        state = 1
        screen.blit(cauhoi1, (450, 100))
        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                    music("mixkit-unlock-game-notification-253.wav")
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 1:
                    music("mixkit-unlock-game-notification-253.wav")

                    dovatx=0
                    dovaty=0
                    dovati=pygame.transform.scale(dovati,(0,0))
                    cauhoi1 = pygame.transform.scale(cauhoi1, (0, 0))

                    score_value += 1
                if choice1 == 2:
                    dovatx = random.randint(450,1550-50)
                    dovaty = random.randint(100,800)
                    music("mixkit-player-losing-or-failing-2042.wav")
        changex = 0
        changey = 0
    if s:
        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi2, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450 +100 and mouse_y < 750 +100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 1:
                    dovatx1 = 0
                    dovaty1 = 0
                    dovat1 = pygame.transform.scale(dovat1, (0, 0))
                    cauhoi2 = pygame.transform.scale(cauhoi2, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 2:
                    dovatx1 = random.randint(0+450, 1100+450-50)
                    dovaty1 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")


    if d:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi3, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx2 = 0
                    dovaty2 = 0
                    dovat2 = pygame.transform.scale(dovat2, (0, 0))
                    cauhoi3 = pygame.transform.scale(cauhoi3, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx2 = random.randint(0+450, 1100+450-50)
                    dovaty2 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if f:
        state = 1

        changex = 0
        changey = 0

        screen.blit(cauhoi4, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx3 = 0
                    dovaty3 = 0
                    dovat3 = pygame.transform.scale(dovat3, (0, 0))
                    cauhoi4 = pygame.transform.scale(cauhoi4, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx3 = random.randint(0+450, 1100+450-50)
                    dovaty3 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if g:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi5, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 1:
                    dovatx4 = 0
                    dovaty4 = 0
                    dovat4 = pygame.transform.scale(dovat4, (0, 0))
                    cauhoi5 = pygame.transform.scale(cauhoi5, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 2:
                    dovatx4 = random.randint(0+450, 1100+450-50)
                    dovaty4 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if h:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi6, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx5 = 0
                    dovaty5 = 0
                    dovat5 = pygame.transform.scale(dovat5, (0, 0))
                    cauhoi6 = pygame.transform.scale(cauhoi6, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx5 = random.randint(0+450, 1100+450-50)
                    dovaty5 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if j:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi7, (0+450 ,0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550 +450and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx6 = 0
                    dovaty6 = 0
                    dovat6 = pygame.transform.scale(dovat6, (0, 0))
                    cauhoi7 = pygame.transform.scale(cauhoi7, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx6 = random.randint(0+450, 1100+450-50)
                    dovaty6 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if k:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi8, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450 +100and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 1:
                    dovatx7 = 0
                    dovaty7 = 0
                    dovat7 = pygame.transform.scale(dovat7, (0, 0))
                    cauhoi8 = pygame.transform.scale(cauhoi8, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 2:
                    dovatx7 = random.randint(0+450, 1100+450-50)
                    dovaty7 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if l:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi9, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx8 = 0
                    dovaty8 = 0
                    dovat8 = pygame.transform.scale(dovat8, (0, 0))
                    cauhoi9 = pygame.transform.scale(cauhoi9, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx9 = random.randint(0+450, 1100+450-50)
                    dovaty9 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if z:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi10, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 1:
                    dovatx9 = 0
                    dovaty9 = 0
                    dovat9 = pygame.transform.scale(dovat9, (0, 0))
                    cauhoi10 = pygame.transform.scale(cauhoi10, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 2:
                    dovatx9 = random.randint(0+450, 1100+450-50)
                    dovaty0 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if x:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi11, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx10 = 0
                    dovaty10= 0
                    dovat10 = pygame.transform.scale(dovat10, (0, 0))
                    cauhoi11 = pygame.transform.scale(cauhoi11, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx10 = random.randint(0+450, 1100+450-50)
                    dovaty10 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if c:


        changex = 0
        changey = 0
        state = 1
        screen.blit(cauhoi12, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 1:
                    dovatx11 = 0
                    dovaty11 = 0
                    dovat11 = pygame.transform.scale(dovat11, (0, 0))
                    cauhoi12 = pygame.transform.scale(cauhoi12, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 2:
                    dovatx11 = random.randint(0+450, 1100+450-50)
                    dovaty11 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if v:


        changex = 0
        changey = 0
        state = 1
        screen.blit(cauhoi13, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 1:
                    dovatx12 = 0
                    dovaty12 = 0
                    dovat12 = pygame.transform.scale(dovat12, (0, 0))
                    cauhoi13 = pygame.transform.scale(cauhoi13, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 2:
                    dovatx12 = random.randint(0+450, 1100+450-50)
                    dovaty12 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if b:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi14, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx13 = 0
                    dovaty13 = 0
                    dovat13 = pygame.transform.scale(dovat13, (0, 0))
                    cauhoi14 = pygame.transform.scale(cauhoi14, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx13 = random.randint(0+450, 1100+450-50)
                    dovaty13 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if n:

        state = 1
        changex = 0
        changey = 0

        screen.blit(cauhoi15, (0+450, 0+100))
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if mouse_x > 200+450 and mouse_x < 500+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 1
                if mouse_x > 550+450 and mouse_x < 1000+450 and mouse_y > 450+100 and mouse_y < 750+100:
                    choice1 = 2
                if choice1 == 2:
                    dovatx14 = 0
                    dovaty14 = 0
                    dovat14 = pygame.transform.scale(dovat14, (0, 0))
                    cauhoi15 = pygame.transform.scale(cauhoi15, (0, 0))
                    music("mixkit-unlock-game-notification-253.wav")
                    score_value += 1
                if choice1 == 1:
                    dovatx14 = random.randint(0+450, 1100+450-50)
                    dovaty14 = random.randint(0+100, 800)
                    music("mixkit-player-losing-or-failing-2042.wav")
    if state==0: mov()
    for countmt, mtIteam in enumerate(listmt):
        xmt = mtIteam["xmt"]
        ymt = mtIteam["ymt"]
        abe = khoangcach(playerX,playerY,xmt,ymt)

        if abe:  # nếu nằm giữa
            music("mixkit-player-losing-or-failing-2042.wav")
            listmt.remove(mtIteam)
            somang-=1


            break
    if score_value == 14:
        cua = pygame.image.load('door (1).png')
    xyz = khoangcach(playerX,playerY,cuaX,cuaY)
    if time_value <=0 and score_value <15:
        changex=0
        changey =0
        timechange=0
        time_value=0
        playerimg=pygame.transform.scale(playerimg,(0,0))
        soundbackground.stop()
        music("mixkit-sad-game-over-trombone-471.wav")
        show_gameover(textx2,texty2)

        if event.type == MOUSEBUTTONDOWN:

            if event.button == 1:
                if mouse_x > 900 and mouse_x < 960 and mouse_y > 450 and mouse_y < 480:
                    time_value = 200
                    timechange =0
                    playerimg = pygame.transform.scale(playerimg, (30, 30))
                    player(playerX,playerY)
                    running = True


    elif time_value>0 and score_value>= 14 and xyz:
        changex =0
        changey=0
        timechange=0
        soundbackground.stop()
        music("mixkit-melodic-bonus-collect-1938.wav")
        show_win(textx3,texty3)
    if time_value>0 and score_value>= 13:
        time_value = 30
        timechange = 0.02


    if somang == 0:
        changex = 0
        changey = 0
        timechange = 0
        playerimg = pygame.transform.scale(playerimg, (0, 0))
        soundbackground.stop()
        music("mixkit-sad-game-over-trombone-471.wav")
        show_gameover(textx2, texty2)

    timechange=0.02
    time_value-= timechange

    show_time(textx1,texty1)
    show_score(textX, testY)
    pygame.display.update()
    fpsClock.tick(FPS)
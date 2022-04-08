# phổ biến luật chơi:
'''điều khiển nhân vật để nhặt các đồ trên map,nhân vật phải tránh quái,nếu đụng phỉa quái sẽ mất mạng và con quái cũng sẽ 
biến mất(người chơi có thể lợi dụng điều này để hi sinh một vài mạng để làm giảm độ khó của game) nv có tối đa 3 mạng,hết mạng là thua.
 người chơi phải ăn dc hết số đồ quy định và không bị hết mạng trong thời gian cho phép,nếu ăn dc 13/15 đồ thời gian sẽ chạy ngược về giây thứ 50
 sau đó phải tìm cách ăn dc thứ 14 rồi quay về cổng thì mới win,nếu trong thời gian còn 0 s mà chưa ăn đủ 13/15 đồ thì thua(lưu ý: đồ có thể sẽ 
 trùng màu với nền hay ở vị trí không nhìn ra trong map,người chơi cân nhắc đi tìm đồ và để ý thời gian:))'''
import pygame,sys,math,random,time
from pygame.locals import *
from pygame import mixer
#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 60
pygame.init()


# screen = pygame.display.set_mode((1900, 1060), pygame.RESIZABLE)

screen = pygame.display.set_mode((1920,1080))

background = pygame.image.load('background2.jpg')
#screen_rect = screen.get_rect()

pygame.display.set_caption("Long Bi")
icon = pygame.image.load('tea-cup.png')
pygame.display.set_icon(icon)

# - objects -

cupusp = pygame.image.load('holder2usp.png')
cupsp = pygame.image.load('holder2sp.png')
cup = pygame.image.load('holder2.png')
cupspdamn = pygame.image.load('holder2spdamn.png')
cupx = cup
temp = pygame.image.load('temp1.png')
temp = pygame.transform.scale(temp,(300, 300))

cupImg = pygame.image.load('holder2.png')
cupImg = pygame.transform.scale(cupImg, (300, 300))

rectangleCup = pygame.rect.Rect(450, 760, 100, 100)
rectangleCup_draging = False

# -----------------------------------------------------

towelImg = pygame.image.load('towel.png')
towelImg = pygame.transform.scale(towelImg, (150,150))

rectangleTowel = pygame.rect.Rect(550, 840, 100, 100)
rectangleTowel_draging = False

# -----------------------------------------------------

choiImg = pygame.image.load('choi.png')
choiImg = pygame.transform.scale(choiImg, (150,150))

rectangleChoi = pygame.rect.Rect(650, 790, 60, 70)
rectangleChoi_draging = False

# -----------------------------------------------------

cup2Img = pygame.image.load('holderf.png')
cup2Img = pygame.transform.scale(cup2Img, (300, 300))

rectangleCup2 = pygame.rect.Rect(700, 800, 120, 100)
rectangleCup2_draging = False

# -----------------------------------------------------

spoonImg = pygame.image.load('spoon1.png')
spoonImg = pygame.transform.scale(spoonImg, (150, 150))

rectangleSpoon = pygame.rect.Rect(850, 800, 50, 100)
rectangleSpoon_draging = False

# # -----------------------------------------------------

# scoopImg = pygame.image.load('scoop.png')
# scoopImg = pygame.transform.scale(scoopImg, (200, 200))

# rectangleScoop = pygame.rect.Rect(900, 800, 120, 100)
# rectangleScoop_draging = False

# -----------------------------------------------------  <green tea>

trayImg = pygame.image.load('combine.png')
trayImg = pygame.transform.scale(trayImg, (400, 400))

rectangleTray = pygame.rect.Rect(1175, 800, 200, 100)
rectangleTray_draging = False

# -----------------------------------------------------

ferImg = pygame.image.load('fer.png')
ferImg = pygame.transform.scale(ferImg, (150,150))

rectangleFer = pygame.rect.Rect(320, 790, 60, 50)
rectangleFer_draging = False

# -----------------------------------------------------

gasImg = pygame.image.load('gas_stove.png')
gasImg = pygame.transform.scale(gasImg, (300, 300))

rectangleGas = pygame.rect.Rect(1450, 800, 170, 120)
rectangleGas_draging = False

# -----------------------------------------------------

greenImg = pygame.image.load('green tea.png')
greenImg = pygame.transform.scale(greenImg, (150, 150))

rectangleGreen = pygame.rect.Rect(450, 900, 50, 60)
rectangleGreen_draging = False

# -----------------------------------------------------

potImg = pygame.image.load('teapot2.png')
potImg = pygame.transform.scale(potImg, (150, 150))

rectanglePot = pygame.rect.Rect(940, 750, 150, 170)
rectanglePot_draging = False

# -----------------------------------------------------

boxImg = pygame.image.load('paper.png')
boxImg = pygame.transform.scale(boxImg, (150, 150))

rectangleBox = pygame.rect.Rect(330-30, 900-30, 70, 50)
rectangleBox_draging = False

# -----------------------------------------------------

paperImg = pygame.image.load('tissue-paper.png')
paperImg = pygame.transform.scale(paperImg, (150, 150))
rectanglePaper = pygame.rect.Rect(330, 900, 70, 50)
rectanglePaper.x = 330
rectanglePaper.y = 900

# -----------------------------------------------------

font1 = pygame.font.Font('freesansbold.ttf', 20)
bigger_text = font1.render('ready', True, (255, 255 ,255))
lala = font1.render("You've just: ", True, (255, 191, 0))

# -----------------------------------------------------

okImg = pygame.image.load('ok.png')
okImg = pygame.transform.scale(okImg, (600, 600))

# -----------------------------------------------------

kingImg = pygame.image.load('king.png')
kingImg = pygame.transform.scale(kingImg, (900, 900))
# - mainloop -
time = 0
# clock = pygame.time.Clock()
potx = 0
step = -1
statet = 1
running = True
get_state = True
score = 0;
plus = 0;
score_state = True
if statet == 1:
 while running:
    mixer.music.load('background.wav')
    mixer.music.play(-1)
    time += 0.02
    # print(time)
    if step == -1:
        screen.blit(background, (0, 100))
        screen.blit(kingImg, (520, -350))
        hoho = font1.render("Welcome to the magician tea making academy", True, (0, 0, 0))
        hihi = font1.render("Whenever ''ready'' appears, click the right mouse button", True, (0, 0, 0))
        haha = font1.render("There is 1 hint each action if you can't find out the way by yourself" , True, (0, 0, 0))
        screen.blit(hoho, (650,150))
        screen.blit(hihi, (650,200))
        screen.blit(haha, (650,250))
        step_state = "ready"
    if step == 0:
        screen.blit(background, (0, 100))
        screen.blit(kingImg, (520, -350))
        hoho = font1.render("Each action you have 15s to find the right way", True, (0, 0, 0))
        hihi = font1.render("If you find the right way before the hint appears, you can get score", True, (0, 0, 0))
        haha = font1.render("Have fun, Enjoy the game and PEACE" , True, (0, 0, 0))
        screen.blit(hoho, (650,150))
        screen.blit(hihi, (650,200))
        screen.blit(haha, (650,250))
        step_state = "ready"        
    elif step == 1:
        if get_state == True:
            get_time = time
            get_state = False
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Genuflected", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Use towel to clean something ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 1 and rectangleCup.x <= rectangleTowel.x and rectangleTowel.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleTowel.y and rectangleTowel.y > rectangleCup.y - 50:
            cupusp = pygame.image.load('holder2u.png')
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False

    elif step == 2:
        if get_state == True:
            get_time = time
            get_state = False           
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Wiped the cup", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("May spoon need it too ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 2 and rectangleSpoon.x -50 <= rectangleTowel.x and rectangleTowel.x <= rectangleSpoon.x + 50 and rectangleSpoon.y + 50 >  rectangleTowel.y  and rectangleTowel.y > rectangleSpoon.y - 50:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 3:
        if get_state == True:
            get_time = time
            get_state = False             
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Wiped the spoon", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Prepare the water ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 3 and rectangleGas.x -30 <= rectanglePot.x and rectanglePot.x <= rectanglePot.x + 30 and rectangleGas.y >  rectanglePot.y and rectanglePot.y > rectangleGas.y - 130:
            if time >= (get_time + 3):
                # potImg = pygame.image.load('teapot2f.png')
                # potImg = pygame.transform.scale(potImg, (300, 300))
                temp = pygame.image.load('temp3.png')
                temp = pygame.transform.scale(temp,(300, 300))
                step_state = "ready" 
                if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                    score += (get_time + 15 - time)*20
                    score_state = False 
    elif step == 4:
        if get_state == True:
            get_time = time
            get_state = False  
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Boiled water", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("You can't make tea in 100 degree C water ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 4 and rectangleTray.x <= rectanglePot.x and rectanglePot.x <= rectangleTray.x + 70 and rectangleTray.y >  rectanglePot.y and rectanglePot.y > rectangleTray.y - 130:
            temp = pygame.image.load('temp2.png')
            temp = pygame.transform.scale(temp,(300, 300))
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 5:
        if get_state == True:
            get_time = time
            get_state = False            
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Kept the pot warm", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Now clean the cup with water ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 5 and rectangleCup.x < rectanglePot.x and rectanglePot.x <= rectangleCup.x + 100 and rectangleCup.y - 200 >  rectanglePot.y and rectanglePot.y > rectangleCup.y - 250:
            cupImg = cupsp
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 6:
        if get_state == True:
            get_time = time
            get_state = False
        screen.blit(background, (0, 0))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Now with brush ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 6 and rectangleCup.x <= rectangleChoi.x and rectangleChoi.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleChoi.y and rectangleChoi.y > rectangleCup.y - 50:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 7:
        if get_state == True:
            get_time = time
            get_state = False            
        screen.blit(background, (0, 0))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Pour excess water ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 7 and rectangleCup2.x < rectangleCup.x and rectangleCup.x <= rectangleCup2.x + 100 and rectangleCup2.y - 150 >  rectangleCup.y and rectangleCup.y > rectangleCup2.y - 200:
            cupImg = cup
            cupx = cup
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 8:
        if get_state == True:
            get_time = time
            get_state = False  
        screen.blit(background, (0, 0))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Wipe the cup ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 8 and rectangleCup.x <= rectangleBox.x and rectangleBox.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleBox.y and rectangleBox.y > rectangleCup.y - 50:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 9:
        if get_state == True:
            get_time = time
            get_state = False  
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Cleaned the cup", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Now find and make tea ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 9 and rectangleGreen.x - 30 <= rectangleSpoon.x and rectangleSpoon.x <= rectangleGreen.x + 50 and rectangleGreen.y >  rectangleSpoon.y and rectangleSpoon.y > rectangleGreen.y - 50:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 10:
        if get_state == True:
            get_time = time
            get_state = False  
        screen.blit(background, (0, 0))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Make tea ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 10 and rectangleCup.x <= rectangleSpoon.x and rectangleSpoon.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleSpoon.y and rectangleSpoon.y > rectangleCup.y - 100:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 11:
        if get_state == True:
            get_time = time
            get_state = False
        screen.blit(background, (0, 0))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("We need a little water ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 11 and rectangleCup.x < rectanglePot.x and rectanglePot.x <= rectangleCup.x + 100 and rectangleCup.y - 200 >  rectanglePot.y and rectanglePot.y > rectangleCup.y - 250:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 12:
        if get_state == True:
            get_time = time
            get_state = False
        screen.blit(background, (0, 0))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Now you are really making tea ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 12 and rectangleCup.x <= rectangleChoi.x and rectangleChoi.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleChoi.y and rectangleChoi.y > rectangleCup.y - 50:            
            cupImg = cupspdamn
            cupx = cupspdamn
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 13:
        if get_state == True:
            get_time = time
            get_state = False
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Made tea", True, (255, 255, 255))
        ej = font1.render("Now just enjoy your tea", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        screen.blit(ej, (1440, 235))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Bring the box to the right spot to get the candy ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 13 and rectangleFer.x >= 500 and rectangleFer.y <= 700:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20 
                score_state = False 
    elif step == 14: 
        if get_state == True:
            get_time = time
            get_state = False   
        screen.blit(background, (0, 0))
        if step == 14 and rectangleFer.x >= 500 and rectangleFer.y <= 700:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 15:
        if get_state == True:
            get_time = time
            get_state = False            
        screen.blit(background, (0, 0))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("Now drink your tea ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))
        if step == 15 and rectangleCup.x >=700 and rectangleCup.x <= 1150 and rectangleCup.y>=850:
            cupImg = cup
            cupx = cup
            step_state = "ready" 
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20 
                score_state = False 
    elif step == 16:
        if get_state == True:
            get_time = time
            get_state = False            
        screen.blit(background, (0, 0))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Now clean the cup!", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        if time >= (get_time + 15) and step_state == "false":
            screen.blit(kingImg, (520, -350))
            hoho = font1.render("From here, no more hint, find out the way by yourself ...", True, (0, 0, 0))
            screen.blit(hoho, (750,200))            
        if step == 16 and rectangleCup.x < rectanglePot.x and rectanglePot.x <= rectangleCup.x + 100 and rectangleCup.y - 200 >  rectanglePot.y and rectanglePot.y > rectangleCup.y - 250:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 17:
        if get_state == True:
            get_time = time
            get_state = False 
        screen.blit(background, (0, 0))
        if step == 17 and rectangleCup.x <= rectangleChoi.x and rectangleChoi.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleChoi.y and rectangleChoi.y > rectangleCup.y - 50:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 18:
        if get_state == True:
            get_time = time
            get_state = False 
        screen.blit(background, (0, 0))
        if step == 18 and rectangleCup2.x < rectangleCup.x and rectangleCup.x <= rectangleCup2.x + 100 and rectangleCup2.y - 150 >  rectangleCup.y and rectangleCup.y > rectangleCup2.y - 200:
            cupImg = cup
            cupx = cup
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 19:
        if get_state == True:
            get_time = time
            get_state = False 
        screen.blit(background, (0, 0))
        if step == 19 and rectangleCup.x <= rectangleBox.x and rectangleBox.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleBox.y and rectangleBox.y > rectangleCup.y - 50:
            step_state = "ready"
            if (get_time + 15 - time) > 0 and (get_time + 15 - time) < 15 and score_state == True:
                score += (get_time + 15 - time)*20
                score_state = False 
    elif step == 20:
        screen.blit(background, (0, -100))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Genuflected", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        step_state = "ready"
    elif step == 21:
        screen.blit(background, (0, 100))
        screen.blit(okImg, (1300, -280 ))
        mid_text = font1.render("Stood up", True, (255, 255, 255))
        screen.blit(mid_text, (1500, 190))
        step_state = "ready"
    if step == 22:
        fake = pygame.image.load('fake.jpg')
        fake = pygame.transform.scale(fake, (1800, 1000))
        screen.blit(fake, (0,0))

        step_state = "ready"
        screen.blit(kingImg, (520, -350))
        hihi = font1.render("congratulations, you get " + str(math.floor(score)) +   ", now we move on to the next game", True, (0, 0, 0))
        screen.blit(hihi, (650,200))
        step_state = "ready"
    elif step == 23:
        running = False
        statet+=1

    # - events -
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.VIDEORESIZE:
        #     window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
# ---------------------------------------------------------
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
            # cup:
                if rectangleCup.collidepoint(event.pos):
                    rectangleCup_draging = True
                    mouseCup_x, mouseCup_y = event.pos
                    offsetCup_x = rectangleCup.x - mouseCup_x
                    offsetCup_y = rectangleCup.y - mouseCup_y
            # towel:
                elif rectangleTowel.collidepoint(event.pos):
                    rectangleTowel_draging = True
                    mouseTowel_x, mouseTowel_y = event.pos
                    offsetTowel_x = rectangleTowel.x - mouseTowel_x
                    offsetTowel_y = rectangleTowel.y - mouseTowel_y
            # choi:
                elif rectangleChoi.collidepoint(event.pos):
                    rectangleChoi_draging = True
                    mouseChoi_x, mouseChoi_y = event.pos
                    offsetChoi_x = rectangleChoi.x - mouseChoi_x
                    offsetChoi_y = rectangleChoi.y - mouseChoi_y
            # cup2:
                elif rectangleCup2.collidepoint(event.pos):
                    rectangleCup2_draging = True
                    mouseCup2_x, mouseCup2_y = event.pos
                    offsetCup2_x = rectangleCup2.x - mouseCup2_x
                    offsetCup2_y = rectangleCup2.y - mouseCup2_y
            # spoon:
                elif rectangleSpoon.collidepoint(event.pos):
                    rectangleSpoon_draging = True
                    mouseSpoon_x, mouseSpoon_y = event.pos
                    offsetSpoon_x = rectangleSpoon.x - mouseSpoon_x
                    offsetSpoon_y = rectangleSpoon.y - mouseSpoon_y
            # # scoop:
            #     elif rectangleScoop.collidepoint(event.pos):
            #         rectangleScoop_draging = True
            #         mouseScoop_x, mouseScoop_y = event.pos
            #         offsetScoop_x = rectangleScoop.x - mouseScoop_x
            #         offsetScoop_y = rectangleScoop.y - mouseScoop_y
            # Tray:
                elif rectangleTray.collidepoint(event.pos):
                    rectangleTray_draging = True
                    mouseTray_x, mouseTray_y = event.pos
                    offsetTray_x = rectangleTray.x - mouseTray_x
                    offsetTray_y = rectangleTray.y - mouseTray_y
            # fer:
                elif rectangleFer.collidepoint(event.pos):
                    rectangleFer_draging = True
                    mouseFer_x, mouseFer_y = event.pos
                    offsetFer_x = rectangleFer.x - mouseFer_x
                    offsetFer_y = rectangleFer.y - mouseFer_y
            # Gas:
                elif rectangleGas.collidepoint(event.pos):
                    rectangleGas_draging = True
                    mouseGas_x, mouseGas_y = event.pos
                    offsetGas_x = rectangleGas.x - mouseGas_x
                    offsetGas_y = rectangleGas.y - mouseGas_y
            # Green:
                elif rectangleGreen.collidepoint(event.pos):
                    rectangleGreen_draging = True
                    mouseGreen_x, mouseGreen_y = event.pos
                    offsetGreen_x = rectangleGreen.x - mouseGreen_x
                    offsetGreen_y = rectangleGreen.y - mouseGreen_y
            # Pot:
                elif rectanglePot.collidepoint(event.pos):
                    rectanglePot_draging = True
                    mousePot_x, mousePot_y = event.pos
                    offsetPot_x = rectanglePot.x - mousePot_x
                    offsetPot_y = rectanglePot.y - mousePot_y
            # Box:
                elif rectangleBox.collidepoint(event.pos):
                    rectangleBox_draging = True
                    mouseBox_x, mouseBox_y = event.pos
                    offsetBox_x = rectangleBox.x - mouseBox_x
                    offsetBox_y = rectangleBox.y - mouseBox_y
            if event.button == 3 and step_state == "ready":
                if step == 0:                   # các level chỉnh theo step này.
                # cup: 
                    rectangleCup.y -= 100
                # towel:
                    rectangleTowel.y -= 100
                # choi:
                    rectangleChoi.y -= 100
                # cup2:
                    rectangleCup2.y -= 100
                # spoon:
                    rectangleSpoon.y -= 100
                # # Scoop:
                #     rectangleScoop.y -= 100
                # Tray:
                    rectangleTray.y -= 100
                # Fer:
                    rectangleFer.y -= 100
                # Gas:
                    rectangleGas.y -= 100
                # Green:
                    rectangleGreen.y -= 100
                # Pot:
                    rectanglePot.y -= 100
                # Box:
                    rectangleBox.y -= 100
                # paper:
                    rectanglePaper.y -= 100
                elif step == 19:
                                        # cup: 
                    rectangleCup.y -= 100
                # towel:
                    rectangleTowel.y -= 100
                # choi:
                    rectangleChoi.y -= 100
                # cup2:
                    rectangleCup2.y -= 100
                # spoon:
                    rectangleSpoon.y -= 100
                # # Scoop:
                #     rectangleScoop.y -= 100
                # Tray:
                    rectangleTray.y -= 100
                # Fer:
                    rectangleFer.y -= 100
                # Gas:
                    rectangleGas.y -= 100
                # Green:
                    rectangleGreen.y -= 100
                # Pot:
                    rectanglePot.y -= 100
                # Box:
                    rectangleBox.y -= 100
                # paper:
                    rectanglePaper.y -= 100
                elif step == 20:
                                        # cup: 
                    rectangleCup.y += 200
                # towel:
                    rectangleTowel.y += 200
                # choi:
                    rectangleChoi.y += 200
                # cup2:
                    rectangleCup2.y += 200
                # spoon:
                    rectangleSpoon.y += 200
                # # Scoop:
                #     rectangleScoop.y += 200
                # Tray:
                    rectangleTray.y += 200
                # Fer:
                    rectangleFer.y += 200
                # Gas:
                    rectangleGas.y += 200
                # Green:
                    rectangleGreen.y += 200
                # Pot:
                    rectanglePot.y += 200
                # Box:
                    rectangleBox.y += 200
                # paper:
                    rectanglePaper.y += 200
                step_state = "false"
                get_state = True
                score_state = True
                step += 1 
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:           
            # cup: 
                rectangleCup_draging = False
            # towel:
                rectangleTowel_draging = False
            # choi:
                rectangleChoi_draging = False
            # cup2:
                rectangleCup2_draging = False
            # Spoon:
                rectangleSpoon_draging = False
            # # Scoop:
            #     rectangleScoop_draging = False
            # Tray:
                rectangleTray_draging = False
            # Fer:
                rectangleFer_draging = False
            # Gas:
                rectangleGas_draging = False
            # Green:
                rectangleGreen_draging = False
            # Pot:
                rectanglePot_draging = False
            # Box:
                rectangleBox_draging = False

        elif event.type == pygame.MOUSEMOTION:
            # cup:
            if rectangleCup_draging:
                mouseCup_x, mouseCup_y = event.pos
                rectangleCup.x = mouseCup_x + offsetCup_x
                rectangleCup.y = mouseCup_y + offsetCup_y
            # towel:
            elif rectangleTowel_draging:
                mouseTowel_x, mouseTowel_y = event.pos
                rectangleTowel.x = mouseTowel_x + offsetTowel_x
                rectangleTowel.y = mouseTowel_y + offsetTowel_y    
            # choi:
            elif rectangleChoi_draging:
                mouseChoi_x, mouseChoi_y = event.pos
                rectangleChoi.x = mouseChoi_x + offsetChoi_x
                rectangleChoi.y = mouseChoi_y + offsetChoi_y
            # cup2:
            elif rectangleCup2_draging:
                mouseCup2_x, mouseCup2_y = event.pos
                rectangleCup2.x = mouseCup2_x + offsetCup2_x
                rectangleCup2.y = mouseCup2_y + offsetCup2_y 
            # Spoon:
            elif rectangleSpoon_draging:
                mouseSpoon_x, mouseSpoon_y = event.pos
                rectangleSpoon.x = mouseSpoon_x + offsetSpoon_x
                rectangleSpoon.y = mouseSpoon_y + offsetSpoon_y
            # # Scoop:
            # elif rectangleScoop_draging:
            #     mouseScoop_x, mouseScoop_y = event.pos
            #     rectangleScoop.x = mouseScoop_x + offsetScoop_x
            #     rectangleScoop.y = mouseScoop_y + offsetScoop_y
            # Tray:
            elif rectangleTray_draging:
                mouseTray_x, mouseTray_y = event.pos
                rectangleTray.x = mouseTray_x + offsetTray_x
                rectangleTray.y = mouseTray_y + offsetTray_y 
            # Fer:
            elif rectangleFer_draging:
                mouseFer_x, mouseFer_y = event.pos
                rectangleFer.x = mouseFer_x + offsetFer_x
                rectangleFer.y = mouseFer_y + offsetFer_y
            # Gas:
            elif rectangleGas_draging:
                mouseGas_x, mouseGas_y = event.pos
                rectangleGas.x = mouseGas_x + offsetGas_x
                rectangleGas.y = mouseGas_y + offsetGas_y 
            # Green:
            elif rectangleGreen_draging:
                mouseGreen_x, mouseGreen_y = event.pos
                rectangleGreen.x = mouseGreen_x + offsetGreen_x
                rectangleGreen.y = mouseGreen_y + offsetGreen_y 
            # Pot:
            elif rectanglePot_draging:
                mousePot_x, mousePot_y = event.pos
                rectanglePot.x = mousePot_x + offsetPot_x
                rectanglePot.y = mousePot_y + offsetPot_y
            # Box:
            elif rectangleBox_draging:
                mouseBox_x, mouseBox_y = event.pos
                rectangleBox.x = mouseBox_x + offsetBox_x
                rectangleBox.y = mouseBox_y + offsetBox_y
    # change and level
    if step_state == "ready":
           screen.blit(bigger_text, (0,0))
        # cup:

    if (step == 7 or step == 18) and (rectangleCup2.x < rectangleCup.x and rectangleCup.x <= rectangleCup2.x + 100 and rectangleCup2.y - 150 >  rectangleCup.y and rectangleCup.y > rectangleCup2.y - 200):
        cupImg = pygame.image.load('holder2aaa.png')
        cupImg = pygame.transform.scale(cupImg, (300, 300))
    else:
        if cupx == cupsp:
            cupImg = cupsp
        elif cupx == cupspdamn:
            cupImg = cupspdamn
        else:
            cupImg = cup
        cupImg = pygame.transform.scale(cupImg, (300, 300))

        # Spoon

    if step == 10 and rectangleCup.x <= rectangleSpoon.x and rectangleSpoon.x <= rectangleCup.x + 50 and rectangleCup.y >  rectangleSpoon.y and rectangleSpoon.y > rectangleCup.y - 100:
        spoonImg = pygame.image.load('spoon.png')
        spoonImg = pygame.transform.scale(spoonImg, (100, 100))
    else:
        spoonImg = pygame.image.load('spoon1.png')
        spoonImg = pygame.transform.scale(spoonImg, (100, 100))

        # cupu:
    if (step == 7 or step == 18) and (rectangleCup2.x < rectangleCup.x and rectangleCup.x <= rectangleCup2.x + 100 and rectangleCup2.y - 150 >  rectangleCup.y and rectangleCup.y > rectangleCup2.y - 200):
        cupuImg = pygame.image.load('holder2au.png')
        cupuImg = pygame.transform.scale(cupuImg, (300, 300))
    else:
        cupuImg = cupusp
        cupuImg = pygame.transform.scale(cupuImg, (300, 300))

        # pot:
    if (step == 5 or step == 11 or step == 16) and (rectangleCup.x < rectanglePot.x and rectanglePot.x <= rectangleCup.x + 100 and rectangleCup.y - 200 >  rectanglePot.y and rectanglePot.y > rectangleCup.y - 250):
        potImg = pygame.image.load('teapot2aaaf.png')
        potImg = pygame.transform.scale(potImg, (300, 300))

        cupImg = cupsp
        cupx = cupsp
        cupImg = pygame.transform.scale(cupImg, (300, 300))
    else:
        if rectangleGas.x -30 <= rectanglePot.x and rectanglePot.x <= rectanglePot.x + 30 and rectangleGas.y >  rectanglePot.y and rectanglePot.y > rectangleGas.y - 130 and time >= (get_time + 3) and step == 3:
            potx = 1
        if potx == 1:
            potImg = pygame.image.load('teapot2f.png')
            potImg = pygame.transform.scale(potImg, (300, 300))
        else:
            potImg = pygame.image.load('teapot2.png')
            potImg = pygame.transform.scale(potImg, (300, 300))    



    # check ========================================
    # pygame.draw.rect(screen, RED, rectangleCup)
    # pygame.draw.rect(screen, RED, rectangleTowel)
    # pygame.draw.rect(screen, RED, rectangleChoi)
    # pygame.draw.rect(screen, RED, rectangleCup2)
    # pygame.draw.rect(screen, RED, rectangleSpoon)

    # pygame.draw.rect(screen, RED, rectangleTray)
    # pygame.draw.rect(screen, RED, rectangleFer)
    # pygame.draw.rect(screen, RED, rectangleGas)
    # pygame.draw.rect(screen, RED, rectangleGreen)
    # pygame.draw.rect(screen, RED, rectanglePot)
    # pygame.draw.rect(screen, RED, rectangleBox)    
    # ================================================

    # screen.blit(scoopImg, (rectangleScoop.x-100, rectangleScoop.y-100))
    if step<=21:
        screen.blit(ferImg, (rectangleFer.x-30, rectangleFer.y-50))
        screen.blit(cup2Img, (rectangleCup2.x-100, rectangleCup2.y-100))
        screen.blit(cupImg, (rectangleCup.x-100, rectangleCup.y-100))
        screen.blit(spoonImg, (rectangleSpoon.x-30, rectangleSpoon.y-0))
        screen.blit(choiImg, (rectangleChoi.x-50, rectangleChoi.y-40))    
        screen.blit(boxImg, (rectangleBox.x-50 + 30 , rectangleBox.y-60 + 30))
        screen.blit(cupuImg, (rectangleCup.x-100, rectangleCup.y-100))
        screen.blit(towelImg, (rectangleTowel.x-5, rectangleTowel.y-30))
        screen.blit(trayImg, (rectangleTray.x-120, rectangleTray.y-140))
        screen.blit(gasImg, (rectangleGas.x-60, rectangleGas.y-110))
        screen.blit(greenImg, (rectangleGreen.x-55, rectangleGreen.y-60))
        screen.blit(potImg, (rectanglePot.x-90, rectanglePot.y-60))
        screen.blit(paperImg, (rectanglePaper.x -50, rectanglePaper.y-60))
        screen.blit(temp, (1500,350))
    if step_state == "ready":
        screen.blit(bigger_text, (200, 120))
    if (step >= 1 and step <=5) or step == 9 or step == 13 or step == 16 or step == 20 or step == 21:
        screen.blit(lala, (1500, 150))
    if step == 13 and rectangleFer.x >= 500 and rectangleFer.y <= 700:
        candyImg = pygame.image.load('candy.png')
        candyImg = pygame.transform.scale(candyImg, (1000, 1000))
        screen.blit(candyImg, (rectangleFer.x-400, rectangleFer.y-400))
    if step == 14 and rectangleFer.x >= 500 and rectangleFer.y <= 700:
        candyImg = pygame.image.load('candy2.png')
        candyImg = pygame.transform.scale(candyImg, (1000, 1000))
        screen.blit(candyImg, (rectangleFer.x-400, rectangleFer.y-400))

    if step == 15 and rectangleCup.x >=700 and rectangleCup.x <= 1150 and rectangleCup.y>=850:
        cupImg = pygame.image.load('holder2m.png')
        cupImg = pygame.transform.scale(cupImg, (2000, 2000))
        screen.blit(cupImg, (rectangleCup.x-800, rectangleCup.y-800))
    # print(score)
    pygame.display.flip()

    # - constant game speed / FPS -

    # clock.tick(FPS)

# - end -
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
playeri = pygame.image.load('right.png')
playerimg = pygame.transform.scale(playeri,(45,45))
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
sizestart = 90
start = pygame.font.Font('freesansbold.ttf',sizestart)
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
    start1 = start.render("start",True,(0,0,0))
    screen.blit(start1,(x,y))


running = True
state1 = 1
if statet == 2:
 while running :


    state=0
    screen.blit(nenimg,(0,0))
    screen.blit(backgroundimg, (450,100))
    for event in pygame.event.get():
        if event.type == QUIT:
            soundbackground.stop()
            running = False
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                 changex=- 7
                 playeri = pygame.image.load('left.png')
                 playerimg = pygame.transform.scale(playeri, (45, 45))
            if event.key == pygame.K_RIGHT:
                 changex= 7
                 playeri = pygame.image.load('right.png')
                 playerimg = pygame.transform.scale(playeri, (45, 45))
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
                changey =tile[1].bottom - playerY
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


    elif  xyz:
        changex =0
        changey=0
        timechange=0
        soundbackground.stop()
        music("mixkit-melodic-bonus-collect-1938.wav")
        show_win(textx3,texty3)
        statet += 1
        running = False
        choi = True

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
        running = False
        statet = 1
    if state1 ==1:
        screen.blit(nenimg, (0, 0))
        show_restart(textx4, texty4)
        if event.type == MOUSEBUTTONDOWN:
         if event.button == 1:
            if mouse_x > 899 and mouse_x < 900 + 300 and mouse_y > 450  and mouse_y < 450 + 100:
                state1 = 2





    timechange=0.02
    time_value-= timechange



    show_time(textx1,texty1)
    show_score(textX, testY)
    pygame.display.update()
    fpsClock.tick(FPS)


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
run=False
#nv1
xsizenv1=110#chieu cao
ysizenv1 =110   #chieu rong
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
stated=1
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
if statet == 3:
 run = True
 state1 = 1
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
    if state1 ==1:
        image_draw(linkbg, 0, 0, xscreen, yscreen)
        show_restart(textx4,texty4)
        mouse_x , mouse_y = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
         if event.button == 1:
            if mouse_x > 899 and mouse_x < 900 + 300 and mouse_y > 450  and mouse_y < 450 + 100:
                state1 = 2
    pygame.display.update()  # Update
    clock = pygame.time.Clock()
    clock.tick(75*state)




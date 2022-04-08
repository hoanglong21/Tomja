
import pygame
import math
from pygame import mixer
#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 60

pygame.init()

mixer.music.load('background.wav')
mixer.music.play(-1)
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

gasImg = pygame.image.load('gasf2.png')
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
running = True
get_state = True
score = 0
plus = 0
score_state = True
count = 0
while running:
    count += 0.25
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
    if (count%2==0):
        gasImg = pygame.image.load('gasf2.png')
        gasImg = pygame.transform.scale(gasImg, (300, 300))
    else:
        gasImg = pygame.image.load('gasf.png')
        gasImg = pygame.transform.scale(gasImg, (300, 300))

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
    if (step >= 1 and step <=5) or step == 9 or step == 13 or step == 20 or step == 21:
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

pygame.quit()

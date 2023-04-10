import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((1200, 550))
display_surface = pygame.display.set_mode((1200, 668))
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
door = pygame.image.load('cdoor.png')
background = pygame.image.load('background.jpg')
car=pygame.image.load('redcar.png')
running = True
offset = 43
doorr = []
j = 0
xx=0
di=0
rest=0
flag = 0
MouseX=0
MouseY=0
n1=0
r1=0
fl=0
n=0
d=8
press=False
d2=0
sk=0
dd=0
fina=0
car_id=0
h=True
open_door = pygame.image.load('open_.png')
redcar = pygame.image.load('redcar.png')
goat=pygame.image.load('goat.png')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Enter No of doors you to play the game', True, green, blue)
textRect = text.get_rect()
text1 = font.render('Press 1 to switch and 2 to Stay', True, green, blue)
textRect = text1.get_rect()
X=1200
Y=668
t1=0
ddd=0
press=False
t=True
textRect.center = (X // 2, Y // 2)
while running:
    screen.blit(background, (0, 0))
    if t == True:
        display_surface.blit(text, textRect)

    if h == True:
      for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key== pygame.K_4:
                n = 4
                d = 1
                fl=1
                t=False
                h = False
            if event.key == pygame.K_6:
              n=6
              d=1
              fl=1
              t = False
              h = False
            if event.key == pygame.K_3:
              n=3
              d=1
              fl=1
              t = False
              h = False
            if event.key == pygame.K_5:
              n=5
              d=1
              fl=1
              t = False
              h = False
    #print(n)

    if d== 1:
      for i in range(n):
        screen.blit(door, (i * 43 + i * 143 + 43, 220))
        sum = i * 43 + i * 143 + 43
        #print(sum)
        doorr.insert(i, sum)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:

            pos = pygame.mouse.get_pos()
            btn = pygame.mouse
            #print("x = {}, y = {}".format(pos[0], pos[1]))
            pp = pos[0]
            press=True
            xx=173
            if pp > 43+xx and pp < 229+xx:
                d2 = 1
            if pp > 229+xx and pp < 415+xx:
                d2 = 2
            if pp > 415+xx and pp < 601+xx:
                d2 = 3
            if pp > 601+xx and pp < 787+xx:
                d2 = 4
            if pp > 787+xx and pp < 973+xx:
                d2 = 5
            if pp>973+xx:
                d2=6
            if fl == 1:
                r1 = random.randint(1, n)
                print(r1)
                print(d2)
                t1=r1
                ss = r1*43 + r1 * 143 + 43
            if r1 == d2:
                fina=1
                if d2+1 < n:
                  d2=d2+1
                else:
                  d2=d2-1
                print("same")
            sk = ss
            fl = 0
            #print(r1)
            dd = d2 * 43 + d2 * 143 + 43
            flag=1
            d=3
    j=0
    if flag == 1:
        screen.blit(background, (0, 0))
        for i in doorr:
            j=j+1
            #print(i)
            #print("Position is ",pos[0])
            if i!=dd and i!=ss:

             screen.blit(goat, (i+5, 300))
             screen.blit(open_door, (i, 220))

        for i in range(n):
         sum = i * 43 + i * 143 + 43
         if  sum==dd or sum==sk:
            screen.blit(door, (i * 43 + i * 143 + 43, 220))

    if press == True:
        text1 = font.render('Press 1 to switch and 2 to Stay', True, green, blue)
        textRect = text1.get_rect()
        display_surface.blit(text1, textRect)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_1:
                    if fina == 1:
                        dd=100
                    else:
                      di = 1
                      ddd = 1
                    press=False
                if event.key == pygame.K_2:
                  if fina ==1:
                     di=1
                     ddd=1
                  else:
                   dd=-100
                   rest = rest + 1
                  press=False

    if dd==-100:
        rest = rest + 1
    if ddd==1:
        screen.blit(door, (ss, 220))
    if di ==1:

        r1=t1
        sk=0
        ddd=0
        if fina==1:

            text2 = font.render('You Won By staying', True, green, blue)
            display_surface.blit(text2, textRect)
            rest = rest + 1
        else:

            text2 = font.render('You Won By switching', True, green, blue)
            display_surface.blit(text2, textRect)
            textRect = text2.get_rect()
            su = t1 * 43 + t1 * 143 + 43
            screen.blit(car,(su,220))
            rest=rest+1
            screen.blit(open_door, (su, 220))

    if rest==4:
      time.sleep(5)
      exec(open("./main.py").read())


        #
    #print(d2)
    #print(r1)
    pygame.display.update()

# 3 doors-> 3 and 1
# 4 doors-> 4 amd 2
#DEVELOPED BY PIDDI AND ANGRRRY BIIRRDDD
#SPECIAL THANKS TO ANGRY BIRD FOR IMPROVING THE SMOOTHNESS OF THE GAME HENCE GIVING BETTER GAMEPLAY EXPERIENCE
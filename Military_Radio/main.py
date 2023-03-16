import pygame
from pygame.locals import *
import random
import time
import threading
import os   
pygame.init
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate",100)
pygame.font.init()
display_width = 1600
display_height = 900
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Forgószelek by:ForstyWolfDEV')
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue=(0,0,255)
green=(0,255,0)
darkgreen=(30, 117, 19)
font = pygame.font.SysFont('timesnewroman',  30)

font2 =pygame.font.Font("font.ttf",22)
pygame.mixer.init()
difficulty=1    # Set Difficulty
def drawtoscreen(text,textRect):
    gameDisplay.blit(text,textRect)
def TextToScreen(font,text,color,x,y):
    textx=font.render(text,True,color,None)
    textRectx=textx.get_rect()
    textRectx.center=(x,y)
    drawtoscreen(textx,textRectx)
def ClickBox(x,y,width,height,border=list): # border=[True/False , color]
    #print(x,y,width,height,border)
    if border[0]==True:
        pygame.draw.aalines(gameDisplay,border[1],True,[(x,y),(x+width,y)])
        pygame.draw.aalines(gameDisplay,border[1],True,[(x,y),(x,y+height)])
        pygame.draw.aalines(gameDisplay,border[1],True,[(x,y+height),(x+width,y+height)])
        pygame.draw.aalines(gameDisplay,border[1],True,[(x+width,y+height),(x+width,y)])
    
        if pygame.mouse.get_pos()[0]>x and pygame.mouse.get_pos()[0]<x+width and pygame.mouse.get_pos()[1]>y and pygame.mouse.get_pos()[1]<y+height and pygame.mouse.get_pressed(num_buttons=3)[0]==True:
            return True
        else:
            return False
            



def game_loop():
    letters=["Alpha","Beta","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India","Juliett","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo","Sierra","Tango","Uniform","Victor","Whiskey","X-ray","Yankee","Zulu"]
    numbers=["One","Two","Three","Four","Five","Six","Seven","Eight","Niner","Zero"]
    say=""
    ndict={"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Niner","0":"Zero"}
    ldict={"A":"Alpha", "B":"Beta","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot","G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike","N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra","T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-ray","Y":"Yankee","Z":"Zulu"}
    game_exit=False
    user_text=""
    previus=""
    
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                game_exit = True
                engine.stop()
                print("Quit with event(quit)!")
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_RSHIFT:    #  Start readout
                    for i in range(random.randint(1+difficulty,4+difficulty+random.randint(0,2))):
                        coin=random.randint(0,1)
                        if coin==1:
                            say+=" "
                            say+=letters[random.randint(0,len(letters)-1)]
                        else:
                            say+=" "
                            say+=numbers[random.randint(0,len(numbers)-1)]
                    user_text=""
                    engine.save_to_file(say,"say.mp3")
                    engine.runAndWait()
                    previus=say
                    say=""
                    saymp3=pygame.mixer.Sound(file="say.mp3")
                    pygame.mixer.Sound.play(saymp3,loops=0)
                if event.key==pygame.K_RCTRL:   # Debug event
                    user_text= pygame.mouse.get_pressed(num_buttons=3)[0]
                if event.key==pygame.K_BACKSPACE:
                    try:
                        user_text=user_text[:-1]
                    except:
                        print("Backspace on empty string")
                elif event.key!=pygame.K_RETURN:
                    try:
                        user_text+=event.unicode
                    except:
                        print("Non unicode character")
                elif event.key==pygame.K_RETURN:
                    print(previus)
                    userlist=list(user_text)
                    for i in range(len(userlist)):
                        if not userlist[i].isnumeric():
                            userlist[i]=ldict.get(userlist[i])
                        else:
                            userlist[i]=ndict.get(userlist[i])
                    userlist = " ".join(userlist)
                    print(userlist)
                    print(previus)
                    if " "+userlist==previus:
                        user_text="Correct"
                    else:
                        user_text="Incorrect"
        gameDisplay.fill(black)
        text=font.render(str(user_text), True, red, None)
        title=font2.render("Militray Radio",True,darkgreen,None)
        text_rect=text.get_rect()
        title_rect=title.get_rect()
        title_rect.center=(display_width//2,60)
        text_rect.center=(display_width//2,display_height//2)
        drawtoscreen(text,text_rect)
        drawtoscreen(title,title_rect)
        TextToScreen(font2,"This software if for official military use only! Any personal use of this software is considered a federal crime!",darkgreen,display_width//2,display_height-30)
        Click=ClickBox(300,display_height//2,200,50,[True,red])
        print(Click)
        if Click:
            user_text="Clicked"

        pygame.display.update()
        clock.tick(60)
"""
 TODO:
    Numbers couse Error      (Done)
    Better Looking Display   (IP)





"""
game_loop()
pygame.quit()
quit()



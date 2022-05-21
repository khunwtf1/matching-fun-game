from os import close
import pygame
import os
from tkinter import *
from pygame import image
from pygame import time
from pygame.constants import TIMER_RESOLUTION
from pygame.event import *
import random
import sys
from pygame import *

global score,score_list,score_text,songg,emai,passw,nam,dat

score_list = [0]
emai = []       #Email List
passw = []      #Password List
nam = []        #Name List
dat = []        #Date of birth List



#Easy Fruit Game Class
class frt_easy :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 128
        gameColumn = 4
        gameRows = 3
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 60, '60'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/fruit easy/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/fruit easy/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0 else 'boom!' 
                    if win < 6 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            #If Lose
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            #If Win
            else :
                if win < 6 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 45 :
                            score += 60
                        elif counter > 30 :
                            score += 45
                        elif counter > 15 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Easy Number Game Class
class num_easy :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 128
        gameColumn = 4
        gameRows = 3
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 60, '60'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/number easy/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/number easy/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 6 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 6 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 45 :
                            score += 60
                        elif counter > 30 :
                            score += 45
                        elif counter > 15 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Easy Alphabet Game Class
class alp_easy :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 128
        gameColumn = 4
        gameRows = 3
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 60, '60'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/alphabet easy/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/alphabet easy/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 6 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 6 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 45 :
                            score += 60
                        elif counter > 30 :
                            score += 45
                        elif counter > 15 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Easy Animal Game Class
class anm_easy :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 128
        gameColumn = 4
        gameRows = 3
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 60, '60'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/animal easy/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/animal easy/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 6 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 6 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 45 :
                            score += 60
                        elif counter > 30 :
                            score += 45
                        elif counter > 15 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Normal Fruit Game Class
class frt_normal :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 112
        gameColumn = 5
        gameRows = 4
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 80, '80'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/fruit normal/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/fruit normal/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 10 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 10 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 60 :
                            score += 60
                        elif counter > 40 :
                            score += 45
                        elif counter > 20 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Normal Number Game Class
class num_normal :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 112
        gameColumn = 5
        gameRows = 4
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 80, '80'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/number normal/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/number normal/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 10 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 10 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 60 :
                            score += 60
                        elif counter > 40 :
                            score += 45
                        elif counter > 20 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Normal Alphabet Game Class
class alp_normal :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 112
        gameColumn = 5
        gameRows = 4
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 80, '80'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/alphabet normal/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/alphabet normal/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 10 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 10 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 60 :
                            score += 60
                        elif counter > 40 :
                            score += 45
                        elif counter > 20 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Normal Animal Game Class
class anm_normal :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 112
        gameColumn = 5
        gameRows = 4
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 80, '80'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/animal normal/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/animal normal/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 10 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 10 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 60 :
                            score += 60
                        elif counter > 40 :
                            score += 45
                        elif counter > 20 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Hard Fruit Game Class
class frt_hard :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 6
        gameRows = 5
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 100, '100'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/fruit hard/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/fruit hard/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 15 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 15 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 75 :
                            score += 60
                        elif counter > 50 :
                            score += 45
                        elif counter > 25 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Hard Number Game Class
class num_hard :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 6
        gameRows = 5
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 100, '100'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/number hard/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/number hard/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 15 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 15 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 75 :
                            score += 60
                        elif counter > 50 :
                            score += 45
                        elif counter > 25 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Hard Alphabet Game Class
class alp_hard :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 6
        gameRows = 5
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 100, '100'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/alphabet hard/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/alphabet hard/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 15 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 15 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 75 :
                            score += 60
                        elif counter > 50 :
                            score += 45
                        elif counter > 25 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Hard Animal Game Class
class anm_hard :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 6
        gameRows = 5
        padding = 20
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 100, '100'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/animal hard/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/animal hard/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 15 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 15 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 75 :
                            score += 60
                        elif counter > 50 :
                            score += 45
                        elif counter > 25 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Expert Fruit Game Class
class frt_expert :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 7
        gameRows = 6
        padding = 10
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 120, '120'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/fruit expert/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/fruit expert/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 21 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 21 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 90 :
                            score += 60
                        elif counter > 60 :
                            score += 45
                        elif counter > 30 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Expert Number Game Class
class num_expert :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 7
        gameRows = 6
        padding = 10
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 120, '120'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/number expert/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/number expert/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 21 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 21 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 90 :
                            score += 60
                        elif counter > 60 :
                            score += 45
                        elif counter > 30 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Expert alphabet Game Class
class alp_expert :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 7
        gameRows = 6
        padding = 10
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 120, '120'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/alphabet expert/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/alphabet expert/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 21 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 21 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 90 :
                            score += 60
                        elif counter > 60 :
                            score += 45
                        elif counter > 30 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Expert anima; Game Class
class anm_expert :
    def __init__(self,root) :
        self.root = root
        
        
    def game(self):
        
        pygame.init()
        
        
        pygame.mixer.music.load('Python Project/Wii Music .mp3')
        pygame.mixer.music.play(loops=-1)
            
        correct = pygame.mixer.Sound('Python Project/Correct.mp3')
        wrong = pygame.mixer.Sound('Python Project/Wrong.mp3')
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')

        #variables for game
        screenWidth = 1000
        screenHeight = 975
        picSize = 96
        gameColumn = 7
        gameRows = 6
        padding = 10
        #               1000    - 106 *6
        leftMargin = (screenWidth - ((picSize+padding) * gameColumn)) // 2
        rightMargin = leftMargin
        topMargin = 325
        bottomMargin = (topMargin + ((picSize+padding) * gameRows))
        button_color = (180,173,102)
        selection1 = None
        selection2 = None
        score = 0
        global counter,win
        counter, text = 120, '120'
        win = 0
        
        label_font = pygame.font.SysFont("Berlin Sans FB",35)
        running_font = pygame.font.SysFont("Berlin Sans FB",50)
        text_font = pygame.font.SysFont("Berlin Sans FB",75)
        clock = pygame.time.Clock()
        gameOver = False
        black = (0,0,0)
        white = (255,255,255)
        
        
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        font = pygame.font.SysFont("Berlin Sans FB",50)

        #Loading the pygame screen
        screen = pygame.display.set_mode((screenWidth,screenHeight))
        pygame.display.set_caption("MATCHING FUN GAME")

        #Loading Background Image to python
        bgImage = pygame.image.load("Python Project/MATCHING Hard.png")
        bgImage = pygame.transform.scale(bgImage , (screenWidth,screenHeight))
        bgImageRect = bgImage.get_rect()

        #Create List of Card
        card = []
        for item in os.listdir("Python Project/animal expert/") :  #------------------------------- เรียก self.str ตรงนี้ว้อยยยยย -----------------------
            card.append(item.split('.')[0])

        cardCopy = card.copy()
        card.extend(cardCopy)
        cardCopy.clear()
        random.shuffle(card)
        
        gameover = text_font.render("Game Over".center(20), True, (255,255,255))
        
        #Show Score
        def show_label(score) :
            global t
            score_label = label_font.render("Score",True ,(0,0,0))
            time_label = label_font.render("Time", True , (0,0,0))
            score_run = running_font.render(str(score).center(5), True, (0,0,0))
            
            screen.blit(score_label, [200,190])
            screen.blit(time_label, [724,190])
            screen.blit(score_run, [198,220])
            
        def draw_text(text, font , text_col , x, y) :
            img = font.render(text, True, text_col)
            screen.blit(img, (x,y))
        
        def draw_result_text(text1, text2 , font , text_col , x1, y1, x2,y2) :
            pygame.draw.rect(screen,white,(0 ,300,1000,400))
            img1 = font.render(text1, True, text_col)
            img2 = font.render(text2, True, text_col)
            screen.blit(img1, (x1,y1)) 
            screen.blit(img2, (x2,y2))   
        
            
        def draw_background(bg) :
            screen.blit(bg, (screenWidth,screenHeight) )
        
        
        #Load each of the Images into the python memory
        matching = []
        matchingRect = []
        hiddenImages = []

        for item in card :
            picture = pygame.image.load(f'Python Project/animal expert/{item}.jpg')
            picture = pygame.transform.scale(picture ,(picSize,picSize))
            matching.append(picture)
            pictureRect = picture.get_rect()
            matchingRect.append(pictureRect) 

        for i in range(len(matchingRect)) :
            #matchrect[0][0]  =    364      +  (        106      ) * (0%6)
            matchingRect[i][0] = leftMargin + ((picSize + padding) * (i%gameColumn))
            matchingRect[i][1] = topMargin + ((picSize + padding) * (i%gameRows))
            hiddenImages.append(False)
                
        print(card)
        print(matching)
        print(matchingRect)
        print(hiddenImages)

        

        #ทำให้ Screen แสดงตลอดจนกว่าจะกดปิด
        gameLoop = True
        while gameLoop :
            #Load Background Image to Screen
            screen.blit(bgImage, bgImageRect)
            
            #Event Handling
            for event in pygame.event.get() :
                if event.type == gameOver :
                    
                    pygame.mixer.music.load('Python Project/Damaged Coda.mp3')
                    pygame.mixer.music.play(loops=-1)
                #Countdown time
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                    text = str(counter) if counter > 0  else 'boom!' 
                    if win < 21 :
                        pass
                    else :
                        counter +=1
                #Exit Game 
                if event.type == pygame.QUIT :
                    gameLoop = False
                    pygame.quit()
                    play_squid_theme()
                #Open Button
                if gameOver == False :
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                        click.play()
                        for i in matchingRect :
                            if i.collidepoint(event.pos) :
                                
                                if selection1 != None :
                                    selection2 = matchingRect.index(i)
                                    hiddenImages[selection2] = True
                                else :
                                    selection1 = matchingRect.index(i)
                                    hiddenImages[selection1] = True
                    
            screen.blit(font.render(text.center(5), True, (0, 0, 0)), (714,220))
            
            keys = pygame.key.get_pressed()
            
            clock.tick(1000)
            #Show Image
            for item in range(len(card)) :
                if hiddenImages[item] == True :
                    screen.blit(matching[item] , matchingRect[item])
                else :
                    pygame.draw.rect(screen,button_color,(matchingRect[item][0] , matchingRect[item][1],picSize,picSize))
            show_label(score)
            
            
            
            if counter <= 0 :
                
                screen.blit(gameover, [250,50])
                gameOver = True
                draw_result_text("Please Try Again".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                    pygame.mixer.music.stop()
                    gameLoop = False
                    pygame.quit()
                    show_result_frame(change2)
            else :
                if win < 21 :
                    print("oooo")  
                else :
                    gameOver = True
                    draw_result_text("Congratulations !".center(30),"Press E or ESC for exit".center(30),text_font,black,100,400,100,500)
                    score_list.clear()
                    score_list.append(str(score))
                    score_text = Label(change1)
                    iii = "Score : "+str(score)            
                    score_text.config(text= iii.center(30) , font= ("Berlin Sans FB",75), bg= "#FCFBE3" , fg = "black") 
                    score_text.place(x = 100,y = 500 , height= 200 , width= 700)                    
                
                    print(score_list)
                    if keys[pygame.K_e] or keys[pygame.K_ESCAPE]:
                        gameLoop = False
                        pygame.quit()
                        show_result_frame(change1)
                        
                        
            
                  
            pygame.display.update()
            if gameOver == False :
                if selection1 != None and selection2 != None :
                    if card[selection1] == card[selection2] :
                        correct.play()
                        win += 1
                        draw_text("Well Done".center(20),text_font,white,250,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        selection1 = None
                        selection2 = None
                        if counter > 90 :
                            score += 60
                        elif counter > 60 :
                            score += 45
                        elif counter > 30 :
                            score += 30
                        else:
                            score += 15
                            
                            
                    else :
                        wrong.play()
                        draw_text("Oh no".center(20),text_font,white,275,50)
                        pygame.display.update()
                        pygame.time.wait(1000)
                        hiddenImages[selection1] = False
                        hiddenImages[selection2] = False
                        selection1 = None
                        selection2 = None
                
                        
            pygame.display.update() #Update bgImage to screen if don't do this bgImage will not display to screen

#Beginner User Interface 
root = Tk()
root.geometry("900x1000+300+0")
root.title("MATCHING FUN GAME BETA !!")

pygame.mixer.init()
songg = pygame.mixer.music
songg.load('Python Project/Squid Game Theme.mp3')
songg.set_volume(0.09)
songg.play(loops=-1)

click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')


#Variables for call game
global fruitEasy,numberExEasy,alphabetEasy,animalEasy                   # Easy level
global fruitNormal,numberNormal,alphabetNormal,animalNormal             # Normal level
global fruitHard,numberHard,alphabetHard,animalHard                     # Hard level
global fruitExpert,numberExpert,alphabetExpert,animalExpert             # Expert level

#game variables
fruitEasy = frt_easy(root)
fruitNormal = frt_normal(root)
fruitHard = frt_hard(root)
fruitExpert = frt_expert(root)

numberEasy = num_easy(root)
numberNormal = num_normal(root)
numberHard = num_hard(root)
numberExpert = num_expert(root)

alphabetEasy = alp_easy(root)
alphabetNormal = alp_normal(root)
alphabetHard = alp_hard(root)
alphabetExpert = alp_expert(root)

animalEasy = anm_easy(root)
animalNormal = anm_normal(root)
animalHard = anm_hard(root)
animalExpert = anm_expert(root)

#Command Function
#----------------------------------------------------------


#Call game for play
def play_game(type):
    type.game()
    songg = pygame.mixer.music
    songg.stop()
    print("hello")
    

#Call frame to root    
def show_frame(frame) :
        click = pygame.mixer.Sound('Python Project/Mouse Click.mp3')
        click.play()
        frame.tkraise()

def show_result_frame(frame) :
        frame.tkraise()
        
        pygame.mixer.init()
        songg = pygame.mixer.music
        songg.load('Python Project/Squid Game Theme.mp3')
        songg.set_volume(0.09)
        songg.play(loops=-1)
        
def play_squid_theme() :
        pygame.mixer.init()
        songg = pygame.mixer.music
        songg.load('Python Project/Squid Game Theme.mp3')
        songg.set_volume(0.09)
        songg.play(loops=-1)
        
        
#Background for each frame
cat_bg = PhotoImage(file="Python Project/category-level.png")   #category frame background
frt_bg = PhotoImage(file="Python Project/fruit bg.png")         #fruit level framebackground
num_bg = PhotoImage(file="Python Project/number bg.png")        #number level frame background
alp_bg = PhotoImage(file="Python Project/alphabet bg.png")      #alphabet level frame background
anm_bg = PhotoImage(file="Python Project/animal bg.png")        #animal level frame background
res_bg = PhotoImage(file="Python Project/category-level.png")   #Result level frame background

category = Frame(root)

change1 = Frame(root)
change1.place(x = 0, y =0 , width= 900 , height= 1000)

change2 = Frame(root)
change2.place(x = 0, y =0 , width= 900 , height= 1000)

res_bg = PhotoImage(file='Python Project/category-level.png')   #result frame background


res_bg_label1 = Label(change1, image=res_bg) #Win frame
res_bg_label1.place(x=0,y=0)

awesome_label = Label(change1, text= "AWESOME !!!!!!".center(20) , font= ("Berlin Sans FB",75) , bg = "#FCFBE3") 
awesome_label.place(x=100,y= 300,width=700)

res_bg_label2 = Label(change2, image=res_bg) #Lose Frame
res_bg_label2.place(x=0,y=0)

gameover_label = Label(change2, text= "GAME OVER".center(20) , font= ("Berlin Sans FB",75) , bg = "#FCFBE3")
gameover_label.place(x=100,y= 300,width=700)

return_Button1 = Button(change1,text = "Back to Main Menu".center(20),font=("Berlin Sans FB",30),fg="black",bg="#E4D936" , command= lambda: show_frame(mainmenu))
return_Button1.place(x=250,y=830,width=400,height=50)

return_button2 = Button(change2,text = "Back to Main Menu".center(20),font=("Berlin Sans FB",30),fg="black",bg="#E4D936" , command= lambda : show_frame(mainmenu))
return_button2.place(x=250,y=730,width=400,height=50)

toLevel_button = Button(change2,text = "Select Another Category".center(30),font=("Berlin Sans FB",30),fg="black",bg="#E4D936" , command= lambda : show_frame(category))
toLevel_button.place(x=200,y=630,width=500,height=50)

#Fruit frame      
frt_level = Frame(root)
frt_level.place(x = 0, y =0 , width= 900 , height= 1020)
frt_level.config(background="#E4D936")

frt_bg_label = Label(frt_level, image=frt_bg)
frt_bg_label.place(x=0,y=0)
                
frt_myLabel1 = Label(frt_level,text="Select",font=("Berlin Sans FB",50),background="#FFFFF7")
frt_myLabel2 = Label(frt_level,text="Level",font=("Berlin Sans FB",75),background="#FFFFF7")

frt_myLabel1.pack(pady=45)
frt_myLabel2.pack(pady=0)

#number frame      
num_level = Frame(root)
num_level.place(x = 0, y =0 , width= 900 , height= 1020)
num_level.config(background="#E4D936")

num_bg_label = Label(num_level, image=num_bg)
num_bg_label.place(x=0,y=0)
                
num_myLabel1 = Label(num_level,text="Select",font=("Berlin Sans FB",50),background="#FFFFF7")
num_myLabel2 = Label(num_level,text="Level",font=("Berlin Sans FB",75),background="#FFFFF7")

num_myLabel1.pack(pady=45)
num_myLabel2.pack(pady=0)


#alphabet frame      
alp_level = Frame(root)
alp_level.place(x = 0, y =0 , width= 900 , height= 1020)
alp_level.config(background="#E4D936")

alp_bg_label = Label(alp_level, image=alp_bg)
alp_bg_label.place(x=0,y=0)
                
alp_myLabel1 = Label(alp_level,text="Select",font=("Berlin Sans FB",50),background="#FFFFF7")
alp_myLabel2 = Label(alp_level,text="Level",font=("Berlin Sans FB",75),background="#FFFFF7")

alp_myLabel1.pack(pady=45)
alp_myLabel2.pack(pady=0)

#animals frame      
anm_level = Frame(root)
anm_level.place(x = 0, y =0 , width= 900 , height= 1020)
anm_level.config(background="#E4D936")

anm_bg_label = Label(anm_level, image=anm_bg)
anm_bg_label.place(x=0,y=0)
                
anm_myLabel1 = Label(anm_level,text="Select",font=("Berlin Sans FB",50),background="#FFFFF7")
anm_myLabel2 = Label(anm_level,text="Level",font=("Berlin Sans FB",75),background="#FFFFF7")

anm_myLabel1.pack(pady=45)
anm_myLabel2.pack(pady=0)

#Result Frame
result = Frame(root)
result.place(x = 0, y =0 , width= 900 , height= 1020)   
result.config(background="#E4D936")

res_bg_label = Label(result, image=cat_bg)
res_bg_label.place(x=0,y=0)

#Category Frame
category = Frame(root)
category.place(x = 0, y =0 , width= 900 , height= 1020)
category.config(background="#E4D936")

cat_bg_label = Label(category, image=cat_bg)
cat_bg_label.place(x=0,y=0)

instruction = Frame(root)
instruction.place(x = 0, y =0 , width= 900 , height= 1020)
instruction.config(background="#E4D936")

ins_bg_label = Label(instruction, image=cat_bg)
ins_bg_label.place(x=0,y=0)

ins_myLabel1 = Label(instruction,text="วิธีการเล่นเกม",font=("Berlin Sans FB",60), background="#FCFBE3")
ins_myLabel2 = Label(instruction,text=" 1. สร้างบัญชีสำหรับการเข้าเล่นเกม ",font=("Berlin Sans FB",30), background="#FCFBE3")
ins_myLabel3 = Label(instruction,text=" 2. นำเอาบัญชีที่สร้างมา มาใส่เพื่อล็อกอินเกม  ",font=("Berlin Sans FB",30), background="#FCFBE3")
ins_myLabel4 = Label(instruction,text=" 3. เลือกหมวดที่ต้องการจะเล่น ",font=("Berlin Sans FB",30), background="#FCFBE3")
ins_myLabel5 = Label(instruction,text=" 4. เลือกระดับความยาก-ง่ายในการเล่น ",font=("Berlin Sans FB",30), background="#FCFBE3")
ins_myLabel6 = Label(instruction,text=" 5. ผู้เล่นจะต้องทำการหาภาพที่คล้ายกันจำนวน 2 ภาพ ภายในระยะเวลาที่กำหนด ",font=("Berlin Sans FB",20), background="#FCFBE3")
ins_myLabel7 = Label(instruction,text=" 6. หากภาพที่เลือกจำนวน 2 ภาพ ไม่ใช่ภาพเดียวกัน ภาพเหล่านั้นก็หันกลับไปเช่นเดิมโดยทันที ",font=("Berlin Sans FB",20), background="#FCFBE3")
ins_myLabel8 = Label(instruction,text="7. เมื่อหมดเวลาแล้วยังไม่สามารถจับคู่ภาพได้ครบก็จะขึ้นว่า Game Over จากนั้นจะมีตัวเลือกว่าจะ",font=("Berlin Sans FB",20), background="#FCFBE3")
ins_myLabel9 = Label(instruction,text=" กลับไปที่ main menu หรือจะเลือกเล่นหมวดอื่น ",font=("Berlin Sans FB",20), background="#FCFBE3")
ins_myLabel10 = Label(instruction,text=" 8. ถ้าหากเราสามารถจับคู่ภาพได้ครบก่อนที่เวลาจะหมด ก็จะมีการแสดงคะแนนเมื่อเล่นจบ   ",font=("Berlin Sans FB",20), background="#FCFBE3")

ins_myLabel1.pack(pady=45)
ins_myLabel2.pack(pady=10)
ins_myLabel3.pack(pady=10)
ins_myLabel4.pack(pady=10)
ins_myLabel5.pack(pady=10)
ins_myLabel6.pack(pady=10)
ins_myLabel7.pack(pady=10)
ins_myLabel8.pack(pady=10)
ins_myLabel9.pack(pady=10)
ins_myLabel10.pack(pady=10)





ins_to_menButton= Button(instruction,text="Back to Main Menu".center(20),font=("Berlin Sans FB",30),fg="black",bg="#E4D936",command= lambda: show_frame(mainmenu))
ins_to_menButton.place(x=250,y=830,width=400,height=50)

#Main Menu Frame
mainmenu = Frame(root)
mainmenu.place(x = 0, y =0 , width= 900 , height= 1020)
mainmenu.config(background="#E4D936")

men_bg_label = Label(mainmenu, image=cat_bg)
men_bg_label.place(x=0,y=0)

men_myLabel1 = Label(mainmenu,text="Welcome",font=("Berlin Sans FB",60), background="#FCFBE3")
men_myLabel1.pack(pady=45)
men_to_catButton= Button(mainmenu,text="Play Game",font=("Berlin Sans FB",30),fg="black",bg="#E4D936",width=15,command=lambda : show_frame(category))
men_to_catButton.pack(pady=45)
instr_Button= Button(mainmenu,text="Instruction",font=("Berlin Sans FB",30),fg="black",bg="#B4AB2A",width=15,command= lambda : show_frame(instruction))
instr_Button.pack(pady=10)
exit_Button= Button(mainmenu,text="Exit Game",font=("Berlin Sans FB",30),fg="black",bg="#5F5C39",width=15,command= lambda : root.destroy())
exit_Button.pack(pady=45)

app=QApplication(sys.argv)
mainwindow = Login()
widget =QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight
widget.setFixedHeight
widget.show()
app.exec_()

mainwindow.loginfunction()

print(emai)
print(passw)
print(nam)
print(dat)


#ใส่ข้อความในหน้าจอ
cat_myLabel1 = Label(category,text="Select",font=("Berlin Sans FB",45), background="#FCFBE3")
cat_myLabel2 = Label(category,text="Category",font=("Berlin Sans FB",70), background="#FCFBE3")

cat_myLabel1.pack(pady=45)
cat_myLabel2.pack(pady=0)
 
#------------------------------------------------------------------
#Category Frame Buttons and place them
#------------------------------------------------------------------

Fruits = Button(category,text="Fruits",font=("Berlin Sans FB",30),fg="white",bg="#5F5C39",command=lambda : show_frame(frt_level) , relief= "raised")
Number = Button(category,text="Number",font=("Berlin Sans FB",30),fg="white",bg="#5F5C39",command=lambda : show_frame(num_level) , relief= "raised")
AtoZ = Button(category,text="A-Z",font=("Berlin Sans FB",30),fg="white",bg="#5F5C39",command=lambda : show_frame(alp_level) , relief= "raised")
Animals = Button(category,text="Animals",font=("Berlin Sans FB",30),fg="white",bg="#5F5C39",command=lambda : show_frame(anm_level) , relief= "raised")
cat_to_menButton= Button(category,text="Back to Main Menu".center(20),font=("Berlin Sans FB",30),fg="black",bg="#E4D936",command= lambda: show_frame(mainmenu))

Fruits.place(x=150,y=325,width=250,height=200)
Number.place(x=500,y=325,width=250,height=200)
AtoZ.place(x=150,y=550,width=250,height=200)
Animals.place(x=500,y=550,width=250,height=200)
cat_to_menButton.place(x=250,y=830,width=400,height=50)

#------------------------------------------------------------------
#Fruits Category Frame Buttons and place them
#------------------------------------------------------------------

frt_Easy = Button(frt_level,text="Easy",font=("Berlin Sans FB",30),fg="black",bg="#FED1DA" , relief= "raised",command=lambda : play_game(fruitEasy))
frt_Medium = Button(frt_level,text="Medium",font=("Berlin Sans FB",30),fg="black",bg="#F8F3BB" , relief= "raised",command=lambda : play_game(fruitNormal))
frt_Hard = Button(frt_level,text="Hard",font=("Berlin Sans FB",30),fg="black",bg="#D3E1C8" , relief= "raised",command=lambda : play_game(fruitHard))
frt_Expert = Button(frt_level,text="Expert",font=("Berlin Sans FB",30),fg="black",bg="#D3F6F2" , relief= "raised",command=lambda : play_game(fruitExpert))
frt_catButton= Button(frt_level,text="Select Category",font=("Berlin Sans FB",30),fg="black",bg="#D9C7DB",command=lambda : show_frame(category))

frt_Easy.place(x=150,y=325,width=250,height=200)
frt_Medium.place(x=500,y=325,width=250,height=200)
frt_Hard.place(x=150,y=550,width=250,height=200)
frt_Expert.place(x=500,y=550,width=250,height=200)
frt_catButton.place(x=300,y=830,width=300,height=50)

#------------------------------------------------------------------
#Number Category Frame Buttons and place them
#------------------------------------------------------------------

num_Easy = Button(num_level,text="Easy",font=("Berlin Sans FB",30),fg="black",bg="#FED1DA" , relief= "raised",command=lambda : play_game(numberEasy))
num_Medium = Button(num_level,text="Medium",font=("Berlin Sans FB",30),fg="black",bg="#F8F3BB" , relief= "raised",command=lambda : play_game(numberNormal))
num_Hard = Button(num_level,text="Hard",font=("Berlin Sans FB",30),fg="black",bg="#D3E1C8" , relief= "raised",command=lambda : play_game(numberHard))
num_Expert = Button(num_level,text="Expert",font=("Berlin Sans FB",30),fg="black",bg="#D3F6F2" , relief= "raised",command=lambda : play_game(numberExpert))
num_catButton= Button(num_level,text="Select Category",font=("Berlin Sans FB",30),fg="black",bg="#D9C7DB",command=lambda : show_frame(category))

num_Easy.place(x=150,y=325,width=250,height=200)
num_Medium.place(x=500,y=325,width=250,height=200)
num_Hard.place(x=150,y=550,width=250,height=200)
num_Expert.place(x=500,y=550,width=250,height=200)
num_catButton.place(x=300,y=830,width=300,height=50)

#------------------------------------------------------------------
#Alphabet Category Frame Buttons and place them
#------------------------------------------------------------------

alp_Easy = Button(alp_level,text="Easy",font=("Berlin Sans FB",30),fg="black",bg="#FED1DA" , relief= "raised",command=lambda : play_game(alphabetEasy))
alp_Medium = Button(alp_level,text="Medium",font=("Berlin Sans FB",30),fg="black",bg="#F8F3BB" , relief= "raised",command=lambda : play_game(alphabetNormal))
alp_Hard = Button(alp_level,text="Hard",font=("Berlin Sans FB",30),fg="black",bg="#D3E1C8" , relief= "raised",command=lambda : play_game(alphabetHard))
alp_Expert = Button(alp_level,text="Expert",font=("Berlin Sans FB",30),fg="black",bg="#D3F6F2" , relief= "raised",command=lambda : play_game(alphabetExpert))
alp_catButton= Button(alp_level,text="Select Category",font=("Berlin Sans FB",30),fg="black",bg="#D9C7DB",command=lambda : show_frame(category))

alp_Easy.place(x=150,y=325,width=250,height=200)
alp_Medium.place(x=500,y=325,width=250,height=200)
alp_Hard.place(x=150,y=550,width=250,height=200)
alp_Expert.place(x=500,y=550,width=250,height=200)
alp_catButton.place(x=300,y=830,width=300,height=50)

#------------------------------------------------------------------
#Animal Category Frame Buttons and place them
#------------------------------------------------------------------

anm_Easy = Button(anm_level,text="Easy",font=("Berlin Sans FB",30),fg="black",bg="#FED1DA" , relief= "raised",command=lambda : play_game(animalEasy))
anm_Medium = Button(anm_level,text="Medium",font=("Berlin Sans FB",30),fg="black",bg="#F8F3BB" , relief= "raised",command=lambda : play_game(animalNormal))
anm_Hard = Button(anm_level,text="Hard",font=("Berlin Sans FB",30),fg="black",bg="#D3E1C8" , relief= "raised",command=lambda : play_game(animalHard))
anm_Expert = Button(anm_level,text="Expert",font=("Berlin Sans FB",30),fg="black",bg="#D3F6F2" , relief= "raised",command=lambda : play_game(animalExpert))
anm_catButton= Button(anm_level,text="Select Category",font=("Berlin Sans FB",30),fg="black",bg="#D9C7DB",command=lambda : show_frame(category))

anm_Easy.place(x=150,y=325,width=250,height=200)
anm_Medium.place(x=500,y=325,width=250,height=200)
anm_Hard.place(x=150,y=550,width=250,height=200)
anm_Expert.place(x=500,y=550,width=250,height=200)
anm_catButton.place(x=300,y=830,width=300,height=50)

root.mainloop()
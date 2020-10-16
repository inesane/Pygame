import pygame
import random
from config import *#to import config file

pygame.init()

win = pygame.display.set_mode((1000,550))#window of game

pygame.display.set_caption("The Game of The Ainesh")

font = pygame.font.SysFont('freesans',20,True,False) #font for all of my text, i.e. score,lives

class stationary():#class for stationary object
    def __init__(self,color,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color

    def makes(self):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

class moving():#class for moving objects
    def __init__(self,color,x,y,width,height,vel):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.vel=vel
    
    def makem(self):
         pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
         self.x=self.x+self.vel
         self.x=self.x%600
         self.vel=random.randint(1,10) + 3*level

#stationary objects
en1 = stationary((100, 20, 50), 100, 250, 20, 20)
en2 = stationary((100, 20, 50), 200, 310, 20, 20)
en3 = stationary((100, 20, 50), 450, 370, 20, 20)
en4 = stationary((100, 20, 50), 300, 190, 20, 20)
en5 = stationary((100, 20, 50), 130, 130, 20, 20)
#moving objects
en6 = moving((0, 0, 100), 0, 100, 20, 20, 0)
en7 = moving((0, 0, 100), 0, 160, 20, 20, 0)
en8 = moving((0, 0, 100), 0, 220, 20, 20, 0)
en9 = moving((0, 0, 100), 0, 280, 20, 20, 0)
en10 = moving((0, 0, 100), 0, 340, 20, 20, 0)
en11 = moving((0, 0, 100), 0, 400, 20, 20, 0)

sta = (en1,en2,en3,en4,en5) #tuple for stationary objects
mov = (en6,en7,en8,en9,en10,en11)#tuple for moving objects
ysta = (en1.y,en2.y,en3.y,en4.y,en5.y)#tuple for y-coordinate of stationary objects
ymov = (en6.y,en7.y,en8.y,en9.y,en10.y,en11.y)#tuple for y-coordinate of moving objects
ystacheck = [0,0,0,0,0]#list to check if we have added score after crossing a stationary object
ymovcheck = [0,0,0,0,0,0]#list to check if we have added score after crossing a moving object

def coll(rec):#function to check for collision
    a=abs(x-rec.x)
    b=abs(y-rec.y)
    c=int(width+rec.width)/2
    d=int(height+rec.height)/2
    if a <= c and b <= d:#checking for collision using position of centers of object and enemy
        return True
    else:
        return False

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    tvar = 0#time variable
    if end==0:
        tvar += 1 #time variable incremented to decrease score with respect to time
        key = pygame.key.get_pressed()
        if player==0:
            if key[pygame.K_LEFT] and x> vel:#move left with left arrow key
                x -= vel#move x-coordinate of player by the velocity to the left
            if key[pygame.K_RIGHT] and x< 600 - width - vel:#move right with right arrow key
                x += vel#move x-coordinate of player by the velocity to the right
            if key[pygame.K_UP] and y> vel:#move up with up arrow key
                y -= vel#move y-coordinate of player by the velocity downwards
            if key[pygame.K_DOWN] and y< 550 - height - vel:#move down with down arrow key
                y += vel#move y-coordinate of player by the velocity upwards
            pygame.draw.rect(win, (0,0,0), (0,0,620,550))#making the playing part of the screen black
            #partitions
            pygame.draw.rect(win, (0, 100, 0), (0, 100, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 160, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 220, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 280, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 340, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 400, 600, 20))
            pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
            #making stationary enemies
            en1.makes()
            en2.makes()
            en3.makes()
            en4.makes()
            en5.makes()
            #making moving enemies
            en6.makem()
            en7.makem()
            en8.makem()
            en9.makem()
            en10.makem()
            en11.makem()
            for i in sta:#checking for stationary collisions
                if coll(i):
                    x = 300#moving back to intital position
                    y = 450
                    lives += 1
                    livesfor -= 1#decreasing lives left by 1
                    ystacheck=[0,0,0,0,0]#reinitializing list that checks if we have crossed stationary enemy
                    ymovcheck=[0,0,0,0,0,0]#reinitializing list that checks if we have crossed moved enemy
            for i in mov:#checking for moving collisions
                if coll(i):
                    x = 300#moving back to intial position
                    y = 450
                    lives += 1
                    livesfor -= 1#decreasing lives by 1
                    ystacheck=[0,0,0,0,0]#reinitializing list that checks if we have crossed stationary enemy
                    ymovcheck=[0,0,0,0,0,0]#reinitializing list that checks if we have crossed moved enemy
            #increasing score
            what = 0
            for i in ysta:
                if y < i and ystacheck[what]==0:
                    score1 += 5
                    ystacheck[what]=1
                what+=1
            why = 0
            for i in ymov:
                if y < i and ymovcheck[why]==0:
                    score1 += 10
                    ymovcheck[why]=1
                why+=1
            if y < 20:#going back to intial position if we pass the whole map
                x = 300
                y = 450
                level += 1#increasing level
                ystacheck=[0,0,0,0,0]
                ymovcheck=[0,0,0,0,0,0]
            if lives == 3:
                player=1
                x=300
                y=20
                vel=10
                lives=0
                level=0
                ystacheck=[0,0,0,0,0]
                ymovcheck=[0,0,0,0,0,0]
                tvar=0
            score1 -= tvar#decreasing score by factor of time
        player_text1 = font.render("Player1 Score "+str(score1),1,(255,255,255))#displaying player 1 score
        player_text2 = font.render("Player2 Score "+str(score2),1,(255,255,255))#displaying player 2 score
        player_lives1 = font.render("Player1 Lives "+str(livesfor),1,(255,255,255))#displaying lives left for player 1
        player_lives2 = font.render("Player2 Lives 3",1,(255,255,255))#displaying live left for player 2
        pygame.draw.rect(win, (0,0,255), (620,0,380,550))
        #blitting text
        win.blit(player_text1,(620,50))
        win.blit(player_text2,(620,500))
        win.blit(player_lives1,(620,100))
        win.blit(player_lives2,(620,450))
        pygame.display.update()
        if player > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] and x> vel:
                x -= vel
            if key[pygame.K_RIGHT] and x< 600 - width - vel:
                x += vel
            if key[pygame.K_UP] and y>20-vel:
                y -= vel
            if key[pygame.K_DOWN] and y<550-vel:
                y += vel
            win.fill((0, 0, 0))
            pygame.draw.rect(win, (0, 100, 0), (0, 100, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 160, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 220, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 280, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 340, 600, 20))
            pygame.draw.rect(win, (0, 100, 0), (0, 400, 600, 20))
            pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
            en1.makes()
            en2.makes()
            en3.makes()
            en4.makes()
            en5.makes()
            en6.makem()
            en7.makem()
            en8.makem()
            en9.makem()
            en10.makem()
            en11.makem()
            for i in sta:
                if coll(i):
                    x = 300
                    y = 20
                    lives += 1
                    livesleft -= 1
                    ystacheck=[0,0,0,0,0]
                    ymovcheck=[0,0,0,0,0,0]
            for i in mov:
                if coll(i):
                    x = 300
                    y = 20
                    lives += 1
                    livesleft -= 1
                    ystacheck=[0,0,0,0,0]
                    ymovcheck=[0,0,0,0,0,0]
            who=0
            for i in ysta:
                if y > i and ystacheck[who]==0:
                    score2 += 5
                    ystacheck[who]=1
                who+=1
            when=0
            for i in ymov:
                if y > i and ymovcheck[when]==0:
                    score2 += 10       
                    ymovcheck[when]=1
                when+=1
            if y > 480:
                x = 300
                y = 20
                level+=1
                ystacheck=[0,0,0,0,0]
                ymovcheck=[0,0,0,0,0,0]
            if lives == 3:
                end=1
            score2 -= tvar 
        player_text1 = font.render("Player1 Score "+str(score1),1,(255,255,255))
        player_text2 = font.render("Player2 Score "+str(score2),1,(255,255,255))
        player_lives1 = font.render("Player1 Lives "+str(livesfor),1,(255,255,255))
        player_lives2 = font.render("Player2 Lives "+str(livesleft),1,(255,255,255))
        pygame.draw.rect(win, (0,0,255), (620,0,380,550))
        win.blit(player_text1,(620,50))
        win.blit(player_text2,(620,500))
        win.blit(player_lives1,(620,100))
        win.blit(player_lives2,(620,450))
    else:
        if score1 < score2:#checking if player 2 won
            victory2  = font.render("Player 2 Wins", 1,(255,255,255))#displaying that player 2 won
            win.blit(victory2, (620, 250))
        elif score2 < score1:#checking if player 1 won
            victory1 = font.render("Player 1 Wins", 1,(255, 255, 255))#displaying that player 1 won
            win.blit(victory1, (620,250))
        else:#tie
            tie = font.render("How t f did u tie", 1,(255,255,255))#displaying that tie occured
            win.blit(tie, (620,250))
        pygame.display.update()
    pygame.display.update()
pygame.time.delay(1000)        
pygame.display.quit()
pygame.quit()

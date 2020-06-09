import pygame, sys
import os, random
from tkinter import *
from tkinter import messagebox
pygame.init()

height = 720
width = 1280
screen = pygame.display.set_mode((width,height))

class checkcol:
     def checkcollision(self,x1,y1,x2,y2, blocksize):
          if x1 >= x2 and x1<= x2 + blocksize:
               if y1 >= y2 and y1 <= y2 + blocksize:
                    return True
          return False

class Snake():
     x = []
     y = []
     move = 25
     direction = 0
     length = 1

     updatemax = 2
     updatecount = 0

     def __init__(self, length):
          self.length = length
          for i in range(0,2000):
               self.x.append(1300)
               self.y.append(800)

          self.x[0] = -100
          self.x[1] = -100
          self.x[2] = -100
          self.y[0] = -100
          self.y[1] = -100
          self.y[2] = -100

         
     def update(self):
          self.updatecount = self.updatecount + 1
          if self.updatecount > self.updatemax:

               for i in range(self.length, 0, -1):
                    self.x[i] = self.x[i-1]
                    self.y[i] = self.y[i-1]

               if self.direction == 0:
                    self.x[0] = self.x[0]+ self.move
               if self.direction == 1:
                    self.x[0] = self.x[0] - self.move
               if self.direction == 2:
                    self.y[0] = self.y[0] - self.move
               if self.direction == 3:
                    self.y[0] = self.y[0] + self.move

               self.updatecount = 0

     def draw(self,surface, image):
          for i in range(0, self.length):
               surface.blit(image, (self.x[i], self.y[i]))
                                             
class Food(pygame.sprite.Sprite):
     
     def __init__(self,x ,y):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface((25,25))
          self.image.set_colorkey(black)
          foodimage = pygame.image.load("apple.png")
          self.image.blit(foodimage, (0,0))
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y

class snakecollide(pygame.sprite.Sprite):
     def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.Surface((25,25))
          self.rect = self.image.get_rect()

def leaderboardentry():
     root2 = Tk()
     root2.withdraw()
     result = messagebox.askyesno("Score", "Would you like to save your score to the leaderboards")
     root2.destroy()
     if result == True:
          root = Tk()
          label = Label(root, text="Name")
          label.pack(side = LEFT)
          entry = Entry(root, bd=5)
          entry.pack(side = RIGHT)
          
          def callback():
               global text
               text = entry.get()
               if len(text) == 0:
                    messagebox.showerror("Error", "Name entry cannot be left blank")
               elif len(text) > 30:
                    messagebox.showerror("Error", "Name entry cannot exceed 30 characters")
                    entry.delete(0, END)
               else:
                    root.destroy()
                    root.quit()
               
               return text                                      
                                         
                                         
                                         
          b = Button(root, text="Confirm", width=10, command=callback)
          b.pack(side = RIGHT)
          root.mainloop()
          

     return result
     
     
def bubblesort(seq, namelist):
     changed = True
     while changed:
          changed = False
          for i in range(len(seq)-1):
               if (int(seq[i])) < (int(seq[i+1])):
                    seq[i], seq[i+1] = seq[i+1], seq[i]
                    namelist[i], namelist[i+1] = namelist[i+1], namelist[i]
                    changed = True
                    
     return seq, namelist
                    

     
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
green = (0,100,0)
yellow = (255, 255, 0)
lgreen = (0,255,0)
lred = (255,108,108)
lyellow = (255,255,224)
foodgroup = pygame.sprite.Group()
snakescreen = pygame.image.load("snakestart.png")
largefont = pygame.font.SysFont("comicsansms", 110)
pausedlabel = largefont.render("GAME PAUSED", 1, (black))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
buttonfont2 = pygame.font.SysFont("Britannic Bold", 35)


def gamewindow1 ():
    
     stopped = True
     playbut = pygame.Rect(100, 550, 100, 50)
     quitbut = pygame.Rect(500,550,100,50)
     leadbut = pygame.Rect(900,550,220,50)
     myfont=pygame.font.SysFont("Britannic Bold", 80)
     buttonfont = pygame.font.SysFont("Britannic Bold", 40)
     leadfont = pygame.font.SysFont("Britannic Bold", 30)
     nlabel=myfont.render("WELCOME TO SNAKE", 1, (255, 0, 0))
     leadlabel = buttonfont.render("LEADERBOARD FILE UNAVAILIBLE, CHECK THE DIRECTORY", 1, (black))
     scorefont = pygame.font.SysFont("Brittanic Bold", 30)
     instructlabel1= buttonfont.render("Use the escape key to return to the main menu at any time",1,(white))
     playbutfont = buttonfont.render("Play!", 1,(black))
     quitbutfont = buttonfont.render("Quit!", 1 ,(black))
     leadbutfont = buttonfont.render("Leaderboards!", 1,(black))
     pauselabel = scorefont.render("Press P to pause", 1, white)
     gameoverinstruct = buttonfont.render("Press Enter/Return key to add score to the leaderboards!",1,(black))
     gameoverinstruct2 = buttonfont.render("Press ESC/ESCAPE key to return to the main menu!",1,(black))


     while stopped:
        pygame.display.set_caption("Snake Game")
        screen.fill(black)
        mouse = pygame.mouse.get_pos()
        screen.blit(instructlabel1,(330,200))
        screen.blit(snakescreen, (550, 200))
        screen.blit(nlabel,(380,110 ))
        
        
        if 500+100 > mouse[0] > 500 and 550 + 50  > mouse[1] > 550:
             pygame.draw.rect(screen, (lred), quitbut)
        else:
             pygame.draw.rect(screen, [255, 0, 0], quitbut)
        if 100+100 > mouse[0] > 100 and 550 + 50 > mouse[1] > 550:
             pygame.draw.rect(screen, (lgreen),  playbut)
        else:
            pygame.draw.rect(screen, (green),  playbut)
        if 900+220 > mouse[0] > 900 and 550 + 50 > mouse[1] > 550:
             pygame.draw.rect(screen, (lyellow),  leadbut)
        else:
             pygame.draw.rect(screen, (yellow),  leadbut)
        screen.blit(playbutfont,(115,560))
        screen.blit(quitbutfont, (515, 560))
        screen.blit(leadbutfont,(915, 560))
        
       
        pygame.display.update()
        clock.tick(60)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopped = False
                sys.exit
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                 if quitbut.collidepoint(mouse):
                      pygame.quit()
                      stopped = False
                      sys.exit
                 if leadbut.collidepoint(mouse):
                      stopped = False
                      screen.fill(white)
                      inlead = True
                      
                      pygame.display.set_caption("Leaderboards")
                      try:
                         afile = open("data.dat","r")
                         lines = afile.read().split()
                         nameslist2 = []
                         scoreslist2 = []                    
                         afile.close()
                         for i in range(0, len(lines)):
                              parts = lines[i].split(",")
                              nameslist2.append(parts[0])
                              scoreslist2.append(parts[1])
                         scoreslabel = myfont.render("Top 10 High Scores", 1, (black))
                         screen.blit(scoreslabel, (400, 100))
                         y = 200
                         length = len(scoreslist2)
                         if length > 10:
                              length = 10

                         for x in range(0, length):
                              namestring = nameslist2[x]
                              score  = leadfont.render(str(x+1) + ".) " + scoreslist2[x] + " scored by " + namestring[0:30], 1 , black)
                              screen.blit(score, (400, y))
                              y = y + 50
                         pygame.display.flip()
                         
               
                         
                         
                         
                      except FileNotFoundError:
                           screen.blit(leadlabel, (100,360))
                           pygame.display.flip()
                      
                      while inlead:
                              
                           for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                     pygame.quit()
                                     stopped = False
                                     sys.exit
                                if event.type == pygame.KEYDOWN:
                                     if event.key == pygame.K_ESCAPE:
                                          pygame.display.set_caption("Snake Game")
                                          pygame.mouse.set_visible(True)
                                          inlead = False
                                          stopped = True   
                

                 if playbut.collidepoint(mouse):
                      pygame.display.set_caption("Game")
                      screen.fill(black)
                      pygame.mouse.set_visible(False)  
                      thesnake = pygame.image.load("block.png").convert()
                      stopped = False
                      ingame = True
                      score = 0
                      snake = Snake(3)
                      xcoord = random.randint(25,1255)
                      ycoord =  random.randint(25,695)
                      food = Food(xcoord,ycoord)
                      checkhit = checkcol()
                      snakecol = snakecollide()
                      snake.x[0] = random.randint(400,800)
                      snake.y[0] = random.randint(300,500)
                      foodgroup.add(food)
                      gameover = False
                      
                      
                      while ingame:
                           snake.update()
                           snakecol.rect.x = snake.x[0]
                           snakecol.rect.y = snake.y[0]
                          
                           for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                     ingame = False
                                     sys.exit
                                     pygame.quit()
                                if event.type == pygame.KEYDOWN:
                                     if event.key == pygame.K_ESCAPE:
                                          pygame.display.set_caption("Snake Game")
                                          pygame.mouse.set_visible(True)
                                          foodgroup.remove(food)
               
                                          ingame = False
                                          stopped = True
                                         
                                     if event.key == pygame.K_p:
                                          paused = True
                                          ingame = False
                                          resumebut = pygame.Rect(100, 550, 100, 50)
                                          quitbut2 = pygame.Rect(900,550,100,50)
                                          resumebutfont = buttonfont2.render("Resume", 1 , (black))
                                          
                                          while paused:
                                               mouse = pygame.mouse.get_pos()
                                               for event in pygame.event.get():
                                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                                         if quitbut2.collidepoint(mouse):
                                                              pygame.quit()
                                                              paused = False
                                                              sys.exit
                                                         if resumebut.collidepoint(mouse):
                                                              pygame.mouse.set_visible(False)
                                                              pygame.display.set_caption("Game")
                                                              paused = False
                                                              ingame = True
                                                              
                                                    if event.type == pygame.QUIT:
                                                         paused = False
                                                         pygame.quit()
                                                         sys.exit()
                                                    if event.type == pygame.KEYDOWN:
                                                         if event.key == pygame.K_ESCAPE:
                                                              foodgroup.remove(food)
                                                              pygame.display.set_caption("Snake Game")
                                                              paused = False
                                                              stopped = True

                                               screen.fill(white)          
                                               if 900+100 > mouse[0] > 900 and 550 + 50  > mouse[1] > 550:
                                                    pygame.draw.rect(screen, (lred), quitbut2)
                                               else:
                                                    pygame.draw.rect(screen, [255, 0, 0], quitbut2)
                                               if 100+100 > mouse[0] >100 and 550 + 50 > mouse[1] >550:
                                                   pygame.draw.rect(screen, (green), resumebut)
                                               else:
                                                   pygame.draw.rect(screen,(lgreen),resumebut)
                                               pygame.display.set_caption("Paused")
                                               pygame.mouse.set_visible(True)
                                               screen.blit(pausedlabel,(200,100))
                                               screen.blit(resumebutfont, (100,560))
                                               screen.blit(quitbutfont, (915, 560))
                                             
                                               pygame.display.update()
                                               
                                     keys = pygame.key.get_pressed()
                                     if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                                          snake.direction = 1
                                     if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                                          snake.direction = 0
                                     if keys[pygame.K_UP] or keys[pygame.K_w]:
                                          snake.direction = 2
                                     if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                                          snake.direction = 3 
                                          

                           if snakecol.rect.colliderect(food):
                                     score = score + 1
                                     snake.length = snake.length + 1
                                     foodgroup.remove(food)
                                     xcoord = random.randint(25,1255)
                                     ycoord = random.randint(25,695)
                                     food = Food(xcoord, ycoord)
                                     foodgroup.add(food)
                                     
                                
                           if snake.x[0] < 0  or snake.x[0] > 1280:
                                ingame = False
                                gameover = True
                                foodgroup.remove(food)
                                pygame.mouse.set_visible(True)
                                
                           if snake.y[0] < 0 or snake.y[0] > 720 :
                                ingame = False
                                gameover = True
                                foodgroup.remove(food)
                                pygame.mouse.set_visible(True)
                                
                                
                           for i in range(2,snake.length):
                                if checkcol.checkcollision(snake,snake.x[0],snake.y[0],snake.x[i],snake.y[i],0):
                                     ingame = False
                                     gameover = True
                                     foodgroup.remove(food)
                                     pygame.mouse.set_visible(True)
                                     
                                     
                           while gameover:
                                 
                                 for event in pygame.event.get():
                                     if event.type == pygame.QUIT:
                                          gameover = False
                                          sys.exit
                                          pygame.quit()
                                     if event.type == pygame.KEYDOWN:
                                          if event.key == pygame.K_ESCAPE:
                                              
                                               gameover = False
                                               stopped = True
                                               pygame.display.set_caption("Snake Game")
                                               pygame.mouse.set_visible(True)
                                          if event.key == pygame.K_RETURN:
                                               result = leaderboardentry()

                                               if result == True:
                                                    nameslist = []
                                                    scoreslist = []

                                                    try:
                                                         thefile = open("data.dat","r+")
                                                    except FileNotFoundError:
                                                         print("Leaderboard file could not be opened creating a new one")
                                                         thefile = open("data.dat", "w+")
                                             
                                                    lines = thefile.read().split()
                                                    thefile.close()
                                                    for i in range(0, len(lines)):
                                                         parts = lines[i].split(",")
                                                         nameslist.append(parts[0])
                                                         scoreslist.append(parts[1])
                                               
                                                    scoreslist.append(score)
                                                    text2 = text.replace(" ","")
                                                    nameslist.append(text2)
                                                    namelist = []
                                                    sortedscores = []
                                                    sortedscores, namelist = bubblesort(scoreslist,nameslist)

                                                    try:
                                                         thefile = open("data.dat","w")
                                                    except FileNotFoundError:
                                                         print("Leaderboard file could not be opened check the directory")

                                                    s = 0
                                                    for s in range(0,len(sortedscores)):
                                                         thefile.write(namelist[s])
                                                         thefile.write(",")
                                                         thefile.write(str(sortedscores[s]))
                                                         thefile.write("\n")
                                                         s = s + 1
                                                         
                                                    thefile.close()         
                                                    
                                                    gameover = False
                                                    stopped = True
                                                    pygame.mouse.set_visible(True)
                                                    

                                 screen.fill(white)
                                 pygame.display.set_caption("Game Over")
                                 endscore = myfont.render("You got a score of " + str(score),1 , (black))
                                 screen.blit(gameoverinstruct,(300,400))
                                 screen.blit(gameoverinstruct2,(300,450))
                                 screen.blit(endscore, (300,280))
                                 pygame.display.flip()

      
                           scorelabel = scorefont.render("Score: " + str(score), 1,white)
                           screen.fill(black)
                           foodgroup.draw(screen)
                           snake.draw(screen, thesnake)
                           screen.blit(scorelabel, (0,0))
                           screen.blit(pauselabel,(630,0))
                           clock.tick(40)
                           pygame.display.update()
                              
gamewindow1()

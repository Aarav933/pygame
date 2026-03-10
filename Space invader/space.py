import pygame 
import random 
import math 
Screenwidth = 1000
Screenheight = 500
Playerstartx = 300
Playerstarty = 400
Enemystartymin = 60
Enemystartymayx = 100
Enemyspeedx = 4
Enemyspeedy = 40
Bulletspeed = 30
Distance  = 20 
pygame.init()
screen = pygame.display.set_mode((Screenwidth, Screenheight))
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (Screenwidth, Screenheight))
pygame.display.set_caption("Space Invader ")
Icon = pygame.image.load('rocket.png')
pygame.display.set_icon(Icon)
playerimg = pygame.image.load('rocket.png')
playerx = Playerstartx
playery = Playerstarty
Playerxchange = 0
Enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numofenemies = 6
for i in range(numofenemies):
    Enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,Screenwidth-64))
    enemyy.append(random.randint(Enemystartymin, Enemystartymayx))
    enemyxchange.append(Enemyspeedx)
    enemyychange.append(Enemyspeedy)
bulletImg = pygame.image.load('bullet.png')
bulletx = 0
bullety = Playerstarty
bulletchangex  = 0 
bulletchangey = Bulletspeed
bulletstate = "ready"
scorevalue = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10
overfont = pygame.font.Font('freesansbold.ttf',64)
def showscore(x,y):
    score = font.render("Score :" +str(scorevalue),True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext():
    overtext = overfont.render("GAME OVER:", True, (255,255,255))
    screen.blit(overtext,(200,250))
def player(x,y):
    screen.blit(playerimg ,(x,y))
def enemy(x,y,i):
    screen.blit(Enemyimg[i] ,(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletImg,  (x +16 , y+10))
def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((enemyx-bulletx)**2 +(enemyy -bullety)**2)
    return distance < distance
running = True 
while running: 
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Playerxchange = -5
            if event.key == pygame.K_RIGHT:
                Playerxchange = 5
            if event.key == pygame.K_SPACE and bulletstate == "ready": 
                bulletx = playerx
                firebullet(bulletx, bullety)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            Playerxchange = 0
        playerx += Playerxchange
        playerx = max(0,min(playerx, Screenwidth - 64))    
        for i in range(numofenemies):
            if enemyy[i]>340:
                for j in range(numofenemies):
                    enemyy[j] = 2000
                gameovertext()
                break 
            enemyx[i] += enemyxchange[i]
            if enemyx[i] <= 0 or enemyx[i] >= Screenwidth - 64:
                enemyxchange[i] *= -1 
                enemyy[i] += enemyychange[i]
            if isCollision(enemyx[i] , enemyy[i] , bulletx , bullety ):
                bullety = Playerstarty
                bulletstate = "ready"
                scorevalue += 1
                enemyx[i] = random.randint(0,Screenwidth -64)
                enemyy[i] = random.randint(Enemystartymin, Enemystartymayx)
            enemy(enemyx[i], enemyy[i], i)
    if bullety <= 0:
        bullety = Playerstarty
        bulletstate = "ready"
    elif bulletstate == "fire":
        firebullet(bulletx, bullety)
        bullety -= bulletchangey
    player(playerx, playery)      
    showscore(textx , texty)
    pygame.display.update()
import pygame 
import random
pygame.init()
spritecolorchangevent = pygame.USEREVENT +1
backgroundcolorchange = pygame.USEREVENT +2
BLUE =  pygame.Color('blue')
LIGHTBLUE =  pygame.Color('lightblue')
DARKBLUE =  pygame.Color('darkblue')
ORANGE =  pygame.Color('orange')
WHITE =  pygame.Color('white')
YELLOW=  pygame.Color('yellow')
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([height,width])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundaryhit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundaryhit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundaryhit = True
        if boundaryhit:
            pygame.event.post(pygame.event.Event(spritecolorchangevent))
            pygame.event.post(pygame.event.Event(backgroundcolorchange))
    def changecolor(self):
        self.image.fill(random.choice([ORANGE,WHITE,YELLOW]))
def changebgcolor():
    global bgcolor
    bgcolor = random.choice([BLUE,LIGHTBLUE,DARKBLUE])
allspritelist = pygame.sprite.Group()
sp1 = Sprite(WHITE, 50,50)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,380)
allspritelist.add(sp1)
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("Sprite bounce")
bgcolor = BLUE
screen.fill(bgcolor)
exit = False
clock = pygame.time.Clock()
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type ==spritecolorchangevent:
            sp1.changecolor()
        elif event.type ==backgroundcolorchange:
            changebgcolor()
    allspritelist.update()
    screen.fill(bgcolor)
    allspritelist.draw(screen)
    pygame.display.flip()
    clock.tick(240)
pygame.QUIT()




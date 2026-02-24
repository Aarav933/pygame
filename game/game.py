import pygame 
import random 
Screenwidth, Screenheight = 500, 400 
Movementspeed = 5
Fontsize = 60
pygame.init()
backgroundimage = pygame.transform.scale(pygame.image.load("gamebackground.jpg"), (Screenwidth, Screenheight))
Font = pygame.font.SysFont("Times New Roman", Fontsize)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color , height, width):
        super().__init__()
        self.image = pygame.Surface([width , height])
        self.image.fill(pygame.Color('blue'))
        pygame.draw.rect(self.image , color , pygame.Rect(0,0,width,height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, Screenwidth - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, Screenheight - self.rect.height), 0)
screen = pygame.display.set_mode((Screenwidth, Screenheight))
pygame.display.set_caption("Sprite Collision Game")
allsprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color('black'), 20 , 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, Screenwidth - sprite1.rect.width) , random.randint(0, Screenheight - sprite1.rect.height)
allsprites.add(sprite1)
sprite2 = Sprite(pygame.Color('red'), 20 , 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, Screenwidth - sprite2.rect.width) , random.randint(0, Screenheight - sprite2.rect.height)
allsprites.add(sprite2)
running ,  won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_x):
            running = False
    if not won: 
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] -keys[pygame.K_LEFT] * Movementspeed)
        y_change = (keys[pygame.K_DOWN] -keys[pygame.K_UP] * Movementspeed)
        sprite1.move(x_change,y_change)
        if sprite1.rect.colliderect(sprite2.rect):
            allsprites.remove(sprite2)
            won = True
    screen.blit(backgroundimage, (0,0))
    allsprites.draw(screen)
    if won:
       win_text = Font.render("You win", True , pygame.Color('black'))
       screen.blit(win_text, ((Screenwidth - win_text.get_width())//2 , 
                              (Screenheight - win_text.get_height())//2))
    pygame.display.flip()
    clock.tick(90)
pygame.quit()
import pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Screen")
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)
text = font.render("Hello Pygame", True, BLACK)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))
    screen.blit(text, (300, 350))
    pygame.display.flip()
pygame.quit()

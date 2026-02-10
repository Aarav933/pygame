import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Adding an image as a background')

background_image = pygame.transform.scale(

pygame.image.load('OIP.jpg').convert(),

(500, 500)

)

image = pygame.transform.scale(

pygame.image.load('OIP (1).jpg').convert(),

(200, 200)

)

image_rect = image.get_rect(

center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110)

)

def game_loop():

    clock = pygame.time.Clock()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False

        display_surface.blit(background_image, (0, 0))

        display_surface.blit(image, image_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':

    game_loop()
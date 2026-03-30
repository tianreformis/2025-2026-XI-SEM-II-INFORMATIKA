#folder name week 8.3 canvas
import pygame

pygame.init()
WIDTH = 800 
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("My First Game")

#variabel warna
RED = (255, 0, 0)

#variabel boolean
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((198, 251, 89)) #rgb code

    pygame.draw.circle(screen, RED, (200,200),150)    

    pygame.display.flip()

pygame.quit()
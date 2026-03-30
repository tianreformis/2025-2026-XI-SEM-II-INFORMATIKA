import pygame
import random
pygame.init()

#mengatur Layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

#Variabel Warna, RGB Color Schema
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

#Game Variable 
score =0
running = True
circle_pos = [400, 300]
circle_radius = 50

#Font untuk Skor
font= pygame.font.SysFont("Times New Roman", 40, bold=True)

#Looping Utama, Buat Game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos= event.pos

            distance =((mouse_pos[0]-circle_pos[0])**2 + (mouse_pos[1]-circle_pos[1])**2)**0.5
            if distance < circle_radius:
                score += 1
   
                circle_pos[0] = random.randint(50, WIDTH-50)
                circle_pos[1] = random.randint(50, HEIGHT-50)
    

    #Mengisi Layar dengan Warna Putih
    screen.fill(BLACK)

    pygame.draw.circle(screen, RED, (circle_pos[0], circle_pos[1]), circle_radius)  # Lingkaran Merah
    score_text = font.render(f"Skor: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    pygame.display.flip()

pygame.quit()
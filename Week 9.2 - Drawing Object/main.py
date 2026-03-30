import pygame

pygame.init()

#mengatur Layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing Objects")

#Variabel Warna, RGB Color Schema
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

#Looping Utama, Buat Game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Mengisi Layar dengan Warna Putih
    screen.fill(BLACK)

    #Menggambar Bentuk
    
    #rect(left, top, width, height)
    pygame.draw.rect(screen,WHITE , (150, 150, 500, 300))  # Persegi Panjang Hijau
    pygame.draw.circle(screen, RED, (400, 300), 100)  # Lingkaran Merah
    #Memperbarui Tampilan
    pygame.display.flip()

pygame.quit()
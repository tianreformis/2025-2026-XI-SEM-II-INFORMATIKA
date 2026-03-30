import pygame
import sys

# 1. Inisialisasi semua modul pygame
pygame.init()

# 2. Mengatur dimensi layar (Lebar, Tinggi)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_surface((SCREEN_WIDTH, SCREEN_HEIGHT))

# 3. Mengatur Judul dan Ikon
pygame.display.set_caption("Petualangan Hebatku")
# icon = pygame.image.load('logo.png') # Pastikan file ada
# pygame.display.set_icon(icon)

# 4. Mengatur Frame Rate (FPS)
clock = pygame.time.Clock()

# --- GAME LOOP ---
running = True
while running:
    # A. EVENT HANDLING (Menangkap input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Jika tombol X diklik
            running = False

    # B. LOGIKA PERMAINAN (Update)
    # (Nanti diisi di sini)

    # C. RENDERING (Menggambar)
    screen.fill((30, 30, 30)) # Membersihkan layar dengan warna abu-abu gelap (RGB)

    # Perbarui tampilan layar
    pygame.display.flip()

    # Membatasi kecepatan game di 60 frame per detik
    clock.tick(60)

# Keluar dari aplikasi dengan bersih
pygame.quit()
sys.exit()
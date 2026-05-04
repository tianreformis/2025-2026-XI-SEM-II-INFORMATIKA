import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BKL di Labirin")

# Level Definition
# 1 = Dinding, 0 = Jalan, 2 = Finish
level1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

level2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

levels = [level1, level2]
current_level_index = 0

try: 
    original_image = pygame.image.load('player.png')
    player_image = pygame.transform.scale(original_image, (32, 32))
except pygame.error:    
    player_image = pygame.Surface((32, 32))
    player_image.fill((255, 0, 0))

player_rect = player_image.get_rect(topleft=(40, 40))
player_speed = 5 
facing_right = True

def can_move(rect, current_map):
    for row_index, row in enumerate(current_map):
        for col_index, tile in enumerate(row):
            if tile == 1:             
                wall_rect = pygame.Rect(col_index * TILE_SIZE, row_index * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if rect.colliderect(wall_rect):
                    return False
    return True

clock = pygame.time.Clock()
running = True

while running:
    current_map = levels[current_level_index]
    screen.fill((255, 255, 255)) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    new_rect = player_rect.copy()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]: new_rect.x -= player_speed; facing_right = False
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: new_rect.x += player_speed; facing_right = True
    if keys[pygame.K_w] or keys[pygame.K_UP]: new_rect.y -= player_speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]: new_rect.y += player_speed

    if can_move(new_rect, current_map):
        player_rect = new_rect

    # --- GAMBAR MAP ---
    for row_index, row in enumerate(current_map):
        for col_index, tile in enumerate(row):
            x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
            if tile == 1:
                pygame.draw.rect(screen, (50, 50, 50), (x, y, TILE_SIZE, TILE_SIZE))
            elif tile == 2:
                pygame.draw.rect(screen, (0, 255, 0), (x, y, TILE_SIZE, TILE_SIZE)) 
                
                
                finish_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                if player_rect.colliderect(finish_rect):
                    current_level_index += 1
                    if current_level_index < len(levels):
                        player_rect.topleft = (40, 40) # Reset posisi pemain
                    else:
                        print("Selamat! Semua level selesai.")
                        running = False

    # --- GAMBAR PLAYER ---
    display_image = player_image 
    if not facing_right:
        display_image = pygame.transform.flip(player_image, True, False)
    
    screen.blit(display_image, player_rect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
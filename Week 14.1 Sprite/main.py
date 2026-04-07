import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#handle error loading image
try:
    #gambar asli 
    original_image = pygame.image.load('player.png')
    #resize gambar
    player_image = pygame.transform.scale(original_image, (64, 64))
except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit()

#player position and speed
player_x = 100
player_y = 100
player_speed = 0.05
facing_right = True #handle arah player

#Looping Game
running = True
while running:
    # Clear the screen with white
    screen.fill((255, 255, 255)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        facing_right = False
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        facing_right = True
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
     
    # Draw the player image at the center
    screen.blit(player_image, (player_x, player_y))  
    
    # Update the display
    pygame.display.flip()  
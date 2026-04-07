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

#Looping Game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen with white
    screen.fill((255, 255, 255))  
    # Draw the player image at the center
    screen.blit(player_image, (WIDTH // 2 - 32, HEIGHT // 2 - 32))  
    
    # Update the display
    pygame.display.flip()  
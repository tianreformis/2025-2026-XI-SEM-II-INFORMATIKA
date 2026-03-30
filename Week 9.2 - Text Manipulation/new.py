import pygame
import sys

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont("Book Antiqua", 40)

#Settings
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
pygame.mixer.music.load("music.mp3")

running = True
while running:
    screen.fill(BLACK)

    text_new_game = font.render("New Game", True, WHITE)
    rect_new_game = text_new_game.get_rect(center=(400,200))
    screen.blit(text_new_game, rect_new_game)

    text_load_game = font.render("Load Game", True, WHITE)
    rect_load_game = text_load_game.get_rect(center=(400,300))
    pygame.draw.rect(screen, BLUE, rect_load_game) 
    screen.blit(text_load_game, rect_load_game)

    text_exit_game = font.render("Exit Game", True, WHITE)
    rect_exit_game = text_exit_game.get_rect(center=(400,400))
    pygame.draw.rect(screen, RED, rect_exit_game) 
    screen.blit(text_exit_game, rect_exit_game)

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if rect_exit_game.collidepoint(event.pos):
                print("Tombol Exit Game Diklik")
                pygame.quit()
                sys.exit()
            elif rect_new_game.collidepoint(event.pos):
                print("Tombol New Game Diklik")

    pygame.display.flip()
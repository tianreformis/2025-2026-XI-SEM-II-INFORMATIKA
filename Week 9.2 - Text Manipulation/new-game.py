import pygame
import sys
import random

pygame.mixer.init()
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Game")

#Font and Colors Setup
font = pygame.font.SysFont("Arial", 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
running = True
pygame.mixer.music.load("music3.mp3")
pygame.mixer.music.play(-1)  # Play music in a loop
pygame.mixer.music.set_volume(0.5)  # Set music volume (0.0 to 1.0)

#event handling/layar
status = "menu"

#settings
player_x = 400
player_y = 300
velocity = 0.05
score = 0
fruit_x = random.randint(50, WIDTH-10)
fruit_y = random.randint(50, HEIGHT-10)

#game loop
while running: 
    screen.fill(BLACK)

    if status =="menu":
        text_new_game = font.render("New Game", True, WHITE)
        rect_new_game = text_new_game.get_rect(center=(400,200))
        screen.blit(text_new_game, rect_new_game)

        text_load_game = font.render("Load Game", True, WHITE)
        rect_load_game = text_load_game.get_rect(center=(400,300))
        screen.blit(text_load_game, rect_load_game)

        text_exit = font.render("Exit", True, WHITE)
        rect_exit = text_exit.get_rect(center=(400,400))
        screen.blit(text_exit, rect_exit)

    elif status =="playing":
        text_score = font.render(f"Score : {score}", True, WHITE)
        rect_score = text_score.get_rect(center=(400,50))
        screen.blit(text_score, rect_score)

        #renderObject       
        text_player = font.render("o", True, WHITE)
        rect_player = text_player.get_rect(center=(player_x,player_y))
        screen.blit(text_player, rect_player)

        text_fruit = font.render("+", True, YELLOW)
        rect_fruit = text_fruit.get_rect(center=(fruit_x,fruit_y))
        screen.blit(text_fruit, rect_fruit)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= velocity            
        if keys[pygame.K_RIGHT]:
            player_x += velocity
        if keys[pygame.K_UP]:
            player_y -= velocity
        if keys[pygame.K_DOWN]:
            player_y += velocity

        
        text_back = font.render("x", True, WHITE)
        rect_back = text_back.get_rect(center=(30,50))
        pygame.draw.rect(screen, RED, rect_back)
        screen.blit(text_back, rect_back)


    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if status == "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if rect_new_game.collidepoint(event.pos):
                        status = "playing"                    
                    elif rect_exit.collidepoint(event.pos):
                        running = False 

            elif status == "playing":
                if rect_back.collidepoint(event.pos):
                    status = "menu"

#https://github.com/tianreformis/2025-2026-XI-SEM-II-INFORMATIKA
           
            


    pygame.display.flip()
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
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

#event handling/layar
status = "menu"

#settings
head_x, head_y = 400.0, 300.0
trail = [(400.0, 300.0)]
velocity = 0.05
spacing = 15
score = 0
snake_length = 1
fruit_x = random.randint(50, WIDTH-50)
fruit_y = random.randint(50, HEIGHT-50)

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

        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            head_x -= velocity
        if keys[pygame.K_RIGHT]:
            head_x += velocity
        if keys[pygame.K_UP]:
            head_y -= velocity
        if keys[pygame.K_DOWN]:
            head_y += velocity

        trail.insert(0, (head_x, head_y))

        #collision detection with fruit
        head_rect = font.render("o", True, WHITE).get_rect(center=(head_x, head_y))
        fruit_rect = font.render("+", True, YELLOW).get_rect(center=(fruit_x, fruit_y))
        if head_rect.colliderect(fruit_rect):
            score += 1
            snake_length += 1
            fruit_x = random.randint(50, WIDTH-50)
            fruit_y = random.randint(50, HEIGHT-50)

   
        snake = []
        dist = 0
        for i in range(len(trail) - 1):
            if len(snake) >= snake_length:
                break
            x1, y1 = trail[i]
            x2, y2 = trail[i + 1]
            segment_dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            dist += segment_dist
            if dist >= spacing:
                snake.append((x1, y1))
                dist = 0

       
        for segment in snake:
            text_segment = font.render("o", True, WHITE)
            rect_segment = text_segment.get_rect(center=(segment[0], segment[1]))
            screen.blit(text_segment, rect_segment)

        text_fruit = font.render("+", True, YELLOW)
        rect_fruit = text_fruit.get_rect(center=(fruit_x,fruit_y))
        screen.blit(text_fruit, rect_fruit)

        
        text_back = font.render("x", True, WHITE)
        rect_back = text_back.get_rect(center=(30,50))
        pygame.draw.rect(screen, RED, rect_back)
        screen.blit(text_back, rect_back)


    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if status == "menu":
                if rect_new_game.collidepoint(event.pos):
                    status = "playing"                    
                elif rect_exit.collidepoint(event.pos):
                    running = False 

            elif status == "playing":
                if rect_back.collidepoint(event.pos):
                    status = "menu"

#https://github.com/tianreformis/2025-2026-XI-SEM-II-INFORMATIKA
            
            
    pygame.display.flip()

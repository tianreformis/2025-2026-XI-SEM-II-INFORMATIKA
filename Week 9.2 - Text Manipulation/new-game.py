import pygame
import sys

pygame.mixer.init()
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Game")

#Font and Colors Setup
font = pygame.font.SysFont("Arial", 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
running = True
pygame.mixer.music.load("music3.mp3")
pygame.mixer.music.play(-1)  # Play music in a loop
pygame.mixer.music.set_volume(0.5)  # Set music volume (0.0 to 1.0)

#event handling/layar
status = "menu"

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
        text_playing = font.render("Playing Game...!", True, WHITE)
        rect_playing = text_playing.get_rect(center=(400,300))
        screen.blit(text_playing, rect_playing)

        text_back = font.render("x", True, WHITE)
        rect_back = text_back.get_rect(center=(30,50))
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
           
            


    pygame.display.flip()
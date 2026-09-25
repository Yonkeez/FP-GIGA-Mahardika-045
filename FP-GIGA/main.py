import pygame
from config import *
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tuyul finding treasure")
    clock = pygame.time.Clock()
    
    game = Game(screen)
    
    running = True
    while running:
        game.handle_events()
        game.update()
        game.draw()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
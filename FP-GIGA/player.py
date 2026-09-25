import pygame
from config import *

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE - 10, TILE_SIZE - 10)
        self.speed = 4

    def update(self, keys, walls):
        dx, dy = 0, 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: dx = -self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: dx = self.speed
        if keys[pygame.K_w] or keys[pygame.K_UP]: dy = -self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: dy = self.speed
        self.move(dx, dy, walls)

    def move(self, dx, dy, walls):
        self.rect.x += dx
        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0: self.rect.right = wall.left
                if dx < 0: self.rect.left = wall.right

        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall):
                if dy > 0: self.rect.bottom = wall.top
                if dy < 0: self.rect.top = wall.bottom

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)
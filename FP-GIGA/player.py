import pygame
from config import *

class Player:
    def __init__(self, x, y):
        hitbox_width = 30   # Ubah lebar hitbox 
        hitbox_height = 30  # Ubah tinggi hitbox   
        self.rect = pygame.Rect(x, y, hitbox_width, hitbox_height)

        self.speed = 4

        self.animations = self.load_spritesheet("assets/player.png", frame_w=64, frame_h=64)     
        self.current_direction = "down"
        self.frame_index = 0.0
        self.animation_speed = 0.15

        self.image = self.animations[self.current_direction][0]

    def load_spritesheet(self, filepath, frame_w=64, frame_h=64):
        sheet = pygame.image.load(filepath).convert_alpha()
        
        animations = {
            "down": [],   
            "left": [],   
            "right": [],  
            "up": []      
        }
        
        directions = ["down", "left", "right", "up"]

        for row_idx, direction in enumerate(directions):
            for col_idx in range(6):
                frame = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
                source_rect = pygame.Rect(col_idx * frame_w, row_idx * frame_h, frame_w, frame_h)
                frame.blit(sheet, (0, 0), source_rect)
                
                # --- UBAH UKURAN DI SINI ---
                frame = pygame.transform.scale(frame, (120, 120))
                
                animations[direction].append(frame)

        return animations
    def update(self, keys, walls):
        dx, dy = 0, 0
        is_moving = False

        if keys[pygame.K_a] or keys[pygame.K_LEFT]: 
            dx = -self.speed
            self.current_direction = "left"
            is_moving = True
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]: 
            dx = self.speed
            self.current_direction = "right"
            is_moving = True
        elif keys[pygame.K_w] or keys[pygame.K_UP]: 
            dy = -self.speed
            self.current_direction = "up"
            is_moving = True
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]: 
            dy = self.speed
            self.current_direction = "down"
            is_moving = True

        self.move(dx, dy, walls)

        if is_moving:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(self.animations[self.current_direction]):
                self.frame_index = 0.0
            self.image = self.animations[self.current_direction][int(self.frame_index)]
        else:
            self.frame_index = 0.0
            self.image = self.animations[self.current_direction][0]

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
        draw_rect = self.image.get_rect(center=self.rect.center)
        

        draw_rect.y -= 10 
        
        surface.blit(self.image, draw_rect)
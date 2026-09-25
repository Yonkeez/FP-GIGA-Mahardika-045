import pygame
from config import *

class Player:
    def __init__(self, x, y):
        # Hitbox (Area tabrakan) berukuran 30x30
        self.rect = pygame.Rect(x, y, TILE_SIZE - 10, TILE_SIZE - 10)
        self.speed = 4

        # Muat sprite sheet dengan ukuran frame yang SUDAH PASTI (64x64)
        self.animations = self.load_spritesheet("assets/player.png", frame_w=64, frame_h=64)
        
        # Pengaturan animasi
        self.current_direction = "down"
        self.frame_index = 0.0
        self.animation_speed = 0.15

        self.image = self.animations[self.current_direction][0]

    def load_spritesheet(self, filepath, frame_w=64, frame_h=64):
        # 1. Load sprite sheet utuh
        sheet = pygame.image.load(filepath).convert_alpha()
        
        animations = {
            "down": [],   # Baris 1
            "left": [],   # Baris 2
            "right": [],  # Baris 3
            "up": []      # Baris 4
        }
        
        directions = ["down", "left", "right", "up"]

        for row_idx, direction in enumerate(directions):
            for col_idx in range(6): # 6 kolom
                # 2. Buat kanvas kosong transparan berukuran 64x64
                frame = pygame.Surface((frame_w, frame_h), pygame.SRCALPHA)
                
                # 3. Tempelkan HANYA area (col_idx, row_idx) dari sheet ke kanvas kosong tadi
                source_rect = pygame.Rect(col_idx * frame_w, row_idx * frame_h, frame_w, frame_h)
                frame.blit(sheet, (0, 0), source_rect)
                
                # 4. (Opsional) Perbesar kanvasnya kalau dirasa kekecilan, misal jadi 80x80
                # frame = pygame.transform.scale(frame, (80, 80))
                
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
        # Pusatkan gambar (64x64) tepat ke atas kotak hitbox (30x30)
        draw_rect = self.image.get_rect(center=self.rect.center)
        # Geser Y agar posisi karakter seolah berdiri pas di kotak grid
        draw_rect.y -= 16 
        surface.blit(self.image, draw_rect)
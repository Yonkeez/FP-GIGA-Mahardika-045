import pygame
from config import *
class Arrow:
    def __init__(self, x, y, direction, speed=6):
        self.direction = direction
        self.speed = speed

        raw_image = pygame.image.load("assets/arrow.png").convert_alpha()

        if direction in ["LEFT", "RIGHT"]:
            self.rect = pygame.Rect(x, y + TILE_SIZE // 2 - 8, 32, 16)
            scaled = pygame.transform.scale(raw_image, (32, 16))
            if direction == "LEFT":
                self.image = pygame.transform.flip(scaled, True, False)
            else:
                self.image = scaled
        else:  
            self.rect = pygame.Rect(x + TILE_SIZE // 2 - 8, y, 16, 32)
            scaled = pygame.transform.scale(raw_image, (32, 16))
            if direction == "DOWN":
                self.image = pygame.transform.rotate(scaled, -90)
            else:  # UP
                self.image = pygame.transform.rotate(scaled, 90)

    def update(self):
        if self.direction == "RIGHT":
            self.rect.x += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed
        elif self.direction == "UP":
            self.rect.y -= self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class ArrowTrap:
    def __init__(self, x, y, direction="RIGHT", cooldown_seconds=1.8):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
        self.direction = direction
        self.cooldown_ms = int(cooldown_seconds * 1000)
        self.last_shot_time = pygame.time.get_ticks()
        self.arrows = []

        # Muat gambar balok perangkap
        raw_trap = pygame.image.load("assets/trap_block.png").convert_alpha()
        scaled_trap = pygame.transform.scale(raw_trap, (TILE_SIZE, TILE_SIZE))

        # Rotasi balok perangkap jika ada indikator arahnya
        if direction == "DOWN":
            self.image = pygame.transform.rotate(scaled_trap, -90)
        elif direction == "LEFT":
            self.image = pygame.transform.flip(scaled_trap, True, False)
        elif direction == "UP":
            self.image = pygame.transform.rotate(scaled_trap, 90)
        else:
            self.image = scaled_trap

    def update(self, walls):
        current_time = pygame.time.get_ticks()
        
        if current_time - self.last_shot_time >= self.cooldown_ms:
            spawn_x, spawn_y = self.rect.x, self.rect.y
            
            if self.direction == "RIGHT":
                spawn_x += TILE_SIZE
            elif self.direction == "LEFT":
                spawn_x -= 32
            elif self.direction == "DOWN":
                spawn_y += TILE_SIZE
            elif self.direction == "UP":
                spawn_y -= 32

            self.arrows.append(Arrow(spawn_x, spawn_y, self.direction))
            self.last_shot_time = current_time

        for arrow in self.arrows[:]:
            arrow.update()
            for wall in walls:
                if arrow.rect.colliderect(wall):
                    if arrow in self.arrows:
                        self.arrows.remove(arrow)
                    break

    def check_player_collision(self, player_rect):
        for arrow in self.arrows[:]:
            if arrow.rect.colliderect(player_rect):
                self.arrows.remove(arrow)
                return True
        return False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for arrow in self.arrows:
            arrow.draw(surface)
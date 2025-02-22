import pygame


class TestEntity:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (18, 201, 12)
    
    def draw(self, surface, camera):
        adjusted_rect = camera.apply(self.rect)
        pygame.draw.rect(surface, self.color, adjusted_rect)
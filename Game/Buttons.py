import pygame


class TestButton:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.text = text
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 0))
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Button:
    def __init__(self, x, y, width, height, text, font_size, resize_factor):
        self.rect = pygame.Rect(x, y, width * resize_factor, height * resize_factor)
        self.text = text
        self.font = pygame.font.Font(None, int(font_size * resize_factor))
        self.current_color = (75, 75, 75)
        self.current_text_color = (255, 255, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.current_color, self.rect)
        text_surface = self.font.render(self.text, True, self.current_text_color)
        text_rect = text_surface.get_rect(center = self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update_color(self, mouse_pos, hover_color):
        if self.is_clicked(mouse_pos):
            self.current_color = hover_color
            self.current_text_color = (0, 0, 0)
        else:
            self.current_color = (75, 75, 75)
            self.current_text_color = (255, 255, 255)
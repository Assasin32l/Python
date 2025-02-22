import pygame


class Text:
    def __init__(self, x, y, width, height, color, text_color, text, font_style, font_size, resize_factor):
        self.rect = pygame.Rect(x, y, width * resize_factor, height * resize_factor)
        self.text = text
        self.font = pygame.font.SysFont(font_style, int(font_size * resize_factor))
        self.color = color
        self.text_color = text_color
    
    def draw(self, surface, orientation = "center"):        
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)

        if orientation == "center":
            text_rect = text_surface.get_rect(center = self.rect.center)
        
        elif orientation == "left":
            text_rect = text_surface.get_rect(left = self.rect.left, centery = self.rect.centery)

        elif orientation == "right":
            text_rect = text_surface.get_rect(right = self.rect.right, centery = self.rect.centery)
        
        surface.blit(text_surface, text_rect)
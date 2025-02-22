import pygame


class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dragging = False
        self.last_mouse_pos = (0, 0)
    
    def start_drag(self, mouse_pos):
        self.dragging = True
        self.last_mouse_pos = mouse_pos
    
    def stop_drag(self):
        self.dragging = False
    
    def update(self, mouse_pos):
        if self.dragging:
            dx = mouse_pos[0] - self.last_mouse_pos[0]
            dy = mouse_pos[1] - self.last_mouse_pos[1]
            self.x += dx
            self.y += dy
            self.last_mouse_pos = mouse_pos
    
    def apply(self, rect):
        return rect.move(self.x, self.y)
from Camera import Camera
from Text_Field import *
from Entitys import *
from Buttons import *
import ctypes
import pygame
import sys


def createEntitys():
    return 0

def createButtons():
    global new_project_button, load_project_button, settings_button, about_button, quit_button
    global back_button

    new_project_button = Button(window_size[0] // 2 - 85, window_size[1] // 2 - 120 * resize_factor, 300, 50, "NEW PROJECT", 40, resize_factor)
    load_project_button = Button(window_size[0] // 2 - 85, window_size[1] // 2 - 60 * resize_factor, 300, 50, "LOAD PROJECT", 40, resize_factor)
    settings_button = Button(window_size[0] // 2 - 85, window_size[1] // 2, 300, 50, "SETTINGS", 40, resize_factor)
    about_button = Button(window_size[0] // 2 - 85, window_size[1] // 2 + 60 * resize_factor, 300, 50, "ABOUT", 40, resize_factor)
    quit_button = Button(window_size[0] // 2 - 85, window_size[1] // 2 + 120 * resize_factor, 300, 50, "QUIT", 40, resize_factor)

def createText_Fields():
    global logic_sim, author, version

    logic_sim = Text(0, 0, 1920, 216, (30, 30, 30), (255, 255, 255), "LOGIC SIMULATOR", None, 100, resize_factor)
    author = Text(0, window_size[1] * 0.95, 960, 54, (30, 30, 30), (90, 90, 90), "   Created by: Alexander Scheidler", None, 41, resize_factor)
    version = Text(window_size[0] * 0.5, window_size[1] * 0.95, 960, 54, (30, 30, 30), (90, 90, 90), "Version: 1.0.0 (alpha)  Last Update: 22/Feb/25   ", None, 41, resize_factor)


def start():
    global window_size, window, camera, resize_factor

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()

    window_size = (1280, 720)
    #window_size = (1920, 1080)
    window = pygame.display.set_mode(window_size)
    resize_factor = window_size[0] / 1920

    pygame.display.set_caption("Logic Simulator")

    camera = Camera()

    createEntitys()
    createButtons()
    createText_Fields()
    

def mainLoop():
    global mouse_pos, current_screen

    running = True
    current_screen = "main_menu"

    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if current_screen == "main_menu":
                        if new_project_button.is_clicked(mouse_pos):
                            current_screen = "new_project_screen"
                        
                        elif load_project_button.is_clicked(mouse_pos):
                            current_screen = "load_project_screen"

                        elif settings_button.is_clicked(mouse_pos):
                            current_screen = "settings"
                    
                        elif about_button.is_clicked(mouse_pos):
                            current_screen = "about_screen"
                    
                        elif quit_button.is_clicked(mouse_pos):
                            running = False

            elif event.type == pygame.QUIT:
                running = False
        
        
        window.fill((40, 40, 40))

        if current_screen == "main_menu":
            new_project_button.update_color(mouse_pos, (255, 255, 255))
            load_project_button.update_color(mouse_pos, (255, 255, 255))
            settings_button.update_color(mouse_pos, (255, 255, 255))
            about_button.update_color(mouse_pos, (255, 255, 255))
            quit_button.update_color(mouse_pos, (255, 60, 60))

            new_project_button.draw(window)
            load_project_button.draw(window)
            settings_button.draw(window)
            about_button.draw(window)
            quit_button.draw(window)

            logic_sim.draw(window)
            author.draw(window, "left")
            version.draw(window, "right")
        
        elif current_screen == "new_project_screen":
            pass

        elif current_screen == "load_project_screen":
            pass

        elif current_screen == "settings":
            pass

        elif current_screen == "about_screen":
            pass

        pygame.display.flip()


def main():
    pygame.init()


    start()
    
    mainLoop()


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
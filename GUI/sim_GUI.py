import pygame
import pygame_gui

class sim_GUI:
    def __init__(self, globals, surface):
        self.globals = globals
        self.manager = pygame_gui.UIManager((self.globals.GUI_WIDTH, self.globals.pixels(self.globals.CANVAS_SIZE_y)))
        self.surface = surface

        self.make_button()

    def make_button(self):
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (100, 40)),
                                                    text='Say Hello',
                                                    manager=self.manager)
        print("button")

    def draw_ui(self):

        self.globals.BACKGROUND.blit(self.globals.GUI_SURFACE, (self.globals.pixels(self.globals.CANVAS_SIZE_X), 0))
        self.manager.draw_ui(self.globals.GUI_SURFACE)


    def process_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.hello_button:
                    print('Hello World!')
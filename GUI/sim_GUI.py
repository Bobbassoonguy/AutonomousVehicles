import pygame
import pygame_gui
import Colors

class sim_GUI:
    def __init__(self, globals, surface):
        self.globals = globals
        self.manager = pygame_gui.UIManager((self.globals.GUI_WIDTH + (self.globals.pixels(self.globals.CANVAS_SIZE_X)), self.globals.pixels(self.globals.CANVAS_SIZE_y)))
        self.surface = surface

        # self.make_button()
        self.vehicles_panel()

    def make_button(self):
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.x(10),10), (100, 40)),
                                                    text='Say Hello',
                                                    manager=self.manager)
        print("button")

    def vehicles_panel(self):
        this_pos = [self.x(10),40]

        self.vehicle_info_hidden = True

        self.vehicle_name = pygame_gui.elements.ui_label.UILabel(pygame.Rect(this_pos[0], this_pos[1],100,20), "Vehicle 1", manager=self.manager)
        self.show_vehicle_info = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(this_pos[0] + 110,this_pos[1], 20, 20),
                                                    text='V',
                                                    manager=self.manager)

    def vehicle_info_panel(self):
        if not self.vehicle_info_hidden:
            this_vehicle_pos = [0,0]
            this_vehicle_vel = [0, 0]
            this_vehicle_accel = [0, 0]
            this_vehicle_turn_rad = round(0, 2)

            info_string = "Position:     " + str(this_vehicle_pos) + "<br>Velocity:     " + str(
                this_vehicle_vel) + "<br>Acceleration: " + str(this_vehicle_accel) + "<br>Turn Radius:   " + str(
                this_vehicle_turn_rad)
            self.vehicle_info = pygame_gui.elements.ui_text_box.UITextBox(info_string,
                                                                          pygame.Rect(self.x(10), 40 + 25,
                                                                                      125 + 55, 150), self.manager)
        else:
            self.vehicle_info.hide()
            print("Kill text box")


    def x(self, x):
        return self.globals.pixels(self.globals.CANVAS_SIZE_X)+x

    def draw_ui(self):
        pygame.draw.rect(self.globals.BACKGROUND, (221, 221, 221), (self.globals.pixels(self.globals.CANVAS_SIZE_X),0,self.globals.GUI_WIDTH,self.globals.pixels(self.globals.CANVAS_SIZE_y)))

        self.globals.BACKGROUND.blit(self.globals.GUI_SURFACE, (0, 0))
        self.manager.draw_ui(self.globals.GUI_SURFACE)


    def process_events(self, event):
        self.manager.process_events(event)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.show_vehicle_info:
                    print("Should toggle vehicle info")
                    self.vehicle_info_hidden = not self.vehicle_info_hidden
                    self.vehicle_info_panel()
                    self.manager.update(self.globals.FPS)
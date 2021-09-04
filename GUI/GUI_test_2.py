import pygame
import pygame_gui
import Colors
from utils import rgb2hex

class GUIVehicle:
    def __init__(self, manager, x, y, name, color=(255,255,255)):
        self.manager = manager
        self.x = x
        self.y = y
        self.name = name
        self.color = str(rgb2hex(color[0],color[1],color[2]))
        # self.color = "#ffffff"

        self.vehicle_pos = [0, 0]
        self.vehicle_vel = [0, 0]
        self.vehicle_accel = [0, 0]
        self.vehicle_turn_rad = round(0, 2)

        self.INTER_MARGINS = 2
        self.LABEL_HEIGHT = 32
        self.OVERALL_WIDTH = 150
        self.TEXT_BOX_HEIGHT = 80

        info_string = "<font face=Roboto color=regular_text><font color=#FFFFFF size=3>Position:     " + str(self.vehicle_pos) + "<br>Velocity:     " + str(
            self.vehicle_vel) + "<br>Acceleration: " + str(self.vehicle_accel) + "<br>Turn Radius:   " + str(
            self.vehicle_turn_rad) + "</font>"

        self.info_shown = False

        self.label = pygame_gui.elements.ui_text_box.UITextBox("<font face=Roboto color=regular_text><font color=" + self.color + " size=3><b>" + self.name + "</b>",
                                                                          pygame.Rect(self.x, self.y,
                                                                                      self.OVERALL_WIDTH - self.INTER_MARGINS - self.LABEL_HEIGHT,
                                                                                      self.LABEL_HEIGHT), manager=self.manager)

        self.info_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.x + (self.OVERALL_WIDTH - self.LABEL_HEIGHT),self.y, self.LABEL_HEIGHT, self.LABEL_HEIGHT),
                                                    text="v",
                                                    manager=self.manager)
        self.info_box = pygame_gui.elements.ui_text_box.UITextBox(info_string,
                                                                          pygame.Rect(self.x, self.y+self.LABEL_HEIGHT+self.INTER_MARGINS,
                                                                                      self.OVERALL_WIDTH, self.TEXT_BOX_HEIGHT), manager=self.manager)
        self.info_box.hide()

    def update_info_box_toggle(self):
        if self.info_shown:
            self.info_box.show()
            self.info_button.set_text("^")
        else:
            self.info_box.hide()
            self.info_button.set_text("v")

    def update_params(self, pos, vel, accel, rad):
        self.vehicle_pos = pos
        self.vehicle_vel = vel
        self.vehicle_accel = accel
        self.vehicle_turn_rad = round(rad, 2)
        print("self.vehicle_pos:", self.vehicle_pos)

        info_string = "<font face=Roboto color=regular_text><font color=#FFFFFF size=3>Position:     " + str(
            self.vehicle_pos) + "<br>Velocity:     " + str(
            self.vehicle_vel) + "<br>Acceleration: " + str(self.vehicle_accel) + "<br>Turn Radius:   " + str(
            self.vehicle_turn_rad) + "</font>"

        self.info_box.html_text = info_string

    def get_height(self):
        if self.info_shown:
            return self.LABEL_HEIGHT+self.INTER_MARGINS+self.TEXT_BOX_HEIGHT
        else:
            return self.LABEL_HEIGHT

    def update_position(self, x, y):
        self.x = x
        self.y = y
        self.label.set_position((self.x, self.y))
        self.info_button.set_position((self.x + (self.OVERALL_WIDTH - self.LABEL_HEIGHT), self.y))
        self.info_box.set_position((self.x, self.y+self.LABEL_HEIGHT+self.INTER_MARGINS))


class SimTestGUI:
    def __init__(self, surface, canvas_size_x, canvas_size_y):
        self.width = 200 # pixels
        self.width_offset = canvas_size_x - self.width # pixels
        self.height = canvas_size_y
        self.manager = pygame_gui.UIManager((self.width + self.width_offset, self.height))
        self.surface = surface
        self.manager.add_font_paths("Roboto", "data/fonts/Roboto/Roboto-Regular.ttf")
        self.manager.preload_fonts([{'name': 'Roboto', 'html_size': 2, 'style': 'regular'},
                                    {'name': 'Roboto', 'html_size': 3, 'style': 'regular'},
                                    {'name': 'Roboto', 'html_size': 4.5, 'style': 'regular'},
                                    {'name': 'Roboto', 'html_size': 6, 'style': 'regular'},
                                    {'name': 'Roboto', 'html_size': 2, 'style': 'bold'},
                                    {'name': 'Roboto', 'html_size': 3, 'style': 'bold'},
                                    {'name': 'Roboto', 'html_size': 4.5, 'style': 'bold'},
                                    {'name': 'Roboto', 'html_size': 6, 'style': 'bold'}
                                    ])

        self.num_of_vehicles = 6
        self.vehicles_display_position_x = self.x(10)
        self.vehicles_display_position_y = 10
        self.vehicles = []
        self.make_vehicles()


    def make_button(self):
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((self.x(10),10), (100, 40)),
                                                    text='Say Hello',
                                                    manager=self.manager)
        print("button")

    def make_text_box(self):
        self.text_box = pygame_gui.elements.ui_text_box.UITextBox("Text and boxy stuff",
                                                                          pygame.Rect(self.x(10), 40 + 25,
                                                                                      125 + 55, 150), manager=self.manager)
    def make_vehicles(self):
        disp_y_inc = self.vehicles_display_position_y
        for i in range(self.num_of_vehicles):
            self.vehicles.append(GUIVehicle(self.manager, self.vehicles_display_position_x, disp_y_inc, "Vehicle "+str(i+1)))
            disp_y_inc += self.vehicles[i].get_height() + 10

    def update_vehicle_list_positions(self):
        disp_y_inc = self.vehicles_display_position_y
        self.vehicles[0].update_position(self.vehicles_display_position_x, disp_y_inc)
        for i in range(1,self.num_of_vehicles):
            disp_y_inc += self.vehicles[i-1].get_height() + 10
            self.vehicles[i].update_position(self.vehicles_display_position_x, disp_y_inc)

    def x(self, x):
        return x + self.width_offset

    def process_event(self, event):
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            for i in self.vehicles:
                if event.ui_element == i.info_button:
                    i.info_shown = not i.info_shown
                    i.update_info_box_toggle()
                    self.update_vehicle_list_positions()

    def manager_event_process(self, event):
        self.manager.process_events(event)

    def update_manager(self, time_delta):
        self.manager.update(time_delta)

    def draw_ui(self):
        self.manager.draw_ui(self.surface)


pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

gui = SimTestGUI(window_surface, 800, 600)


clock = pygame.time.Clock()
is_running = True

posTest = [0,0]

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            gui.process_event(event)

        gui.manager_event_process(event)


    pygame.draw.rect(background,Colors.MAP_CYAN,(150,125,250,175),6,4)
    posTest[0] += .01
    gui.vehicles[1].update_params(posTest, [0,0], [0,0], 0.5)


    gui.update_manager(time_delta)

    window_surface.blit(background, (0, 0))

    gui.draw_ui()

    pygame.display.update()
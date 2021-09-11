from typing import List, Any

import pygame
import Vehicle
import GLOBALS
import Colors
import Object
import Vector
import RoadMap
import pygame_gui
import GUI_test_2

#this is a new change
class Scenario:
    def __init__(self, name, disp_x=1000, disp_y=1000, pix=15):
        #GLOBAL VARIABLES
        self.globals = GLOBALS.Globals(disp_x=disp_x, disp_y=disp_y, pix=pix)
        self.globals.ROAD_MIN_CURVE_RAD = 12
        self.globals.FPS = 60

        self.name = name
        self.vehicles = []  # type: List[Vehicle]
        # vehicles: List[Vehicle] # Python 3.6 syntax, PEP 526

        self.road_map = RoadMap.RoadMap(self,self.globals)

        pygame.display.set_caption(self.name)

        self.GUI = GUI_test_2.SimTestGUI(self.globals.BACKGROUND, self.globals.CANVAS_SIZE_X + self.globals.GUI_WIDTH, self.globals.CANVAS_SIZE_Y)

        self.globals.BACKDROP.fill((18, 20, 26))  # (18, 20, 26)


    def draw(self):
        for i in self.vehicles:
            i.draw()
        self.road_map.draw_lines(road_segment_points=True)

        self.globals.BACKGROUND.blit(self.globals.BACKDROP, (0, 0))
        self.globals.BACKGROUND.blit(self.globals.ROAD_SURFACE, (0, 0))
        self.globals.BACKGROUND.blit(self.globals.VEHICLE_SURFACE, (0, 0))

        pygame.draw.rect(self.globals.BACKDROP, Colors.MAP_CYAN, (1000, 125, 250, 175), 6, 4)

        self.GUI.draw_ui()
        pygame.display.update()

    def addCar(self, x=10, y=10, fill_color=Colors.CAR_GREEN_FILL, outline_color=Colors.CAR_GREEN_LINE):
        vehicle_to_add = Vehicle.Vehicle(self, self.globals, x, y, fill_color, outline_color)
        self.vehicles.append(vehicle_to_add)


from typing import List, Any

import pygame
import Vehicle
import GLOBALS
import Colors
import Object
import Vector
import RoadMap

#this is a new change
class Scenario:
    def __init__(self, name, disp_x=200, disp_y=200, pix=5):
        #GLOBAL VARIABLES
        self.globals = GLOBALS.Globals(disp_x=disp_x, disp_y=disp_y, pix=pix)
        self.globals.ROAD_MIN_CURVE_RAD = 12
        self.globals.FPS = 60

        self.name = name
        self.vehicles = []  # type: List[Vehicle]
        # vehicles: List[Vehicle] # Python 3.6 syntax, PEP 526

        self.road_map = RoadMap.RoadMap(self,self.globals)

        pygame.display.set_caption(self.name)

    def draw(self):
        self.globals.MAIN_SURFACE.fill((18, 20, 26))
        for i in self.vehicles:
            i.draw()

        self.road_map.draw_lines(road_segment_points=True)

    def addCar(self, x=10, y=10, fill_color=Colors.CAR_GREEN_FILL, outline_color=Colors.CAR_GREEN_LINE):
        vehicle_to_add = Vehicle.Vehicle(self, self.globals, x, y, fill_color, outline_color)
        self.vehicles.append(vehicle_to_add)


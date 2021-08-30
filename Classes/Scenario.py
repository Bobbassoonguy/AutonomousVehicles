from typing import List, Any

import pygame
import Vehicle

#this is a new change
class Scenario:
    def __init__(self, name):
        #GLOBAL VARIABLES
        self.CANVAS_SIZE_X = 1000
        self.CANVAS_SIZE_y = 1000
        self.PIXELS_PER_METER = 20
        self.ROAD_MIN_CURVE_RAD = 10
        self.FPS = 60

        self.name = name
        self.vehicles = []  # type: List[Vehicle]
        # vehicles: List[Vehicle] # Python 3.6 syntax, PEP 526


        self.screen = pygame.display.set_mode([self.CANVAS_SIZE_X, self.CANVAS_SIZE_y])
        pygame.display.set_caption(self.name)

    def main(self):
        self.screen.fill((18, 20, 26))
        for i in self.vehicles:
            i.draw()
        pygame.display.flip()

    def addCar(self):
        vehicle_to_add = Vehicle.Vehicle(self)
        self.vehicles.append(vehicle_to_add)

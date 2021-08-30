import pygame
import Shape

class CLASSNAME:
    def __init__(self, parent, globals, points):
        self.parent = parent
        self.globals = globals
        self.surface = self.globals.MAIN_SURFACE
        self.points = points
        self.velocity = [0, 0]  # a velocity vector in m/s
        self.acceleration = [0, 0]  # an acceleration vector in m/s^2
        self.shape = Shape

    def funcone(self):
        #foo bar
        print("Hello")
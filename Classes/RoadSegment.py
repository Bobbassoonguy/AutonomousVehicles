import pygame
import Vector

class RoadSegment:
    def __init__(self, parent_MapSegment, globals, start_point, end_point, arc_radius=0):
        self.parent = parent_MapSegment
        self.globals = globals
        self.start_point = start_point
        self.end_point = end_point
        self.arc_radius = arc_radius

    def draw(self):
        width = 3.66
        #TODO make a thing that creates a rectangle based on the two points

    def centerline_as_vector(self):
        return Vector.Vector(self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])




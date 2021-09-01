import pygame
import Vector
import GLOBALS

class RoadSegment:
    def __init__(self, parent_MapSegment, globals, start_point, end_point, arc_radius=0):
        self.parent = parent_MapSegment
        self.globals = globals
        self.start_point = start_point
        self.end_point = end_point
        self.arc_radius = arc_radius

    def draw(self, l1, l2):
        width = l1+l2  # 3.66
        # TODO make a thing that creates a rectangle based on the two points
        v = self.centerline_as_vector()
        v1 = v.rotate(90)
        v2 = v.rotate(270)
        v1.set_magnitude(l1)
        v2.set_magnitude(l2)
        v1.draw_starting_from(GLOBALS,self.end_point)
        v2.draw_starting_from(GLOBALS, self.end_point)
        v2.draw_starting_from(GLOBALS, self.start_point)
        v1.draw_starting_from(GLOBALS, self.start_point)
        points = {self.end_point+v1, self.end_point+v2, self.start_point+v2, self.start_point+v1}

    def centerline_as_vector(self):
        return Vector.Vector(self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])




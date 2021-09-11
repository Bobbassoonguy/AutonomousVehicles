import pygame

import Colors
import Vector
import copy
import math
import Tools

class RoadSegment:
    def __init__(self, parent_MapSegment, globals, start_point, end_point, arc_radius=0):
        self.parent = parent_MapSegment
        self.globals = globals
        self.start_point = start_point
        self.end_point = end_point
        self.arc_radius = arc_radius

    def get_corners(self):
        width = 3.66  # 3.66
        v = self.centerline_as_vector()
        v1 = Vector.Vector(v.x, v.y)
        v1.rotate(90)
        v2 = Vector.Vector(v.x, v.y)
        v2.rotate(270)
        v1.set_magnitude(width)
        v2.set_magnitude(width)
        return [(v1 + self.end_point).list(), (v2 + self.end_point).list(), (v2 + self.start_point).list(),
                  (v1 + self.start_point).list()]

    def draw(self, color=Colors.ROAD_ORANGE):
        if self.arc_radius == 0:
            points = self.get_corners()
            points[0] = self.globals.point_to_pixels(points[0])
            points[1] = self.globals.point_to_pixels(points[1])
            points[2] = self.globals.point_to_pixels(points[2])
            points[3] = self.globals.point_to_pixels(points[3])
            pygame.draw.polygon(self.globals.ROAD_SURFACE, color, points, width=0)
        else:
            Tools.draw_arc(self.globals,self.globals.ROAD_SURFACE,self.start_point,self.end_point,self.arc_radius,3.66,color)
            Tools.draw_arc(self.globals, self.globals.ROAD_SURFACE, self.start_point, self.end_point, self.arc_radius, 3.66, color, inside=False)


    def centerline_as_vector(self):
        return Vector.Vector(self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])




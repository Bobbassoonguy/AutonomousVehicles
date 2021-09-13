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
        lanes_forward, lanes_reverse = self.parent.get_lane_nums()
        v = self.centerline_as_vector()
        v1 = Vector.Vector(v.x, v.y)
        v1.rotate(90)
        v2 = Vector.Vector(v.x, v.y)
        v2.rotate(270)
        v1.set_magnitude(lanes_forward * self.globals.LANE_WIDTH)
        v2.set_magnitude(lanes_reverse * self.globals.LANE_WIDTH)
        return [(v1 + self.end_point).list(), (v2 + self.end_point).list(), (v2 + self.start_point).list(),
                  (v1 + self.start_point).list()]

    def draw(self, color=Colors.ROAD_ORANGE):
        lanes_forward, lanes_reverse = self.parent.get_lane_nums()
        if self.arc_radius == 0:
            points = self.get_corners()
            points[0] = self.globals.point_to_pixels(points[0])
            points[1] = self.globals.point_to_pixels(points[1])
            points[2] = self.globals.point_to_pixels(points[2])
            points[3] = self.globals.point_to_pixels(points[3])
            pygame.draw.polygon(self.globals.ROAD_SURFACE, color, points, width=0)
            Tools.draw_double_line(self.globals,self.globals.ROAD_SURFACE,self.start_point,self.end_point,self.globals.ROAD_LINE_WIDTH, Colors.ROAD_LINE_YELLOW)

            for i in range(1,lanes_forward):
                v = self.centerline_as_vector()
                v1 = Vector.Vector(v.x, v.y)
                v1.rotate(90)
                v1.set_magnitude(i * self.globals.LANE_WIDTH)
                Tools.draw_dashed_line(self.globals,self.globals.ROAD_SURFACE,(v1+self.start_point).list(),(v1+self.end_point).list(),self.globals.ROAD_LINE_WIDTH,Colors.ROAD_LINE_WHITE,dash_length=self.globals.ROAD_DASH_LENGTH)
            for i in range(1,lanes_reverse):
                v = self.centerline_as_vector()
                v1 = Vector.Vector(v.x, v.y)
                v1.rotate(270)
                v1.set_magnitude(i * self.globals.LANE_WIDTH)
                Tools.draw_dashed_line(self.globals,self.globals.ROAD_SURFACE,(v1+self.start_point).list(),(v1+self.end_point).list(),self.globals.ROAD_LINE_WIDTH,Colors.ROAD_LINE_WHITE,dash_length=self.globals.ROAD_DASH_LENGTH)

        else:
            if self.arc_radius < 0:
                Tools.draw_arc(self.globals, self.globals.ROAD_SURFACE, self.start_point, self.end_point,
                               self.arc_radius, lanes_forward * self.globals.LANE_WIDTH, color)
                Tools.draw_arc(self.globals, self.globals.ROAD_SURFACE, self.start_point, self.end_point,
                               self.arc_radius, lanes_reverse * self.globals.LANE_WIDTH, color, inside=False)
            else:
                Tools.draw_arc(self.globals, self.globals.ROAD_SURFACE, self.start_point, self.end_point,
                               self.arc_radius, lanes_reverse * self.globals.LANE_WIDTH, color)
                Tools.draw_arc(self.globals, self.globals.ROAD_SURFACE, self.start_point, self.end_point,
                               self.arc_radius, lanes_forward * self.globals.LANE_WIDTH, color, inside=False)

            Tools.draw_double_arc(self.globals,self.globals.ROAD_SURFACE,self.start_point,self.end_point,self.arc_radius,self.globals.ROAD_LINE_WIDTH,Colors.ROAD_LINE_YELLOW)
            center, start_angle, end_angle = Tools.two_point_arc_circle(self.start_point, self.end_point, self.arc_radius)

            for i in range(1,lanes_forward):
                Tools.draw_dashed_arc(self.globals,self.globals.ROAD_SURFACE,center,start_angle,end_angle,self.arc_radius+(self.globals.LANE_WIDTH * i)-(self.globals.ROAD_LINE_WIDTH/2),self.globals.ROAD_LINE_WIDTH,Colors.ROAD_LINE_WHITE,inside=True,dash_length=self.globals.ROAD_DASH_LENGTH)

            for i in range(1,lanes_reverse):
                Tools.draw_dashed_arc(self.globals, self.globals.ROAD_SURFACE, center, start_angle, end_angle,
                                      self.arc_radius - (self.globals.LANE_WIDTH * i) - (
                                                  self.globals.ROAD_LINE_WIDTH / 2), self.globals.ROAD_LINE_WIDTH,
                                      Colors.ROAD_LINE_WHITE, inside=True, dash_length=self.globals.ROAD_DASH_LENGTH)


    def centerline_as_vector(self):
        return Vector.Vector(self.end_point[0] - self.start_point[0], self.end_point[1] - self.start_point[1])




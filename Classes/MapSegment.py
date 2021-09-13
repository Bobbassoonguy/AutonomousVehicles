import pygame
import Vector
import RoadSegment
import Colors
import Tools

class MapSegment:
    def __init__(self, parent_MapRoad, globals, start_point, end_point, arc_radius=0):
        self.parent = parent_MapRoad
        self.globals = globals
        self.start_point = start_point
        self.end_point = end_point
        self.arc_radius = arc_radius

        self.road_segment = RoadSegment.RoadSegment(self,self.globals,[self.start_point[0],self.start_point[1]], [self.end_point[0], self.end_point[1]], arc_radius=self.arc_radius)

    def get_as_vector(self):
        return Vector.Vector(self.end_point[0]-self.start_point[0], self.end_point[1]-self.start_point[1])

    def draw_as_line(self, endpoints=False):
        if self.arc_radius == 0:
            pygame.draw.aaline(self.globals.ROAD_SURFACE, Colors.MAP_ORANGE, self.globals.point_to_pixels(self.start_point), self.globals.point_to_pixels(self.end_point))
        else:
            Tools.draw_arc(self.globals,self.globals.ROAD_SURFACE,self.start_point,self.end_point,self.arc_radius,1/self.globals.PIXELS_PER_METER,Colors.MAP_ORANGE)
        if endpoints:
            pygame.draw.circle(self.globals.ROAD_SURFACE, Colors.MAP_ORANGE, self.globals.point_to_pixels(self.start_point), 3)
            pygame.draw.circle(self.globals.ROAD_SURFACE, Colors.MAP_ORANGE, self.globals.point_to_pixels(self.end_point), 3)

    def draw_road_segment(self):
        self.road_segment.draw()

    def get_lane_nums(self):
        return [self.parent.lanes_forward,self.parent.lanes_reverse]


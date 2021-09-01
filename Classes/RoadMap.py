import pygame
import MapRoad

class RoadMap:
    def __init__(self, parent, globals):
        self.parent = parent
        self.globals = globals

        self.roads = []

    def add_road(self, points):
        new_road = MapRoad.MapRoad(self,self.globals,points)
        self.roads.append(new_road)

    def draw_lines(self, road_segment_points=False):
        for i in self.roads:
            i.draw_as_line(road_nodes=road_segment_points)

    def draw_roads(self):
        for i in self.roads:
            i.draw_road_segments()
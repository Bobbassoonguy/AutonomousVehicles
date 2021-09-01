import pygame
import MapSegment

class MapRoad:
    def __init__(self, parent_RoadMap, globals, points):
        self.parent = parent_RoadMap
        self.globals = globals

        self.points = points

        self.segments = []
        self.create_segments()

    def num_segments(self):
        return len(self.points) - 1

    def create_segments(self):
        self.segments = []

        for i in range(len(self.points) - 1):
            new_segment = MapSegment.MapSegment(self, self.globals, self.points[i], self.points[i+1])
            self.segments.append(new_segment)

    def draw_as_line(self, road_nodes=False):
        for i in self.segments:
            i.draw_as_line(road_nodes)


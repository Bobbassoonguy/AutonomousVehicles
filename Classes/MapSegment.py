import pygame


class MapSegment:
    def __init__(self, parent_MapRoad, globals, start_point, end_point, arc_radius=0):
        self.parent = parent_MapRoad
        self.globals = globals
        self.start_point = start_point
        self.end_point = end_point
        self.arc_radius = arc_radius

    def draw_as_line(self, endpoints=False):
        draw_color = (244, 134, 64)
        pygame.draw.aaline(self.globals.MAIN_SURFACE,draw_color,self.globals.point_to_pixels(self.start_point), self.globals.point_to_pixels(self.end_point))
        if endpoints:
            pygame.draw.circle(self.globals.MAIN_SURFACE, draw_color, self.globals.point_to_pixels(self.start_point), 3)
            pygame.draw.circle(self.globals.MAIN_SURFACE, draw_color, self.globals.point_to_pixels(self.end_point), 3)


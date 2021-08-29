import pygame
import math

class Shape:
    def __init__(self, parent, surface, points, color, line_width=4, fill=True, fill_color=None):
        self.parent = parent
        self.surface = surface
        self.points = points
        self.color = color
        self.line_width = line_width
        self.fill = fill
        self.fill_color = fill_color

    def get_centroid(self):
        num_points = len(self.points)
        x = 0
        y = 0
        for i in self.points:
            x += i[0]
            y += i[1]
        return [x/num_points, y/num_points]

    def rotate(self, angle, rotation_point="centroid"):
        angle = math.radians(angle)
        if rotation_point == "centroid":
            rotation_point = self.get_centroid()
        for i in self.points:
            x = i[0] - rotation_point[0]
            y = i[1] - rotation_point[1]
            i[0] = x * math.cos(angle) - y * math.sin(angle) + rotation_point[0]
            i[1] = x * math.sin(angle) + y * math.cos(angle) + rotation_point[1]

    def move(self, x_offset, y_offset):
        for i in self.points:
            i[0] += x_offset
            i[1] += y_offset

    def move_point_to_point(self, from_point, to_point):
        x_offset = to_point[0] - from_point[0]
        y_offset = to_point[1] - from_point[1]
        self.move(x_offset, y_offset)

    def draw(self):
        if self.fill:
            pygame.draw.polygon(self.surface, self.fill_color, self.points)
            pygame.draw.aalines(self.surface, self.color, True,  self.points)
        else:
            pygame.draw.aalines(self.surface, self.color, True, self.points)

import pygame

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

    def rotate(self, angle, rotation_center=None):
        #foo bar
        print("Hello")

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
            pygame.draw.polygon(self.surface, self.color, self.points, width=self.line_width)
        else:
            pygame.draw.polygon(self.surface, self.color, self.points, width=self.line_width)

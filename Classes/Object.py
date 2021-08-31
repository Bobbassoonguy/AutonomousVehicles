import pygame
import Shape
import Colors
import Vector

class Object:
    def __init__(self, parent, globals, points, line_color=Colors.GREEN_LINE, fill_color=Colors.GREEN_FILL):
        self.parent = parent
        self.globals = globals
        self.surface = self.globals.MAIN_SURFACE
        self.line_color = line_color
        self.fill_color = fill_color

        self.shape = Shape.Shape(self, self.globals, points, self.line_color, fill_color=self.fill_color)

        self.velocity = Vector.Vector(0, 0)  # a velocity vector in m/s
        self.acceleration = Vector.Vector(0, 0)  # an acceleration vector in m/s^2

    def draw(self, draw_velocity_vector=False, draw_acceleration_vector=False):
        self.shape.fill_color = self.fill_color
        self.shape.color = self.line_color
        self.shape.globals = self.globals
        self.shape.draw()

        if draw_velocity_vector:
            pygame.draw.line(self.globals.MAIN_SURFACE, (255, 0, 0), [self.position()[0] * self.globals.PIXELS_PER_METER, self.position()[1] * self.globals.PIXELS_PER_METER], [self.velocity.x * self.globals.PIXELS_PER_METER, self.velocity.y * self.globals.PIXELS_PER_METER],4)

    def position(self):
        return self.shape.get_centroid()

    def angle(self):
        return self.shape.angle

    def move(self, dx, dy):
        self.shape.move(dx, dy)

    def move_to(self, x, y):
        current = self.position()
        self.move(x-current[0], y-current[1])

    def rotate(self, angle, rotation_point):
        self.shape.rotate(angle, rotation_point)

    def rotate_to_angle(self, angle, rotation_point):
        self.rotate(angle - self.shape.angle, rotation_point)



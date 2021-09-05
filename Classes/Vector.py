import math
import pygame
import copy

class Vector:
    def __init__(self, x, y, unit_vector=False):
        self.x = x
        self.y = y
        self.unit_vector = unit_vector
        if self.unit_vector:
            self.set_magnitude(1)

    def __add__(self, a):
        if type(a) is Vector:
            new_vector = Vector(self.x + a.x, self.y + a.y)
        elif type(a) is list and len(a) == 2:
            new_vector = Vector(self.x + a[0], self.y + a[1])
        else:
            raise Exception("Can only add Vector or List to type: Vector")
        return new_vector

    def __iadd__(self, other):
        if type(other) is Vector:
            self.x += other.x
            self.y += other.y
        elif type(other) is list and len(other) == 2:
            self.x += other[0]
            self.y += other[1]
        else:
            raise Exception("Can only add Vector or List to type: Vector")
        return self

    def draw_starting_at(self, globals, point, color=(255, 0, 0)):
        point2 = self.list()
        point2[0] += point[0]
        point2[1] += point[1]
        pygame.draw.aaline(globals.VEHICLE_SURFACE,color,globals.point_to_pixels(point),globals.point_to_pixels(point2))

    def magnitude(self):
        if self.unit_vector:
            return 1
        return math.sqrt(self.x**2+self.y**2)

    def angle(self):  # returns angle from theta=0 (clockwise from +x axis)
        if self.x > 0:
            if self.y > 0:
                return math.degrees(math.atan(abs(self.y / self.x))) % 360
            elif self.y < 0:
                return 360 - (math.degrees(math.atan(abs(self.y / self.x))) % 360)
            else:
                return 0
        elif self.x < 0:
            if self.y > 0:
                return 180 - (math.degrees(math.atan(abs(self.y / self.x))) % 360)
            elif self.y < 0:
                return 180 + (math.degrees(math.atan(abs(self.y / self.x))) % 360)
            else:
                return 180
        else:
            if self.y > 0:
                return 90
            elif self.y < 0:
                return 270
            else:
                return 0

    def rotate(self, degrees):  # positive -> clockwise negative -> counter clockwise
        return self.rotate_to(degrees + self.angle())

    def rotate_to(self, degrees):  # rotates the vector to an angle from theta=0 (clockwise from +x axis)
        mag = self.magnitude()
        self.x = mag * math.cos(math.radians(degrees))
        self.y = mag * math.sin(math.radians(degrees))

    def scale(self, scale):  # scales vector by its magnitude
        if not self.unit_vector:
            self.x *= scale
            self.y *= scale

    def set_magnitude(self, magnitude):  # scales a vector such that it points in the same direction and has passed magnitude
        if self.unit_vector:
            x, y = self.x, self.y
            self.x *= 1 / math.sqrt(x ** 2 + y ** 2)
            self.y *= 1 / math.sqrt(x ** 2 + y ** 2)
        else:
            x, y = self.x, self.y
            self.x *= magnitude / math.sqrt(x ** 2 + y ** 2)
            self.y *= magnitude / math.sqrt(x ** 2 + y ** 2)

    def ROC_scale(self, ROC_vector, dt): # assuming ROC_vector is in units/dt change self according to passed ROC_vector (i.e.) change self(velocity vector) based on passed vector(acceleration vector) over time period dt(time interval)
        if not self.unit_vector:
            self.x += ROC_vector[0] * dt
            self.y += ROC_vector[1] * dt

    def list(self):
        return [self.x, self.y]


def get_Vector_between_points(start_point, end_point):
    return Vector(end_point[0]-start_point[0], end_point[1]-start_point[1])

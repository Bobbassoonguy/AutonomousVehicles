import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2)

    def angle(self):  # returns angle from theta=0 (clockwise from +x axis)
        return -math.degrees(math.atan(self.y/self.x)) % 360

    def rotate(self, degrees):  # positive -> clockwise negative -> counter clockwise
        return self.rotate_to(degrees+self.angle())

    def rotate_to(self, degrees):  # rotates the vector to an angle from theta=0 (clockwise from +x axis)
        self.x = math.cos(math.radians(degrees))
        self.y = -math.sin(math.radians(degrees))

    def scale(self, scale):  # scales vector by its magnitude
        self.x *= scale
        self.y *= scale

    def set_magnitude(self, magnitude):  # scales a vector such that it points in the same direction and has passed magnitude
        self.x *= magnitude / math.sqrt(self.x ** 2 + self.y ** 2)
        self.y *= magnitude / math.sqrt(self.x ** 2 + self.y ** 2)

    def ROC_scale(self, ROC_vector, dt): # assuming ROC_vector is in units/dt change self according to passed ROC_vector (i.e.) change self(velocity vector) based on passed vector(acceleration vector) over time period dt(time interval)
        self.x += ROC_vector[0] * dt
        self.y += ROC_vector[1] * dt

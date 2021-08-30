import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):

    def angle(self):  # returns angle from theta=0 (clockwise from +x axis)

    def rotate(self, degrees):  # positive -> clockwise negative -> counter clockwise

    def rotate_to(self, degrees): # rotates the vector to an angle from theta=0 (clockwise from +x axis)

    def scale(self, scale):  # scales vector by its magnitude

    def set_magnitude(self, magnitude):  # scales a vector such that it points in the same direction and has passed magnitude

    def ROC_scale(self, ROC_vector, dt): # assuming ROC_vector is in units/dt change self according to passed ROC_vector (i.e.) change self(velocity vector) based on passed vector(acceleration vector) over time period dt(time interval)


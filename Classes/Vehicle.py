import pygame
import Shape
import math

class Vehicle:
    def __init__(self, parent, x=3, y=4):
        self.parent = parent
        self.surface = self.parent.screen
        self.LENGTH = 4.5  # meters
        self.WIDTH = 1.8  # meters
        self.FRONT_AXLE_TO_FRONT = 1  # meters
        self.WHEELBASE = 2.7  # meters
        self.TRACK = 1.5  # meters
        self.MIN_TURN_RADIUS = 10.8  # meters
        self.PIXELS_PER_METER = self.parent.PIXELS_PER_METER

        self.x = x
        self.y = y

        self.create_outline()

        # TODO fix this because it shouldn't be based on the center of the car
        self.front_right_wheel = Wheel(self, True, self.x + (self.TRACK / 2),
                                       self.y - (self.WHEELBASE / 2))
        self.front_left_wheel = Wheel(self, True, self.x - (self.TRACK / 2),
                                       self.y - (self.WHEELBASE / 2))
        self.back_right_wheel = Wheel(self, True, self.x + (self.TRACK / 2),
                                       self.y + (self.WHEELBASE / 2))
        self.back_left_wheel = Wheel(self, True, self.x - (self.TRACK / 2),
                                       self.y + (self.WHEELBASE / 2))
        self.wheels = [self.front_right_wheel, self.front_left_wheel,self.back_left_wheel,self.back_right_wheel]

        print("New Car initialized")

    def create_outline(self):
        display_border_thickness = 0.05  # meters
        display_rectangle_round_corners = 1.5 * display_border_thickness
        self.outline = Shape.Shape(self, self.surface,
                                   [[(self.x - (self.WIDTH/2)) * self.PIXELS_PER_METER, (self.y - (self.LENGTH/2)) * self.PIXELS_PER_METER],
                                    [(self.x + (self.WIDTH/2)) * self.PIXELS_PER_METER, (self.y - (self.LENGTH/2)) * self.PIXELS_PER_METER],
                                    [(self.x + (self.WIDTH/2)) * self.PIXELS_PER_METER, (self.y + (self.LENGTH/2)) * self.PIXELS_PER_METER],
                                    [(self.x - (self.WIDTH/2)) * self.PIXELS_PER_METER, (self.y + (self.LENGTH/2)) * self.PIXELS_PER_METER]],
                                   (51, 204, 51), line_width=round(display_border_thickness * self.PIXELS_PER_METER),
                                   fill_color=(153, 255, 153))

    def draw(self):
        # TODO make this position/rotation dependant

        self.outline.draw()

        self.front_right_wheel.draw()
        self.front_left_wheel.draw()
        self.back_right_wheel.draw()
        self.back_left_wheel.draw()

    def turn(self, degrees):
        self.outline.rotate(math.radians(degrees))

        # foo bar




class Wheel:
    def __init__(self, parent, steering, x, y):
        self.parent = parent
        self.surface = self.parent.surface
        self.WIDTH = 0.18  # meters
        self.DIAMETER = 0.44  # meters
        self.STEERING = False
        self.PIXELS_PER_METER = self.parent.PIXELS_PER_METER

        self.x = x
        self.y = y

        self.create_outline()

        # TODO define position and rotation relative to parent vehicle

    def create_outline(self):
        display_border_thickness = 0.02  # meters
        self.outline = Shape.Shape(self.parent, self.surface,
                              [[(self.x - (self.WIDTH / 2)) * self.PIXELS_PER_METER,
                                (self.y - (self.DIAMETER / 2)) * self.PIXELS_PER_METER],
                               [(self.x + (self.WIDTH / 2)) * self.PIXELS_PER_METER,
                                (self.y - (self.DIAMETER / 2)) * self.PIXELS_PER_METER],
                               [(self.x + (self.WIDTH / 2)) * self.PIXELS_PER_METER,
                                (self.y + (self.DIAMETER / 2)) * self.PIXELS_PER_METER],
                               [(self.x - (self.WIDTH / 2)) * self.PIXELS_PER_METER,
                                (self.y + (self.DIAMETER / 2)) * self.PIXELS_PER_METER]],
                              (0, 153, 51), line_width=round(display_border_thickness * self.PIXELS_PER_METER),
                              fill_color=(0, 204, 0))

    def draw(self):
        self.outline.draw()
import pygame
import Shape
import math

class Vehicle:
    def __init__(self, parent, x=20, y=10):
        self.parent = parent
        self.surface = self.parent.screen
        self.LENGTH = 4.5  # meters
        self.WIDTH = 1.8  # meters
        self.FRONT_AXLE_TO_FRONT = 0.95  # meters
        self.WHEELBASE = 2.7  # meters
        self.TRACK = 1.5  # meters
        self.MIN_TURN_DIAMETER = 10.8  # meters
        self.PIXELS_PER_METER = self.parent.PIXELS_PER_METER

        self.angle = 0
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
        self.front_right_wheel.outline.fill_color = [255, 128, 128]
        self.front_left_wheel.outline.fill_color = [255, 128, 128]
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

    def rotate(self, degrees, rotation_point):
        self.angle += degrees
        self.angle %= 360
        self.outline.rotate(degrees, rotation_point)
        self.x, self.y = self.outline.get_centroid()
        for i in self.wheels:
            i.rotate(degrees, rotation_point)

    def turn(self, turn_radius, turn_degrees, right_turn=True, display_turn_circle=False):
        if turn_radius < self.MIN_TURN_DIAMETER/2:
            raise ValueError('Attempted a turn radius which was smaller than minimum')
        if right_turn:
            center = self.get_turn_circle_center(turn_radius, right_turn=True)
            self.rotate(turn_degrees, center)
            if self.front_left_wheel.angle == self.angle:
                self.front_left_wheel.rotate(math.degrees(math.asin(self.WHEELBASE/turn_radius)))
                self.front_right_wheel.rotate(math.degrees(math.asin(self.WHEELBASE/math.sqrt(
                    self.WHEELBASE**2+(-self.TRACK+math.sqrt(turn_radius**2-self.WHEELBASE**2))**2))))

        else:
            center = self.get_turn_circle_center(turn_radius, right_turn=False)
            self.rotate(-turn_degrees, center)
            if self.front_right_wheel.angle == self.angle:
                self.front_right_wheel.rotate(-math.degrees(math.asin(self.WHEELBASE / turn_radius)))
                self.front_left_wheel.rotate(-math.degrees(math.asin(self.WHEELBASE / math.sqrt(
                    self.WHEELBASE ** 2 + (-self.TRACK + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2)) ** 2))))

        if display_turn_circle:
            pygame.draw.circle(self.surface, [0, 0, 255], center, turn_radius * self.PIXELS_PER_METER, width=1)
            pygame.draw.circle(self.surface, [0, 0, 255], center, 3, width=3)



    def get_turn_circle_center(self, turn_radius, right_turn=True):
        turn_radius *= self.PIXELS_PER_METER
        if right_turn:
            back = self.back_left_wheel
            center = [back.x + math.sqrt(turn_radius**2-(self.WHEELBASE*self.PIXELS_PER_METER)**2) * math.cos(math.radians(self.angle)),
                      back.y + math.sqrt(turn_radius**2-(self.WHEELBASE*self.PIXELS_PER_METER)**2) * math.sin(math.radians(self.angle))]
        else:
            back = self.back_right_wheel
            center = [back.x - math.sqrt(turn_radius**2-(self.WHEELBASE*self.PIXELS_PER_METER)**2) * math.cos(math.radians(self.angle)),
                      back.y - math.sqrt(turn_radius**2-(self.WHEELBASE*self.PIXELS_PER_METER)**2) * math.sin(math.radians(self.angle))]
        return center




class Wheel:
    def __init__(self, parent, steering, x, y):
        self.parent = parent
        self.surface = self.parent.surface
        self.WIDTH = 0.18  # meters
        self.DIAMETER = 0.44  # meters
        self.STEERING = False
        self.PIXELS_PER_METER = self.parent.PIXELS_PER_METER

        self.angle = 0
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

    def move_to(self, x, y):
        self.outline.move_point_to_point(self.outline.get_centroid(), [x, y])
        self.x = x
        self.y = y

    def rotate(self, angle, rotation_point="centroid"):
        self.angle += angle
        self.angle %= 360
        if rotation_point == "centroid":
            rotation_point = self.outline.get_centroid()
        self.outline.rotate(angle, rotation_point)
        self.x = self.outline.get_centroid()[0]
        self.y = self.outline.get_centroid()[1]

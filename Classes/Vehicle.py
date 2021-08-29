import pygame
import Shape
import math

#this is a new change
class Vehicle:
    def __init__(self, parent, x=10, y=10):
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
        self.x = x  # meters
        self.y = y  # meters
        self.current_turn_radius = 0  # <0 left turn, >0 right turn, ==0 straight
        self.speed = 0  # current speed in m/s
        self.acceleration = 0  # current acceleration in m/s^2

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

    def move(self, dx, dy): #  moves car relative to current location. dx, dy in meters
        self.x = self.x + dx
        self.y = self.y + dy
        self.outline.move(dx*self.PIXELS_PER_METER, dy*self.PIXELS_PER_METER)
        for i in self.wheels:
            i.move(dx, dy)

    def move_to(self, x, y):  # moves car to these absolute coordinates (meters)
        self.move(x-self.x,y-self.y)

    def rotate(self, degrees, rotation_point="centroid"):
        self.angle += degrees
        self.angle %= 360
        if rotation_point != "centroid":
            rotation_point = [rotation_point[0]*self.PIXELS_PER_METER, rotation_point[1]*self.PIXELS_PER_METER]
        self.outline.rotate(degrees, rotation_point=rotation_point)
        self.x, self.y = [self.outline.get_centroid()[0]/self.PIXELS_PER_METER, self.outline.get_centroid()[1]/self.PIXELS_PER_METER]
        if rotation_point == "centroid":
            rotation_point = [self.outline.get_centroid()[0]/self.PIXELS_PER_METER, self.outline.get_centroid()[1]/self.PIXELS_PER_METER]
        else:
            rotation_point = [rotation_point[0]/self.PIXELS_PER_METER, rotation_point[1]/self.PIXELS_PER_METER]
        for i in self.wheels:
            i.rotate(degrees, rotation_point=rotation_point)

    def rotate_to_angle(self, angle, rotation_point="centroid"):
        self.rotate(angle-self.angle, rotation_point)

    def turn(self, turn_radius, turn_degrees, right_turn=True, display_turn_circle=False):
        if turn_radius < self.MIN_TURN_DIAMETER/2:
            raise ValueError('Attempted a turn radius which was smaller than minimum')
        if right_turn:
            center = self.get_turn_circle_center(turn_radius, right_turn=True)
            self.rotate(turn_degrees, center)

            if self.front_left_wheel.angle != self.angle + math.degrees(math.asin(self.WHEELBASE/turn_radius)):
                self.front_left_wheel.rotate_to_angle(self.angle + math.degrees(math.asin(self.WHEELBASE/turn_radius)))
                self.front_right_wheel.rotate_to_angle(self.angle + math.degrees(math.asin(self.WHEELBASE/math.sqrt(
                    self.WHEELBASE**2+(-self.TRACK+math.sqrt(turn_radius**2-self.WHEELBASE**2))**2))))

        else:
            center = self.get_turn_circle_center(turn_radius, right_turn=False)
            self.rotate(-turn_degrees, center)
            if self.front_right_wheel.angle != self.angle - math.degrees(math.asin(self.WHEELBASE/turn_radius)):
                self.front_right_wheel.rotate_to_angle(self.angle-math.degrees(math.asin(self.WHEELBASE / turn_radius)))
                self.front_left_wheel.rotate_to_angle(self.angle-math.degrees(math.asin(self.WHEELBASE / math.sqrt(
                    self.WHEELBASE ** 2 + (-self.TRACK + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2)) ** 2))))

        if display_turn_circle:
            pygame.draw.circle(self.surface, [0, 0, 255], [center[0]*self.PIXELS_PER_METER, center[1]*self.PIXELS_PER_METER], turn_radius * self.PIXELS_PER_METER, width=1)
            pygame.draw.circle(self.surface, [0, 0, 255], [center[0]*self.PIXELS_PER_METER, center[1]*self.PIXELS_PER_METER], 3, width=3)

    def get_turn_circle_center(self, turn_radius, right_turn=True):
        if right_turn:
            back = self.back_left_wheel
            center = [back.x + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.cos(math.radians(self.angle)),
                      back.y + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.sin(math.radians(self.angle))]
        else:
            back = self.back_right_wheel
            center = [back.x - math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.cos(math.radians(self.angle)),
                      back.y - math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.sin(math.radians(self.angle))]
        return center

    def go(self, delta_time):  # moves the car according to current_turn_radius to place it would be after
        # delta_time. (Usually pass 1/FPS as delta_time)
        distance = self.speed * delta_time + 0.5 * self.acceleration * delta_time ** 2
        self.speed = self.speed + self.acceleration * delta_time
        if self.current_turn_radius < 0:  # Left turn
            self.turn(self.current_turn_radius, math.degrees(distance/self.current_turn_radius), right_turn=False, display_turn_circle=True)
        elif self.current_turn_radius > 0:  # Right turn
            self.turn(self.current_turn_radius, math.degrees(distance / self.current_turn_radius), right_turn=True, display_turn_circle=True)
        else:
            self.move(distance*math.cos(math.radians(self.angle-90)), distance*math.sin(math.radians(self.angle-90)))



class Wheel:
    def __init__(self, parent, steering, x, y):
        self.parent = parent
        self.surface = self.parent.surface
        self.WIDTH = 0.18  # meters
        self.DIAMETER = 0.44  # meters
        self.STEERING = False
        self.PIXELS_PER_METER = self.parent.PIXELS_PER_METER

        self.angle = 0  # degrees
        self.x = x  # meters
        self.y = y  # meters

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

    def move(self, dx, dy): # meters
        self.outline.move(dx * self.PIXELS_PER_METER, dy * self.PIXELS_PER_METER)
        self.x = self.x + dx
        self.y = self.y + dy

    def move_to(self, x, y):
        self.move(x-self.x, y-self.y)

    def rotate(self, angle, rotation_point="centroid"):
        self.angle += angle
        self.angle %= 360
        if rotation_point != "centroid":
            rotation_point = [rotation_point[0] * self.PIXELS_PER_METER, rotation_point[1] * self.PIXELS_PER_METER]
        self.outline.rotate(angle, rotation_point)
        self.x = self.outline.get_centroid()[0] / self.PIXELS_PER_METER
        self.y = self.outline.get_centroid()[1] / self.PIXELS_PER_METER

    def rotate_to_angle(self, angle, rotation_point="centroid"):
        self.rotate(angle-self.angle, rotation_point)
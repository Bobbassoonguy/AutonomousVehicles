import pygame

import Colors
import Shape
import math
import Object


class Vehicle:
    def __init__(self, parent, globals, x, y, fill_color, outline_color):
        self.parent = parent
        self.globals = globals
        self.surface = self.globals.MAIN_SURFACE

        # CAR PARAMETERS
        self.LENGTH = 4.5  # meters
        self.WIDTH = 1.8  # meters
        self.FRONT_AXLE_TO_FRONT = 0.95  # meters
        self.WHEELBASE = 2.7  # meters
        self.TRACK = 1.5  # meters
        self.TIRE_WIDTH = 0.18  # meters
        self.TIRE_DIAMETER = 0.44  # meters

        self.MIN_TURN_DIAMETER = 10.8  # meters
        self.MAX_SPEED = 50  # m/s
        self.MIN_SPEED = 0  # m/s eventually will be -9
        self.MAX_ACCELERATION = 3.5  # m/s/s
        self.MIN_ACCELERATION = -9.5  # m/s/s

        # VEHICLE DISPLAY PARAMETERS
        self.FILL_COLOR = fill_color
        self.OUTLINE_COLOR = outline_color

        # CAR VARIABLES
        self.current_turn_radius = 0  # <0 left turn, >0 right turn, ==0 straight

        self.body = Object.Object(self, self.globals,
                                  [[(x - (self.LENGTH / 2)), (y - (self.WIDTH / 2))],
                                   [(x + (self.LENGTH / 2)), (y - (self.WIDTH / 2))],
                                   [(x + (self.LENGTH / 2)), (y + (self.WIDTH / 2))],
                                   [(x - (self.LENGTH / 2)), (y + (self.WIDTH / 2))]],
                                  line_color=self.OUTLINE_COLOR, fill_color=self.FILL_COLOR)

        self.front_right_wheel = Object.Object(self, self.globals,
                                               [[x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT + (
                                                       self.TIRE_DIAMETER / 2),
                                                 y + (self.TRACK / 2) + (self.TIRE_WIDTH / 2)],
                                                [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT + (
                                                        self.TIRE_DIAMETER / 2),
                                                 y + (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                                [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - (
                                                        self.TIRE_DIAMETER / 2),
                                                 y + (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                                [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - (
                                                        self.TIRE_DIAMETER / 2),
                                                 y + (self.TRACK / 2) + (self.TIRE_WIDTH / 2)]],
                                               line_color=self.OUTLINE_COLOR, fill_color=self.OUTLINE_COLOR)

        self.front_left_wheel = Object.Object(self, self.globals,
                                              [[x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT + (
                                                      self.TIRE_DIAMETER / 2),
                                                y - (self.TRACK / 2) + (self.TIRE_WIDTH / 2)],
                                               [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT + (
                                                       self.TIRE_DIAMETER / 2),
                                                y - (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                               [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - (
                                                       self.TIRE_DIAMETER / 2),
                                                y - (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                               [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - (
                                                       self.TIRE_DIAMETER / 2),
                                                y - (self.TRACK / 2) + (self.TIRE_WIDTH / 2)]],
                                              line_color=self.OUTLINE_COLOR, fill_color=self.OUTLINE_COLOR)

        self.back_right_wheel = Object.Object(self, self.globals,
                                              [[x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE + (
                                                      self.TIRE_DIAMETER / 2),
                                                y + (self.TRACK / 2) + (self.TIRE_WIDTH / 2)],
                                               [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE + (
                                                       self.TIRE_DIAMETER / 2),
                                                y + (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                               [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE - (
                                                       self.TIRE_DIAMETER / 2),
                                                y + (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                               [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE - (
                                                       self.TIRE_DIAMETER / 2),
                                                y + (self.TRACK / 2) + (self.TIRE_WIDTH / 2)]],
                                              line_color=self.OUTLINE_COLOR, fill_color=self.FILL_COLOR)

        self.back_left_wheel = Object.Object(self, self.globals,
                                             [[x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE + (
                                                     self.TIRE_DIAMETER / 2),
                                               y - (self.TRACK / 2) + (self.TIRE_WIDTH / 2)],
                                              [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE + (
                                                      self.TIRE_DIAMETER / 2),
                                               y - (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                              [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE - (
                                                      self.TIRE_DIAMETER / 2),
                                               y - (self.TRACK / 2) - (self.TIRE_WIDTH / 2)],
                                              [x + (self.LENGTH / 2) - self.FRONT_AXLE_TO_FRONT - self.WHEELBASE - (
                                                      self.TIRE_DIAMETER / 2),
                                               y - (self.TRACK / 2) + (self.TIRE_WIDTH / 2)]],
                                             line_color=self.OUTLINE_COLOR, fill_color=self.FILL_COLOR)

        self.wheels = [self.front_right_wheel, self.front_left_wheel, self.back_left_wheel, self.back_right_wheel]

        print("New Car initialized")

    def draw(self):
        self.body.draw(draw_velocity_vector=True, draw_acceleration_vector=True)

        self.front_right_wheel.draw()
        self.front_left_wheel.draw()
        self.back_right_wheel.draw()
        self.back_left_wheel.draw()

    def turn(self, turn_radius, turn_degrees, right_turn=True, display_turn_circle=False):
        if turn_radius < self.MIN_TURN_DIAMETER / 2:
            raise ValueError('Attempted a turn radius which was smaller than minimum')
        if right_turn:
            center = self.get_turn_circle_center(turn_radius, right_turn=True)
            self.rotate(turn_degrees, center)
            if self.front_left_wheel.angle() != self.body.angle() + math.degrees(
                    math.asin(self.WHEELBASE / turn_radius)):
                self.front_left_wheel.rotate_to_angle(
                    self.body.angle() + math.degrees(math.asin(self.WHEELBASE / turn_radius)),
                    self.front_left_wheel.position())
                self.front_right_wheel.rotate_to_angle(
                    self.body.angle() + math.degrees(math.asin(self.WHEELBASE / math.sqrt(
                        self.WHEELBASE ** 2 + (-self.TRACK + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2)) ** 2))),
                    self.front_right_wheel.position())

        else:
            center = self.get_turn_circle_center(turn_radius, right_turn=False)
            self.rotate(-turn_degrees, center)
            if self.front_right_wheel.angle() != self.body.angle() - math.degrees(
                    math.asin(self.WHEELBASE / turn_radius)):
                self.front_right_wheel.rotate_to_angle(
                    self.body.angle() - math.degrees(math.asin(self.WHEELBASE / turn_radius)),
                    self.front_right_wheel.position())
                self.front_left_wheel.rotate_to_angle(
                    self.body.angle() - math.degrees(math.asin(self.WHEELBASE / math.sqrt(
                        self.WHEELBASE ** 2 + (-self.TRACK + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2)) ** 2))),
                    self.front_left_wheel.position())

        if display_turn_circle:
            pygame.draw.circle(self.surface, [0, 0, 255],
                               [center[0] * self.globals.PIXELS_PER_METER, center[1] * self.globals.PIXELS_PER_METER],
                               turn_radius * self.globals.PIXELS_PER_METER, width=1)
            pygame.draw.circle(self.surface, [0, 0, 255],
                               [center[0] * self.globals.PIXELS_PER_METER, center[1] * self.globals.PIXELS_PER_METER],
                               3, width=3)

    def rotate(self, turn_degrees, rotation_point):
        self.body.rotate(turn_degrees, rotation_point)
        for i in self.wheels:
            i.rotate(turn_degrees, rotation_point)
        self.body.velocity.rotate_to(self.body.angle())
        self.body.acceleration.rotate_to(self.body.angle())

    def get_turn_circle_center(self, turn_radius, right_turn=True):
        if right_turn:
            back = self.back_left_wheel.position()
            center = [
                back[0] - math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.sin(math.radians(self.body.angle())),
                back[1] + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.cos(math.radians(self.body.angle()))]
        else:
            back = self.back_right_wheel.position()
            center = [
                back[0] + math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.sin(math.radians(self.body.angle())),
                back[1] - math.sqrt(turn_radius ** 2 - self.WHEELBASE ** 2) * math.cos(math.radians(self.body.angle()))]
        return center

    def go(self, delta_time):  # moves the car according to current_turn_radius to place it would be after
        # delta_time. (Usually pass 1/FPS as delta_time)
        if self.body.acceleration.magnitude() < self.MIN_ACCELERATION:
            self.body.acceleration.set_magnitude(self.MIN_ACCELERATION)
        if self.body.acceleration.magnitude() > self.MAX_ACCELERATION:
            self.body.acceleration.set_magnitude(self.MAX_ACCELERATION)
        if self.body.velocity.magnitude() > self.MAX_SPEED:
            self.body.velocity.set_magnitude(self.MAX_SPEED)
        if self.body.velocity.magnitude() < self.MIN_SPEED:
            self.body.velocity.set_magnitude(self.MIN_SPEED)
        if self.body.velocity.magnitude() + self.body.acceleration.magnitude() * delta_time > self.MAX_SPEED:
            self.body.acceleration.set_magnitude(
                (self.MAX_SPEED - self.body.velocity.magnitude()) / delta_time)
        if self.body.velocity.magnitude() + self.body.acceleration.magnitude() * delta_time < self.MIN_SPEED:
            self.body.acceleration.set_magnitude(
                (self.MIN_SPEED - self.body.velocity.magnitude()) / delta_time)
        distance = self.body.velocity.magnitude() * delta_time + 0.5 * self.body.acceleration.magnitude() * delta_time ** 2
        self.body.velocity.set_magnitude(self.body.velocity.magnitude() + self.body.acceleration.magnitude() * delta_time)

        if self.current_turn_radius < 0:  # Left turn
            self.turn(abs(self.current_turn_radius), math.degrees(distance / abs(self.current_turn_radius)), right_turn=False,
                      display_turn_circle=True)
        elif self.current_turn_radius > 0:  # Right turn
            self.turn(abs(self.current_turn_radius), math.degrees(distance / abs(self.current_turn_radius)), right_turn=True,
                      display_turn_circle=True)
        else:
            self.body.move(-distance * math.sin(math.radians(self.body.angle() - 90)), distance * math.cos(math.radians(self.body.angle() - 90)))
            for i in self.wheels:
                i.move(-distance * math.sin(math.radians(self.body.angle() - 90)), distance * math.cos(math.radians(self.body.angle() - 90)))

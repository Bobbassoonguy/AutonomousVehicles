import pygame

class Vehicle:
    def __init__(self, parent):
        self.parent = parent
        self.surface = self.parent.screen
        self.LENGTH = 4.5  # meters
        self.WIDTH = 1.8  # meters
        self.FRONT_AXLE_TO_FRONT = 1  # meters
        self.WHEELBASE = 2.7  # meters
        self.TRACK = 1.5  # meters
        self.MIN_TURN_RADIUS = 10.8  # meters

        self.x = 150
        self.y = 250

        # TODO fix this because it shouldn't be based on the center of the car
        self.front_right_wheel = Wheel(self, False,
                                       (self.x + (self.TRACK * self.parent.PIXELS_PER_METER / 2)),
                                       (self.y - (self.WHEELBASE * self.parent.PIXELS_PER_METER / 2)))
        self.front_left_wheel = Wheel(self, False,
                                      (self.x - (self.TRACK * self.parent.PIXELS_PER_METER / 2)),
                                      (self.y - (self.WHEELBASE * self.parent.PIXELS_PER_METER / 2)))
        self.back_right_wheel = Wheel(self, False,
                                      (self.x + (self.TRACK * self.parent.PIXELS_PER_METER / 2)),
                                      (self.y + (self.WHEELBASE * self.parent.PIXELS_PER_METER / 2)))
        self.back_left_wheel = Wheel(self, False,
                                     (self.x - (self.TRACK * self.parent.PIXELS_PER_METER / 2)),
                                     (self.y + (self.WHEELBASE * self.parent.PIXELS_PER_METER / 2)))

        print("New Car initialized")

    def draw(self):
        # TODO make this position/rotation dependant
        display_border_thickness = 0.05  # meters
        display_rectangle_round_corners = 1.5 * display_border_thickness

        outline = pygame.Rect(self.x-(self.WIDTH * self.parent.PIXELS_PER_METER / 2), self.y-(self.LENGTH * self.parent.PIXELS_PER_METER / 2), self.WIDTH * self.parent.PIXELS_PER_METER, self.LENGTH * self.parent.PIXELS_PER_METER)
        pygame.draw.rect(self.surface, (153, 255, 153), outline, border_radius=round(display_rectangle_round_corners * self.parent.PIXELS_PER_METER))
        pygame.draw.rect(self.surface, (51, 204, 51), outline, width=round(display_border_thickness * self.parent.PIXELS_PER_METER), border_radius=round(display_rectangle_round_corners * self.parent.PIXELS_PER_METER))

        self.front_right_wheel.draw()
        self.front_left_wheel.draw()
        self.back_right_wheel.draw()
        self.back_left_wheel.draw()

        # foo bar




class Wheel:
    def __init__(self, parent, steering, x, y):
        self.parent = parent
        self.display_screen = self.parent.surface
        self.WIDTH = 0.18  # meters
        self.DIAMETER = 0.44  # meters
        self.STEERING = False

        self.x = x
        self.y = y

        # TODO define position and rotation relative to parent vehicle

    def draw(self):
        display_border_thickness = 0.02  # meters
        display_rectangle_round_corners = 1.5 * display_border_thickness

        outline = pygame.Rect(self.x - (self.WIDTH * self.parent.parent.PIXELS_PER_METER / 2),
                              self.y - (self.DIAMETER * self.parent.parent.PIXELS_PER_METER / 2),
                              self.WIDTH * self.parent.parent.PIXELS_PER_METER, self.DIAMETER * self.parent.parent.PIXELS_PER_METER)
        pygame.draw.rect(self.display_screen, (0, 204, 0), outline,
                         border_radius=round(display_rectangle_round_corners * self.parent.parent.PIXELS_PER_METER))
        pygame.draw.rect(self.display_screen, (0, 153, 51), outline,
                         width=round(display_border_thickness * self.parent.parent.PIXELS_PER_METER),
                         border_radius=round(display_rectangle_round_corners * self.parent.parent.PIXELS_PER_METER))

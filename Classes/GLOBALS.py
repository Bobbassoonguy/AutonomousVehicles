import pygame


class Globals:
    def __init__(self):
        self.PIXELS_PER_METER = 20
        self.CANVAS_SIZE_X = 1000
        self.CANVAS_SIZE_y = 1000
        self.ROAD_MIN_CURVE_RAD = 10
        self.FPS = 60
        self.MAIN_SURFACE = pygame.display.set_mode([self.CANVAS_SIZE_X, self.CANVAS_SIZE_y])

    def point_to_pixels(self, point):
        return [point[0] * self.PIXELS_PER_METER, point[1] * self.PIXELS_PER_METER]

    def pixels(self, val):
        return val * self.PIXELS_PER_METER

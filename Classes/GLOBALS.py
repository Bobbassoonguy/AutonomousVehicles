import pygame


class Globals:
    def __init__(self, disp_x=200, disp_y=200, pix=5):
        self.PIXELS_PER_METER = pix
        self.CANVAS_SIZE_X = disp_x
        self.CANVAS_SIZE_y = disp_y
        self.ROAD_MIN_CURVE_RAD = pix
        self.FPS = 60
        self.MAIN_SURFACE = pygame.display.set_mode([self.pixels(self.CANVAS_SIZE_X), self.pixels(self.CANVAS_SIZE_y)])

    def point_to_pixels(self, point):
        return [point[0] * self.PIXELS_PER_METER, point[1] * self.PIXELS_PER_METER]

    def pixels(self, val):
        return val * self.PIXELS_PER_METER

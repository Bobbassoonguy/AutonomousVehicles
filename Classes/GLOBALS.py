import pygame


class Globals:
    def __init__(self):
        self.PIXELS_PER_METER = 20
        self.CANVAS_SIZE_X = 1000
        self.CANVAS_SIZE_y = 1000
        self.ROAD_MIN_CURVE_RAD = 10
        self.FPS = 60
        self.MAIN_SURFACE = pygame.display.set_mode([self.CANVAS_SIZE_X, self.CANVAS_SIZE_y])
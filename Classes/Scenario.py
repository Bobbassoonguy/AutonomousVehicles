import pygame

class Scenario:
    def __init__(self, name):
        #GLOBAL VARIABLES
        self.CANVAS_SIZE_X = 1000
        self.CANVAS_SIZE_y = 1000
        self.PIXELS_PER_METER = 10
        self.ROAD_MIN_CURVE_RAD = 10
        self.FPS = 60

        self.name = name

        self.screen = pygame.display.set_mode([self.CANVAS_SIZE_X, self.CANVAS_SIZE_y])
        pygame.display.set_caption(self.name)

    def main(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()
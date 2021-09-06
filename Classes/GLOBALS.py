import pygame
import Vector
import math
import Colors


class Globals:
    def __init__(self, disp_x=200, disp_y=200, pix=5):
        self.PIXELS_PER_METER = pix
        self.CANVAS_SIZE_X = disp_x
        self.CANVAS_SIZE_y = disp_y
        self.GUI_WIDTH = 300
        self.ROAD_MIN_CURVE_RAD = pix
        self.FPS = 60
        self.BACKGROUND = pygame.display.set_mode([self.pixels(self.CANVAS_SIZE_X)+self.GUI_WIDTH, self.pixels(self.CANVAS_SIZE_y)])
        self.BACKDROP = pygame.Surface((self.pixels(self.CANVAS_SIZE_X) + self.GUI_WIDTH, self.pixels(self.CANVAS_SIZE_y)), pygame.SRCALPHA, 32)
        self.BACKDROP = self.BACKDROP.convert_alpha()
        #self.GUI_SURFACE = pygame.Surface((self.pixels(self.CANVAS_SIZE_X), self.pixels(self.CANVAS_SIZE_y)))
        self.ROAD_SURFACE = pygame.Surface((self.pixels(self.CANVAS_SIZE_X), self.pixels(self.CANVAS_SIZE_y)),pygame.SRCALPHA, 32)
        self.ROAD_SURFACE = self.ROAD_SURFACE.convert_alpha()
        self.VEHICLE_SURFACE = pygame.Surface((self.pixels(self.CANVAS_SIZE_X), self.pixels(self.CANVAS_SIZE_y)),pygame.SRCALPHA, 32)
        self.VEHICLE_SURFACE = self.VEHICLE_SURFACE.convert_alpha()

    def point_to_pixels(self, point):
        return [point[0] * self.PIXELS_PER_METER, point[1] * self.PIXELS_PER_METER]

    def pixels(self, val):
        return val * self.PIXELS_PER_METER

    def draw_arc(self, surface, color, start_point, end_point, arc_radius, width):
        points_vector1 = Vector.get_Vector_between_points(start_point, end_point)
        points_vector2 = Vector.get_Vector_between_points(start_point, end_point)

        center_point = [(start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2]
        dist_to_center_point = math.sqrt(
            ((end_point[0] - start_point[0]) ** 2) + ((end_point[1] - start_point[1]) ** 2)) / 2
        if arc_radius < dist_to_center_point:
            raise ValueError('Tried to generate an arc with a radius smaller than 1/2 the distance between the points.')
        points_vector1.rotate(90)
        points_vector2.rotate(-90)

        points_vector1.set_magnitude(math.sqrt((arc_radius ** 2) - (dist_to_center_point ** 2)))
        points_vector2.set_magnitude(math.sqrt((arc_radius ** 2) - (dist_to_center_point ** 2)))

        points_vector1 += center_point
        points_vector2 += center_point

        center_1 = points_vector1.list()
        center_1_to_start_v = Vector.get_Vector_between_points(center_1, start_point)
        center_1_to_end_v = Vector.get_Vector_between_points(center_1, end_point)
        center_1_to_start = math.radians(center_1_to_start_v.angle())
        center_1_to_end = math.radians(center_1_to_end_v.angle())

        center_2 = points_vector2.list()
        center_2_to_start_v = Vector.get_Vector_between_points(center_2, start_point)
        center_2_to_end_v = Vector.get_Vector_between_points(center_2, end_point)
        center_2_to_end_v.draw_starting_at(self, center_2)
        center_2_to_start = math.radians(center_2_to_start_v.angle())
        center_2_to_start_v.draw_starting_at(self, center_2, color=(255, 255, 0))
        center_2_to_end = math.radians(center_2_to_end_v.angle())

        pygame.draw.circle(self.VEHICLE_SURFACE, Colors.CAR_BLUE_LINE, self.point_to_pixels(points_vector1.list()),
                           self.pixels(arc_radius), 1)
        pygame.draw.circle(self.VEHICLE_SURFACE, Colors.CAR_BLUE_LINE, self.point_to_pixels(points_vector2.list()),
                           self.pixels(arc_radius), 1)
        pygame.draw.circle(self.VEHICLE_SURFACE, Colors.CAR_ORANGE_LINE, self.point_to_pixels(start_point), 3)
        pygame.draw.circle(self.VEHICLE_SURFACE, Colors.CAR_ORANGE_LINE, self.point_to_pixels(end_point), 3)

        if center_1_to_start-center_1_to_end <= math.pi:
            pygame.draw.arc(surface, color, (
                self.pixels(center_1[0] - arc_radius), self.pixels(center_1[1] - arc_radius),
                2 * self.pixels(arc_radius), 2 * self.pixels(arc_radius)),
                            -center_1_to_start, -center_1_to_end, width)
        else:
            pygame.draw.arc(surface, color, (
                self.pixels(center_1[0] - arc_radius), self.pixels(center_1[1] - arc_radius),
                2 * self.pixels(arc_radius), 2 * self.pixels(arc_radius)),
                            -center_1_to_end, -center_1_to_start, width)

        if center_2_to_start-center_2_to_end <= math.pi:
            pygame.draw.arc(surface, color, (
                self.pixels(center_2[0] - arc_radius), self.pixels(center_2[1] - arc_radius),
                2 * self.pixels(arc_radius),
                2 * self.pixels(arc_radius)),
                            -center_2_to_start, -center_2_to_end, width)
        else:
            pygame.draw.arc(surface, color, (
                self.pixels(center_2[0] - arc_radius), self.pixels(center_2[1] - arc_radius),
                2 * self.pixels(arc_radius),
                2 * self.pixels(arc_radius)),
                            -center_2_to_end, -center_2_to_start, width)

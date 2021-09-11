import math
import GLOBALS
import pygame
import Vector
import Colors


def draw_arc(globals, surface, start_point, end_point, radius, width, color):
    points = get_arc_points(globals, start_point, end_point, radius, width)

    for i in points:
        print("Before: ", i)
        i = globals.point_to_pixels(i)
        print("After: ", i)
        pygame.draw.circle(surface,color,i,3)


    # pygame.draw.polygon(surface, color, points, 0)


def get_arc_points(globals, start_point, end_point, radius, width):
    # Note: if radius is positive, the turn is a "right turn" from the start_point
    # Note: all values are in meters, but it shouldnt matter mathematically.
    # Note: round numbers to 5 decimal places?
    # f0 = globals.PIXELS_PER_METER*0.25  # 0.25 meters
    f0 = 5
    points_vector1 = Vector.get_Vector_between_points(start_point, end_point)
    points_vector2 = Vector.get_Vector_between_points(start_point, end_point)

    center_point = [(start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2]
    dist_to_center_point = math.sqrt(
        ((end_point[0] - start_point[0]) ** 2) + ((end_point[1] - start_point[1]) ** 2)) / 2
    if abs(radius) < dist_to_center_point:
        raise ValueError('Tried to generate an arc with a radius smaller than 1/2 the distance between the points.')
    points_vector1.rotate(90)
    points_vector2.rotate(-90)

    points_vector1.set_magnitude(math.sqrt((radius ** 2) - (dist_to_center_point ** 2)))
    points_vector2.set_magnitude(math.sqrt((radius ** 2) - (dist_to_center_point ** 2)))

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
    center_2_to_start = math.radians(center_2_to_start_v.angle())
    center_2_to_end = math.radians(center_2_to_end_v.angle())

    center_to_end = center_2_to_end
    center_to_start = center_2_to_start
    center_to_start_v = center_2_to_start_v
    center_to_end_v = center_2_to_end_v
    center = center_2
    if radius > 0:
        center_to_end = center_1_to_end
        center_to_start = center_1_to_start
        center_to_start_v = center_1_to_start_v
        center_to_end_v = center_1_to_end_v
        center = center_1

    phi = center_to_end-center_to_start
    theta_0 = 2*math.asin(f0/(2*radius))
    n = math.ceil(phi/theta_0)
    theta = phi/n
    f = 2*radius*math.sin(theta/2)

    points = []
    points.append(center_to_start_v)
    print("center to start v: ",center_to_start_v.list())
    print("center: ", center)
    current_point = center_2_to_start_v
    print("N: ", n)
    for i in range(1,n):
        current_point.rotate(math.degrees(theta))
        points.append(current_point.copy())
    points.append(center_to_end_v)
    for i in range (n,-1,-1):
        points.append(points[i].scale((radius-width)/radius))
    actual_points = []
    for i in points:
        add_list = i.list()
        add_list[0] += center[0]
        add_list[1] += center[1]
        actual_points.append(add_list)

    return actual_points

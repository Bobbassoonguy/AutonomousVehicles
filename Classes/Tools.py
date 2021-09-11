import math
import GLOBALS
import pygame
import Vector
import Colors


def draw_dashed_line(globals, surface, start_point, end_point, width, color, dash_length=3.05):
    pix_width = round(globals.pixels(width))
    l = dash_length
    d = math.sqrt((end_point[0]-start_point[0])**2 + (end_point[1]-start_point[1])**2)
    n = math.floor(d/(2*l))
    v = Vector.Vector((end_point[0]-start_point[0]),(end_point[1]-start_point[1]))
    v.set_magnitude(l)
    current_point = start_point[:]
    for i in range(n):
        pygame.draw.line(surface,color,globals.point_to_pixels(current_point),globals.point_to_pixels((v.copy()+current_point).list()),width=pix_width)
        current_point = (v.copy()+v.copy()+current_point).list()

    if (2*n+1)*l >= d:
        pygame.draw.line(surface, color, globals.point_to_pixels(current_point),
                         globals.point_to_pixels(end_point), width=pix_width)
    else:
        pygame.draw.line(surface, color, globals.point_to_pixels(current_point),
                         globals.point_to_pixels((v.copy() + current_point).list()), width=pix_width)




def draw_double_line(globals, surface, start_point, end_point, width, color): # Width in meters
    v = Vector.Vector((end_point[0]-start_point[0]),(end_point[1]-start_point[1]))
    v1 = v.copy()
    v1.rotate(90)
    v2 = v.copy()
    v2.rotate(270)
    v1.set_magnitude(2*width)
    v2.set_magnitude(2*width)
    pygame.draw.line(surface,color,globals.point_to_pixels((v2.copy()+start_point).list()),globals.point_to_pixels((v2.copy()+end_point).list()),width=round(globals.pixels(width)))
    pygame.draw.line(surface, color, globals.point_to_pixels((v1.copy()+start_point).list()), globals.point_to_pixels((v1.copy()+end_point).list()), width=round(globals.pixels(width)))


def draw_arc(globals, surface, start_point, end_point, radius, width, color, inside=True):
    points = get_arc_points(globals, start_point, end_point, radius, width, inside)
    pixel_points = []
    for i in points:
        pixel_points.append(globals.point_to_pixels(i))
        # pygame.draw.circle(surface,color,globals.point_to_pixels(i),3)

    pygame.draw.polygon(surface, color, pixel_points, 0)
    # pygame.draw.circle(surface, Colors.CAR_GREEN_LINE, globals.point_to_pixels(start_point), 7, width=1)
    # pygame.draw.circle(surface, Colors.CAR_RED_LINE, globals.point_to_pixels(end_point), 7, width=1)



def get_arc_points(globals, start_point, end_point, radius, width, inside=True):
    # Note: if radius is positive, the turn is a clockwise turn from the start_point
    # Note: all values are in meters, but it shouldnt matter mathematically.
    # Note: round numbers to 5 decimal places?
    f0 = 20/(globals.PIXELS_PER_METER)  # 0.25 meters
    # f0 = 2
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
    if radius < 0:
        center_to_end = center_1_to_end
        center_to_start = center_1_to_start
        center_to_start_v = center_1_to_start_v
        center_to_end_v = center_1_to_end_v
        center = center_1

    phi = (center_to_end-center_to_start) % (2 * math.pi)
    if phi > math.pi:
        phi -= 2*math.pi
    theta_0 = 2*math.asin(f0/(2*radius))
    n = math.ceil(abs(phi)/abs(theta_0))
    theta = phi/n
    f = 2*radius*math.sin(theta/2)

    # print("center to start v: ",center_to_start_v.list())
    # print("center: ", center)
    # print("Starting angle: ", center_to_start_v.angle())
    # print("Ending angle: ", center_to_end_v.angle())
    # print("N: ", n)
    # print("phi: ", math.degrees(phi))
    # print("theta: ", math.degrees(theta))
    points = []
    points.append(center_to_start_v)
    current_point = center_to_start_v.copy()
    for i in range(1,n):
        current_point.rotate(math.degrees(theta))
        points.append(current_point.copy())
    points.append(center_to_end_v)
    for i in range (n,-1,-1):
        if inside:
            points.append(points[i].scale(abs((abs(radius)-width)/abs(radius))))
        else:
            points.append(points[i].scale(abs((abs(radius) + width) / abs(radius))))
    actual_points = []
    for i in points:
        add_list = i.list()
        add_list[0] += center[0]
        add_list[1] += center[1]
        actual_points.append(add_list)

    return actual_points

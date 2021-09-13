import math
import GLOBALS
import pygame
import Vector
import Colors


def draw_dashed_line(globals, surface, start_point, end_point, width, color, dash_length=3.05):
    pix_width = round(globals.pixels(width))
    l = dash_length
    d = math.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2)
    n = math.floor(d / (2 * l))
    v = Vector.Vector((end_point[0] - start_point[0]), (end_point[1] - start_point[1]))
    v.set_magnitude(l)
    current_point = start_point[:]
    for i in range(n):
        pygame.draw.line(surface, color, globals.point_to_pixels(current_point),
                         globals.point_to_pixels((v.copy() + current_point).list()), width=pix_width)
        current_point = (v.copy() + v.copy() + current_point).list()

    if (2 * n + 1) * l >= d:
        pygame.draw.line(surface, color, globals.point_to_pixels(current_point),
                         globals.point_to_pixels(end_point), width=pix_width)
    else:
        pygame.draw.line(surface, color, globals.point_to_pixels(current_point),
                         globals.point_to_pixels((v.copy() + current_point).list()), width=pix_width)


def draw_double_line(globals, surface, start_point, end_point, width, color):  # Width in meters
    v = Vector.Vector((end_point[0] - start_point[0]), (end_point[1] - start_point[1]))
    v1 = v.copy()
    v1.rotate(90)
    v2 = v.copy()
    v2.rotate(270)
    v1.set_magnitude(2 * width)
    v2.set_magnitude(2 * width)
    pygame.draw.line(surface, color, globals.point_to_pixels((v2.copy() + start_point).list()),
                     globals.point_to_pixels((v2.copy() + end_point).list()), width=round(globals.pixels(width)))
    pygame.draw.line(surface, color, globals.point_to_pixels((v1.copy() + start_point).list()),
                     globals.point_to_pixels((v1.copy() + end_point).list()), width=round(globals.pixels(width)))


def draw_arc(globals, surface, start_point, end_point, radius, width, color, inside=True):
    # TODO pygame arc drawing leaves a little gap, plz fix
    center, start_angle, end_angle = two_point_arc_circle(start_point, end_point, radius)
    if globals.pixels(width) <= 2:
        draw_start = start_angle
        draw_end = end_angle
        if radius < 0:
            draw_start = end_angle
            draw_end = start_angle
            radius = abs(radius)
        pygame.draw.arc(surface, color, [globals.pixels(center[0] - radius), globals.pixels(center[1] - radius),
                                         globals.pixels(2 * radius), globals.pixels(2 * radius)], -draw_start,
                        -draw_end, math.ceil(globals.pixels(width)))
        print("draw line arc")

    else:
        points = get_arc_outline_points(globals, center, abs(radius), start_angle, end_angle, width, inside)
        pixel_points = []
        for i in points:
            pixel_points.append(globals.point_to_pixels(i))
            # pygame.draw.circle(surface,color,globals.point_to_pixels(i),3)

        pygame.draw.polygon(surface, color, pixel_points, 0)
    # pygame.draw.circle(surface, Colors.CAR_GREEN_LINE, globals.point_to_pixels(start_point), 7, width=1)
    # pygame.draw.circle(surface, Colors.CAR_RED_LINE, globals.point_to_pixels(end_point), 7, width=1)


def draw_dashed_arc(globals, surface, center, start_angle, end_angle, radius, width, color, inside=True, dash_length=3.05):
    # TODO pygame arc drawing leaves a little gap, plz fix
    print("Start Angle: ", math.degrees(start_angle))
    print("End Angle: ", math.degrees(end_angle))
    # pygame.draw.circle(surface, Colors.CAR_GREEN_LINE, globals.point_to_pixels(start_point), 7,
    #                    width=1)  # draw start point
    # pygame.draw.circle(surface, Colors.CAR_RED_LINE, globals.point_to_pixels(end_point), 7, width=1)  # draw end point
    # pygame.draw.circle(surface, Colors.MAP_ORANGE, globals.point_to_pixels(center), 7, width=1)  # draw center point
    pix_width = round(globals.pixels(width))
    l = dash_length
    d = abs(radius * ((end_angle - start_angle) % (2 * math.pi)))
    n = math.floor(d / (2 * l))
    dtheta = l / radius  # angle swept by one dash (one dash-space pair would be 2*dtheta)
    current_theta = start_angle

    if globals.pixels(width) <= 2:
        print("thin dashed arc N:", n)
        draw_start = start_angle
        draw_end = end_angle
        if radius < 0:
            draw_start = end_angle
            draw_end = start_angle
            radius = abs(radius)
        for i in range(n):
            if dtheta <= 0.05:
                line_start = globals.point_to_pixels([center[0] + math.cos(current_theta)*radius, center[1] + math.sin(current_theta)*radius])
                line_end = globals.point_to_pixels([center[0] + math.cos(current_theta-dtheta)*radius,center[1] + math.sin(current_theta-dtheta)*radius])
                pygame.draw.line(surface, color, line_start, line_end, math.ceil(globals.pixels(width)))
                # print("line_start:",line_start," line_end:",line_end, " Dtheta:", dtheta, " Width:", math.ceil(globals.pixels(width)))
            else:
                pygame.draw.arc(surface, color, [globals.pixels(center[0] - radius), globals.pixels(center[1] - radius),
                                                 globals.pixels(2 * radius), globals.pixels(2 * radius)],
                                -current_theta + dtheta,
                                -current_theta, math.ceil(globals.pixels(width)))
            current_theta -= dtheta * 2

        if (2 * n + 1) * l >= d:
            print("Current Theta: ", math.degrees(current_theta))
            if dtheta < 0.05:
                line_start = globals.point_to_pixels(
                    [center[0] + math.cos(current_theta) * radius, center[1] + math.sin(current_theta) * radius])
                line_end = globals.point_to_pixels([center[0] + math.cos(end_angle) * radius,
                                                    center[1] + math.sin(end_angle) * radius])
                pygame.draw.line(surface, color, line_start, line_end, math.ceil(globals.pixels(width)))
            else:
                pygame.draw.arc(surface, (255, 0, 0),
                                [globals.pixels(center[0] - radius), globals.pixels(center[1] - radius),
                                 globals.pixels(2 * radius), globals.pixels(2 * radius)], -end_angle,
                                -current_theta, math.ceil(globals.pixels(width)))
        else:
            if dtheta < 0.05:
                line_start = globals.point_to_pixels(
                    [center[0] + math.cos(current_theta) * radius, center[1] + math.sin(current_theta) * radius])
                line_end = globals.point_to_pixels([center[0] + math.cos(current_theta - dtheta) * radius,
                                                    center[1] + math.sin(current_theta - dtheta) * radius])
                pygame.draw.line(surface, color, line_start, line_end, math.ceil(globals.pixels(width)))
            else:
                pygame.draw.arc(surface, color, [globals.pixels(center[0] - radius), globals.pixels(center[1] - radius),
                                             globals.pixels(2 * radius), globals.pixels(2 * radius)],
                            -current_theta + dtheta,
                            -current_theta, math.ceil(globals.pixels(width)))

    else:
        for i in range(n):

            points = get_arc_outline_points(globals, center, abs(radius), current_theta, current_theta - dtheta, width,
                                            inside)
            pixel_points = []
            for i in points:
                pixel_points.append(globals.point_to_pixels(i))
            pygame.draw.polygon(surface, color, pixel_points, 0)
            current_theta -= dtheta * 2

        if (2 * n + 1) * l >= d:
            points = get_arc_outline_points(globals, center, abs(radius), current_theta, end_angle, width,
                                            inside)
            pixel_points = []
            for i in points:
                pixel_points.append(globals.point_to_pixels(i))
            pygame.draw.polygon(surface, color, pixel_points, 0)
        else:
            points = get_arc_outline_points(globals, center, abs(radius), current_theta, current_theta - dtheta, width,
                                            inside)
            pixel_points = []
            for i in points:
                pixel_points.append(globals.point_to_pixels(i))
            pygame.draw.polygon(surface, color, pixel_points, 0)

def draw_double_arc(globals, surface, start_point, end_point, radius, width, color):
    #radius is the centerline
    # TODO pygame arc drawing leaves a little gap, plz fix
    center, start_angle, end_angle = two_point_arc_circle(start_point, end_point, radius)
    if globals.pixels(width) <= 2:
        draw_start = start_angle
        draw_end = end_angle
        if radius < 0:
            draw_start = end_angle
            draw_end = start_angle
            radius = abs(radius)
        pygame.draw.arc(surface, color, [globals.pixels(center[0] - (radius-width)), globals.pixels(center[1] - (radius-width)),
                                         globals.pixels(2 * (radius-width)), globals.pixels(2 * (radius-width))], -draw_start,
                        -draw_end, math.ceil(globals.pixels(width)))
        pygame.draw.arc(surface, color, [globals.pixels(center[0] - (radius + 2 * width)), globals.pixels(center[1] - (radius + 2 * width)),
                                         globals.pixels(2 * (radius + 2 * width)), globals.pixels(2 * (radius + 2 * width))], -draw_start,
                        -draw_end, math.ceil(globals.pixels(width)))
        print("draw line arc")

    else:
        points = get_arc_outline_points(globals, center, abs(radius-width), start_angle, end_angle, width)
        pixel_points = []
        for i in points:
            pixel_points.append(globals.point_to_pixels(i))
            # pygame.draw.circle(surface,color,globals.point_to_pixels(i),3)

        pygame.draw.polygon(surface, color, pixel_points, 0)

        points = get_arc_outline_points(globals, center, abs(radius + 2*width), start_angle, end_angle, width)
        pixel_points = []
        for i in points:
            pixel_points.append(globals.point_to_pixels(i))
            # pygame.draw.circle(surface,color,globals.point_to_pixels(i),3)

        pygame.draw.polygon(surface, color, pixel_points, 0)
    # pygame.draw.circle(surface, Colors.CAR_GREEN_LINE, globals.point_to_pixels(start_point), 7, width=1)
    # pygame.draw.circle(surface, Colors.CAR_RED_LINE, globals.point_to_pixels(end_point), 7, width=1)

def two_point_arc_circle(start_point, end_point, radius):
    # returns the center point and angle swept (RADIANS) of an arc from start_point to end_point with given radius
    # Note: if radius is positive, the turn is a clockwise turn from the start_point
    points_vector = Vector.get_Vector_between_points(start_point, end_point)
    center_point = [(start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2]
    dist_to_center_point = math.sqrt(
        ((end_point[0] - start_point[0]) ** 2) + ((end_point[1] - start_point[1]) ** 2)) / 2
    if abs(radius) < dist_to_center_point:
        raise ValueError('Tried to generate an arc with a radius smaller than 1/2 the distance between the points.')

    if radius < 0:
        points_vector.rotate(90)
    else:
        points_vector.rotate(-90)

    points_vector.set_magnitude(math.sqrt((radius ** 2) - (dist_to_center_point ** 2)))

    points_vector += center_point

    center = points_vector.list()
    center_to_start_v = Vector.get_Vector_between_points(center, start_point)
    center_to_end_v = Vector.get_Vector_between_points(center, end_point)
    center_to_start = math.radians(center_to_start_v.angle())
    center_to_end = math.radians(center_to_end_v.angle())

    # print("Center: ", center)
    # print("Center to start: ", math.degrees(center_to_start))
    # print("Center to end: ", math.degrees(center_to_end))

    return center, center_to_start, center_to_end


def get_arc_outline_points(globals, center, radius, start_angle, end_angle, width, inside=True):
    # Note: if radius is positive, the turn is a clockwise turn from the start_point
    # Note: all values are in meters, but it shouldnt matter mathematically.
    # Note: angles are in RADIANS
    # Note: round numbers to 5 decimal places?
    f0 = 20 / (globals.PIXELS_PER_METER)  # 0.25 meters
    # f0 = 2

    phi = (end_angle - start_angle) % (2 * math.pi)
    if phi > math.pi:
        phi -= 2 * math.pi
    theta_0 = 2 * math.asin(f0 / (2 * radius))
    n = math.ceil(abs(phi) / abs(theta_0))
    theta = phi / n
    f = 2 * radius * math.sin(theta / 2)

    center_to_start_v = Vector.Vector(radius, 0)
    center_to_start_v.rotate_to(math.degrees(start_angle))
    center_to_end_v = Vector.Vector(radius, 0)
    center_to_end_v.rotate_to(math.degrees(end_angle))

    points = []
    points.append(center_to_start_v)
    current_point = center_to_start_v.copy()
    for i in range(1, n):
        current_point.rotate(math.degrees(theta))
        points.append(current_point.copy())
    points.append(center_to_end_v)
    for i in range(n, -1, -1):
        if inside:
            points.append(points[i].scale(abs((abs(radius) - width) / abs(radius))))
        else:
            points.append(points[i].scale(abs((abs(radius) + width) / abs(radius))))
    actual_points = []
    for i in points:
        add_list = i.list()
        add_list[0] += center[0]
        add_list[1] += center[1]
        actual_points.append(add_list)

    return actual_points

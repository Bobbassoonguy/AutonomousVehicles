import pygame


class Node:
    def __init__(self, parent, point, radius, arc=True):
        self.parent = parent
        self.x = point[0]
        self.y = point[1]
        self.arc = arc
        self.radius = radius
import math
import Object
import Vector
import pygame
from Classes.Scenario import Scenario
from Scenario import Scenario
import Colors

pygame.init()

done = False
main: Scenario = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.globals.PIXELS_PER_METER = 20
main.globals.FPS = 30



while not done:
    clock.tick(main.globals.FPS)
    main.globals.MAIN_SURFACE.fill((18, 20, 26))
    main.road_map.add_road([[30,1],[3,3],[3,6],[5,15],[25,30]])
    main.road_map.draw_lines(road_segment_points=True)

    #main.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
import math
import Object
import Vector
import pygame
from Classes.Scenario import Scenario
from Scenario import Scenario
import Colors

pygame.init()

done = False
main: Scenario = Scenario("Scenario 1 - Create Car",disp_x=200, disp_y=200, pix=5)
clock = pygame.time.Clock()

main.globals.FPS = 30

main.globals.MAIN_SURFACE.fill((18, 20, 26))
main.road_map.add_road([[30,20],[180,10],[170,150],[120,80],[25,30]])
#main.road_map.add_road([[10, 45], [35, 10]])
main.road_map.draw_roads()
main.road_map.draw_lines(road_segment_points=True)

pygame.display.flip()

while not done:
    clock.tick(main.globals.FPS)


    #main.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
import math
import Object
import Vector
import pygame
from Classes.Scenario import Scenario
from Scenario import Scenario
import Colors
import pygame_gui

pygame.init()

done = False
main: Scenario = Scenario("Scenario 1 - Create Car",disp_x=200, disp_y=200, pix=5)
clock = pygame.time.Clock()

main.globals.FPS = 30

# main.globals.BACKGROUND.fill((18, 250, 26)) # (18, 20, 26)

main.road_map.add_road([[30,20],[180,10,10],[170,150],[120,80],[25,30]])
#main.road_map.add_road([[10, 45], [35, 10]])
main.road_map.draw_roads()
main.road_map.draw_lines(road_segment_points=True)
main.globals.draw_arc(main.globals.VEHICLE_SURFACE, Colors.CAR_PURPLE_FILL, [30, 30], [80, 60], 30, 10)


while not done:
    clock.tick(main.globals.FPS)
    main.GUI.manager.update(main.globals.FPS)


    main.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        main.GUI.process_events(event)

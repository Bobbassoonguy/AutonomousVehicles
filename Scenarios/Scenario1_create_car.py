import math
import Object
import Vector
import pygame
from Classes.Scenario import Scenario
from Scenario import Scenario
import Colors
import pygame_gui
import Tools

pygame.init()

done = False
main: Scenario = Scenario("Scenario 1 - Create Car",disp_x=1000, disp_y=1000, pix=5)
clock = pygame.time.Clock()

main.globals.FPS = 30

# main.road_map.add_road([[30,20],[150,10,-100],[130,150],[120,80],[25,30]])
#main.road_map.add_road([[10, 45], [35, 10]])
main.road_map.draw_roads()
main.road_map.draw_lines(road_segment_points=True)
# main.globals.draw_arc(main.globals.VEHICLE_SURFACE, Colors.CAR_PURPLE_FILL, [30, 30], [80, 60], 30, 10)

# Tools.draw_dashed_line(main.globals, main.globals.VEHICLE_SURFACE,[60,100],[100,100],0.15,Colors.MAP_CYAN)
# Tools.draw_double_line(main.globals, main.globals.VEHICLE_SURFACE,[60,120],[100,150],0.15,Colors.MAP_YELLOW)

test_start = [100,100]
test_end = [140,140]
test_rad = -50
Tools.draw_dashed_arc(main.globals,main.globals.VEHICLE_SURFACE,test_start,test_end,test_rad,1,Colors.CAR_GREEN_LINE) # 1*3.66
Tools.draw_arc(main.globals,main.globals.VEHICLE_SURFACE,test_start,test_end,test_rad,.01,Colors.CAR_RED_LINE) # 1*3.66


while not done:
    time_delta = clock.tick(main.globals.FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            break
        if event.type == pygame.USEREVENT:
            main.GUI.process_event(event)
        main.GUI.manager_event_process(event)
    if done:
        break


    #all the actual stuff


    main.GUI.update_manager(time_delta)
    main.draw()



import math

import pygame
from Classes.Scenario import Scenario
from Scenario import Scenario

pygame.init()

done = False
main: Scenario = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar()
main.vehicles[0].rotate_to_angle(90, rotation_point="centroid")
# print(main.vehicles[0].x, ",", main.vehicles[0].y)
# print(main.vehicles[0].outline.get_centroid())
main.vehicles[0].move_to(20, 5)
main.vehicles[0].speed = 0
main.vehicles[0].acceleration = 3.5
main.vehicles[0].current_turn_radius = 20

while not done:
    clock.tick(main.FPS)
    main.main()

    main.vehicles[0].go(1/main.FPS)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
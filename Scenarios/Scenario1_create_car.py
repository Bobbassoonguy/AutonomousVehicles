import math

import pygame
from Classes.Scenario import Scenario
from Scenario import Scenario

pygame.init()

done = False
main: Scenario = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar(x=20, y=5)
main.vehicles[0].rotate_to_angle(90, rotation_point="centroid")
main.vehicles[0].speed = 0
main.vehicles[0].acceleration = 3.5
main.vehicles[0].current_turn_radius = 20

main.addCar(x=20, y=45, fill_color=(0, 51, 204), outline_color=(0, 153, 255))
main.vehicles[1].rotate_to_angle(270, rotation_point="centroid")
main.vehicles[1].speed = 40
main.vehicles[1].acceleration = 0
main.vehicles[1].current_turn_radius = 7

while not done:
    clock.tick(main.globals.FPS)
    main.main()

    main.vehicles[0].go(1/main.globals.FPS)
    main.vehicles[1].go(1 / main.globals.FPS)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
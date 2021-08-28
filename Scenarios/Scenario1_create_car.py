import math

import pygame
from Classes.Scenario import Scenario
pygame.init()

done = False
main = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar()
main.vehicles[0].turn(45, main.vehicles[0].outline.get_centroid())
main.vehicles[0].front_right_wheel.rotate(45)
main.vehicles[0].front_left_wheel.rotate(90)
main.vehicles[0].back_right_wheel.rotate(135)
main.vehicles[0].back_left_wheel.rotate(180)
counter = 0

while not done:
    clock.tick(main.FPS)
    main.main()
    counter += 1
    main.vehicles[0].turn(counter/30.0, main.vehicles[0].outline.get_centroid())
    main.vehicles[0].front_right_wheel.rotate(1)
    main.vehicles[0].front_left_wheel.rotate(1)
    main.vehicles[0].back_right_wheel.rotate(1)
    main.vehicles[0].back_left_wheel.rotate(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
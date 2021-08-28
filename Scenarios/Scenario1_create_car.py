import math

import pygame
from Classes.Scenario import Scenario
pygame.init()

done = False
main = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar()
main.vehicles[0].rotate(45, main.vehicles[0].outline.get_centroid())

while not done:
    clock.tick(main.FPS)
    main.main()

    main.vehicles[0].rotate(1, [500, 500])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
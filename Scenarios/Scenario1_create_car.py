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

    main.vehicles[0].turn(5.4, 1, right_turn=True, display_turn_circle=True)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
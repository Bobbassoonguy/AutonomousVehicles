import math

import pygame
from Classes.Scenario import Scenario
pygame.init()

done = False
main = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar()
main.vehicles[0].rotate(135, main.vehicles[0].outline.get_centroid())
main.vehicles[0].speed = 0
main.vehicles[0].acceleration = .5

# counter = 0
# right_turn = True
while not done:
    clock.tick(main.FPS)
    main.main()
    # counter += .5
    # if counter > 10:
    #     counter = 0
    #     right_turn = not right_turn
    main.vehicles[0].go(1/main.FPS)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
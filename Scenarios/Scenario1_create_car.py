import math

import pygame
from Classes.Scenario import Scenario
pygame.init()

done = False
main = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar()
main.vehicles[0].rotate(135, main.vehicles[0].outline.get_centroid())

counter = 0
right_turn = True
while not done:
    clock.tick(main.FPS)
    main.main()
    counter += .5
    if counter > 10:
        counter = 0
        right_turn = not right_turn
    main.vehicles[0].turn(5.4 + counter, 1, right_turn=right_turn, display_turn_circle=True)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
import math

import pygame
from Classes.Scenario import Scenario
pygame.init()

done = False
main = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar()
main.vehicles[0].rotate(45, main.vehicles[0].outline.get_centroid())

center = main.vehicles[0].get_turn_circle_center(200)
print(center)
while not done:
    clock.tick(main.FPS)
    main.main()

    main.vehicles[0].rotate(1, center)
    pygame.draw.circle(main.screen, [0,0,255], center, 200, width=2)
    pygame.draw.circle(main.screen, [0, 0, 255], center, 3, width=2)
    print(main.vehicles[0].x, ",",main.vehicles[0].y)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
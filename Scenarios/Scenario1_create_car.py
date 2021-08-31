import math
import Object
import Vector
import pygame
from Classes.Scenario import Scenario
from Scenario import Scenario
import Colors

pygame.init()

done = False
main: Scenario = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.globals.PIXELS_PER_METER = 20
main.addCar(x=20, y=10)
main.vehicles[0].rotate(45, main.vehicles[0].body.position())
main.vehicles[0].body.velocity.x = 10
main.vehicles[0].body.acceleration.x = 10
main.vehicles[0].current_turn_radius = 10

# main.addCar(x=20, y=45, fill_color=Colors.ORANGE_FILL, outline_color=Colors.ORANGE_LINE)
# main.vehicles[1].rotate(180, main.vehicles[1].body.position())
# main.vehicles[1].body.velocity.x = -40
# main.vehicles[1].current_turn_radius = -7

while not done:
    clock.tick(main.globals.FPS)
    main.main()

    main.vehicles[0].go(1/main.globals.FPS)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
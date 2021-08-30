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

main.globals.PIXELS_PER_METER = 50
main.addCar(x=10, y=5)
main.vehicles[0].body.rotate_to_angle(0, main.vehicles[0].body.position())
main.vehicles[0].body.velocity.x = 1
main.vehicles[0].body.acceleration.x = 3.5
main.vehicles[0].current_turn_radius = 20

# main.addCar(x=20, y=45, fill_color=Colors.ORANGE_FILL, outline_color=Colors.ORANGE_LINE)
# main.vehicles[1].body.rotate_to_angle(180, main.vehicles[1].body.position())
# main.vehicles[1].body.velocity.x = -40
# main.vehicles[1].current_turn_radius = 7

while not done:
    clock.tick(main.globals.FPS)
    main.main()

    main.vehicles[0].go(1/main.globals.FPS)
    # main.vehicles[1].go(1 / main.globals.FPS)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
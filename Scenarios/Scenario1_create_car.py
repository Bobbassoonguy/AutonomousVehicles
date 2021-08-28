import pygame
from Classes.Scenario import Scenario
pygame.init()

done = False
main = Scenario("Scenario 1 - Create Car")
clock = pygame.time.Clock()

main.addCar()
main.vehicles[0].turn(20)

while not done:
    clock.tick(main.FPS)
    main.main()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
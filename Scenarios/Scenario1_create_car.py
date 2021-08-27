import pygame
from Classes.Scenario import Scenario
pygame.init()

done = False
main = Scenario()

while not done:
    main.draw_frame(1)

pygame.quit()
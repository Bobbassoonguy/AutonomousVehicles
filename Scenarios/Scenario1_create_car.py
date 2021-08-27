import pygame
from Classes.Scenario import Scenario
pygame.init()

done = false
main = Scenario()

while not done:
    main.draw_frame()

pygame.quit()
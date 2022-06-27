import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))

while True:
    screen.fill((0, 0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
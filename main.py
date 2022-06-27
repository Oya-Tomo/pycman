import pygame
from pygame.locals import *
import sys
from block import block_data, feed_data

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("pycman")
    clock = pygame.time.Clock()

    blocks = [
        pygame.image.load("img/block/wall.png").convert_alpha(),
        pygame.image.load("img/block/field.png").convert_alpha(),
    ]
    items = [
        None,
        pygame.image.load("img/item/pixel.png").convert_alpha(),
        pygame.image.load("img/item/feed.png").convert_alpha(),
    ]

    while True:
        screen.fill((0, 0, 0))
        for y in range(len(block_data)):
            for x in range(len(block_data[0])):
                screen.blit(blocks[block_data[y][x]], (x * 30, y * 30))
        for y in range(len(feed_data)):
            for x in range(len(feed_data[0])):
                if items[feed_data[y][x]] != None:
                    screen.blit(items[feed_data[y][x]], (x * 30, y * 30))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        clock.tick(30)

if __name__ == "__main__":
    main()
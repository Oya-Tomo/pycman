import pygame
from pygame.locals import *
import sys
from block import block_data, feed_data
from pycman import Pycman

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

    pycman = Pycman(30, 30)

    while True:
        screen.fill((0, 0, 0))
        for y in range(len(block_data)):
            for x in range(len(block_data[0])):
                screen.blit(blocks[block_data[y][x]], (x * 30, y * 30))
        for y in range(len(feed_data)):
            for x in range(len(feed_data[0])):
                if items[feed_data[y][x]] != None:
                    screen.blit(items[feed_data[y][x]], (x * 30, y * 30))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    pycman.book_next_dir("right")
                elif event.key == K_UP:
                    pycman.book_next_dir("up")
                elif event.key == K_LEFT:
                    pycman.book_next_dir("left")
                elif event.key == K_DOWN:
                    pycman.book_next_dir("down")


        pycman.move()
        pycman.change_dir()
        pycman.draw(screen)
        pygame.display.update()
        print(pycman.x)
        print(pycman.y)
        print(pycman.dir)
        clock.tick(30)

if __name__ == "__main__":
    main()
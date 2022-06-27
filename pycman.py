import pygame
from block import block_data, feed_data

CHANGE_MOUTH_STATUS_LOOP = 4
BLOCK_SIZE = 30

SPEED_SLOW = 3
SPEED_FAST = 3

class Pycman(Character):
    def __init__(self, x, y):
        self.image = [
            [
                pygame.image.load("img/pycman/pycman1.png").convert_alpha(),
                pygame.transform.rotate(pygame.image.load("img/pycman/pycman1.png").convert_alpha(), 90),
                pygame.transform.rotate(pygame.image.load("img/pycman/pycman1.png").convert_alpha(), 180),
                pygame.transform.rotate(pygame.image.load("img/pycman/pycman1.png").convert_alpha(), 270),
            ],
            [
                pygame.image.load("img/pycman/pycman2.png").convert_alpha(),
                pygame.transform.rotate(pygame.image.load("img/pycman/pycman2.png").convert_alpha(), 90),
                pygame.transform.rotate(pygame.image.load("img/pycman/pycman2.png").convert_alpha(), 180),
                pygame.transform.rotate(pygame.image.load("img/pycman/pycman2.png").convert_alpha(), 270),
            ]
        ]

        self.x = x
        self.y = y
        self.dir = None
        self.next_dir = None
        self.mouth = 0

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image[self.get_mouth_status()][self.dir], (self.x, self.y))

    def move(self):
        if self.get_dir_block(self.dir) == 1:


    def get_mouth_status(self) -> int:
        if self.mouth > CHANGE_MOUTH_STATUS_LOOP:
            return 0
        else:
            return 1

    def change_dir(self):
        if self.x % BLOCK_SIZE == 0 and self.y % BLOCK_SIZE == 0:
            if self.get_dir_block(self.next_dir)

    def book_next_dir(self, dir_key: str):
        if dir_key == "right":
            self.next_dir = 0
        elif dir_key == "up":
            self.next_dir = 1
        elif dir_key == "left":
            self.next_dir = 2
        elif dir_key == "down":
            self.next_dir = 3

    def get_dir_block(self, dir: int) -> int:
        if dir == 0:
            dir_block = block_data[int(self.y / BLOCK_SIZE)][int(self.x / BLOCK_SIZE) + 1]
        elif dir == 1:
            dir_block = block_data[int(self.y / BLOCK_SIZE) - 1][int(self.x / BLOCK_SIZE)]
        elif dir == 2:
            dir_block = block_data[int(self.y / BLOCK_SIZE)][int(self.x / BLOCK_SIZE) - 1]
        elif dir == 3:
            dir_block = block_data[int(self.y / BLOCK_SIZE) + 1][int(self.x / BLOCK_SIZE)]
        return dir_block
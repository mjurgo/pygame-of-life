import pygame


class Cell:
    COLOR_ALIVE = 191, 6, 3
    COLOR_DEAD = 112, 141, 129
    WIDTH = 7
    HEIGHT = 7

    def __init__(self, size, grid_width, row: int, col: int) -> None:
        self.rect = pygame.Rect(
            size * col + grid_width,
            size * row + grid_width,
            size - grid_width,
            size - grid_width,
        )
        self.row = row
        self.col = col
        self.alive = 0
        self.color = self.COLOR_DEAD

    def kill(self):
        self.alive = 0
        self.color = self.COLOR_DEAD

    def revive(self):
        self.alive = 1
        self.color = self.COLOR_ALIVE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, neighbours_alive):
        if self.alive:
            if neighbours_alive < 2 or neighbours_alive > 3: self.kill()
        else:
            if neighbours_alive == 3: self.revive()

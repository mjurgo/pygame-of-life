import pygame


class Board:
    GRID_COLOR = 244, 213, 141
    GRID_WIDTH = 1

    def __init__(self, width: int, height: int, col_size: int) -> None:
        self.width = width
        self.height = height
        self.col_size = col_size
        self.cells = []
    
    def update(self, surface) -> None:
        self.draw(surface)

    def draw(self, surface) -> None:
        self.draw_grid(surface, self.width, self.height)
        self.draw_cells(surface)

    def draw_grid(self, surface, width, height) -> None:
        for i in range(0, width + 1, self.col_size):
            pygame.draw.line(surface, self.GRID_COLOR, (i, 0), (i, height), self.GRID_WIDTH)
        for i in range(0, height, self.col_size):
            pygame.draw.line(surface, self.GRID_COLOR, (0, i), (width, i), self.GRID_WIDTH)
            
    def draw_cells(self, surface) -> None:
        for row in self.cells:
            for cell in row:
                cell.draw(surface)

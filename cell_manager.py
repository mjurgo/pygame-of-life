import copy

from cell import Cell
from typing import List


class CellManager:
    def get_neighbours(self, cells, cell: Cell) -> List:
        cells = [[cells[i][j] if  i >= 0 and i < len(cells) and j >= 0 and j < len(cells[0]) and (i != cell.row or j != cell.col) else None
            for j in range(cell.col - 1, cell.col + 2)]
                for i in range(cell.row - 1, cell.row + 2)]

        return [cell for row in cells for cell in row if cell is not None]

    def get_alive_neighbours(self, cells, cell: Cell) -> List:
        return [neighbour for neighbour in self.get_neighbours(cells, cell) if neighbour.alive]

    def generate_lwss(self, width, height, col_size, grid_width) -> List:
        cells = []
        for row in range(0, height // col_size):
            cols = []
            for col in range(0, width // col_size):
                cols.append(Cell(col_size, grid_width, row, col))
            cells.append(cols)

        half_row = len(cells) // 2
        half_col = len(cells[0]) // 2

        cells[half_row][half_col].revive()
        cells[half_row][half_col + 3].revive()
        cells[half_row + 1][half_col - 1].revive()
        cells[half_row + 2][half_col - 1].revive()
        cells[half_row + 2][half_col + 3].revive()
        cells[half_row + 3][half_col - 1].revive()
        cells[half_row + 3][half_col].revive()
        cells[half_row + 3][half_col + 1].revive()
        cells[half_row + 3][half_col + 2].revive()

        return cells

    def update_cells(self, cells, width, height, col_size) -> List:
        new_cells = copy.deepcopy(cells)
        for row in range(0, height // col_size):
            for col in range(0, width // col_size):
                new_cells[row][col].update(len(self.get_alive_neighbours(cells, cells[row][col])))
        
        return new_cells

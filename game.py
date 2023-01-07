import pygame

from board import Board
from cell_manager import CellManager


class Game:
    WIDTH, HEIGHT = 640, 480
    CELL_SIZE = 8

    BG_COLOR = 112, 141, 129
    TXT_COLOR = 191, 6, 3
    FPS = 3

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("CONWAY'S GAME OF LIFE")

        self.font = pygame.font.SysFont('Arial', 35)

        self.clock = pygame.time.Clock()
        self.cell_manager = CellManager()

        self.board = Board(self.WIDTH, self.HEIGHT, self.CELL_SIZE)
        self.board.cells = self.cell_manager.generate_lwss(self.WIDTH, self.HEIGHT, self.CELL_SIZE, self.board.GRID_WIDTH)

    def update(self):
        self.board.cells = self.cell_manager.update_cells(self.board.cells, self.WIDTH, self.HEIGHT, self.CELL_SIZE)
        self.board.update(self.screen)


    def run(self):
        pause = True
        running = True

        while running:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        pause = not pause
                    if event.key == pygame.K_r:
                        self.restart()
                        pause = True


            self.screen.fill(self.BG_COLOR)

            self.board.draw(self.screen)

            if not pause:
                self.update()
            else:
                img = self.font.render('Space to pause/unpause, R to restart', True, self.TXT_COLOR)
                self.screen.blit(img, (0, 20))

            pygame.display.update()

    def restart(self):
        self.board = Board(self.WIDTH, self.HEIGHT, self.CELL_SIZE)
        self.board.cells = self.cell_manager.generate_lwss(self.WIDTH, self.HEIGHT, self.CELL_SIZE, self.board.GRID_WIDTH)

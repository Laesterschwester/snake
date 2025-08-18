import config
import pygame

class Grid:
    def __init__(self):
        self.width = config.WINDOW_WIDTH
        self.height = config.WINDOW_HEIGHT
        self.cell_size = config.TILE_WIDTH
        self.color = config.TILE_COLOR

    def draw_grid(self, display):
        for x in range(0, self.width, config.TILE_WIDTH + config.TILE_SPACING):
            for y in range(0, self.height, config.TILE_WIDTH + config.TILE_SPACING):
                pygame.draw.rect(
                    display, self.color, (x, y, self.cell_size, self.cell_size)
                )
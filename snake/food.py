import config
from random import randrange
import pygame


class Food:
    food = []

    def __init__(self):
        self.position = Food.add_food()
        Food.food.append(self)

    @classmethod
    def add_food(cls):
        # TODO: nowhere left to place -> win
        while True:
            x = randrange(
                0, (config.NUMBER_OF_TILES_HEIGHT - 1) * config.WINDOW_RATIO - 1
            )
            y = randrange(0, config.NUMBER_OF_TILES_HEIGHT - 1)
            if [x, y] not in Food.food:
                break
        return [x, y]

    @classmethod
    def remove_food(cls, food):
        cls.food.remove(food)

    def draw_food(self, display):
        for i in range(len(Food.food)):
            scalar = config.TILE_WIDTH + config.TILE_SPACING
            pygame.draw.rect(
                display,
                config.FOOD_COLOR,
                (
                    Food.food[i].position[0] * scalar,
                    Food.food[i].position[1] * scalar,
                    config.TILE_WIDTH,
                    config.TILE_WIDTH,
                ),
            )

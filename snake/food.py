import config
from random import randrange
import pygame


class Food:
    foodBasket = []
    foodOnScreen = 0

    def addFood(self, display):
        #hier auch memoisieren
        x = randrange(0, (config.NUMBER_OF_TILES_HEIGHT-1)*config.WINDOW_RATIO-1) * (config.TILE_WIDTH + config.TILE_SPACING)
        y = randrange(0, config.NUMBER_OF_TILES_HEIGHT-1) * (config.TILE_WIDTH + config.TILE_SPACING)
        position = [x, y]
        self.foodOnScreen += 1
        self.foodBasket.append(position)
        pygame.draw.rect(display, config.FOOD_COLOR, (x, y, config.TILE_WIDTH, config.TILE_WIDTH))

    def delete_Food(self):
        self.foodBasket.pop(0)
        self.foodOnScreen -= 1

    def draw_food(self, display):
        for i in range(self.foodOnScreen):
            pygame.draw.rect(display, config.FOOD_COLOR, (self.foodBasket[i][0], self.foodBasket[i][1], config.TILE_WIDTH, config.TILE_WIDTH))
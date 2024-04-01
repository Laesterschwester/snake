import config
import pygame
import borderCol

class Snake:
    foodInStomachDuration = []
    longBoi = []
    head_position = [0, 0]
    butt_position = head_position
    speed = [0, 1]
    length = 1
    foodInStomach = []
    lastPosition = []

    def check_Bounds(self):
        if self.head_position[0]>config.WINDOW_WIDTH or self.head_position[0]<0 or self.head_position[1]>config.WINDOW_HEIGHT or self.head_position[1]<0:
            pygame.quit()

    def updateStomach(self):
        i = 0
        for duration in self.foodInStomachDuration:
            self.foodInStomachDuration[i] += 1

            if duration-1 >= len(self.longBoi):
                self.longBoi.append(self.foodInStomach[0])
                self.foodInStomach.pop(0)
                self.foodInStomachDuration.pop(0)
                self.length += 1
            i += 1

    def eat(self, food):
        index = 0
        for i in food.foodBasket:
            if self.head_position[0] == i[0] and self.head_position[1] == i[1]:
                food.foodOnScreen -= 1
                del food.foodBasket[index]
                #wartet so lange, bis es das Ende von longBoi erreicht hat und dann append
                self.foodInStomach.append(i)

                self.foodInStomachDuration.append(0)
            index += 1

    def drawStomach(self, display):
        "hier prozentualen offset einbauen um Bauch dick zu machen"
        for i in self.foodInStomach:
            pygame.draw.rect(display, self.color, (i[0]-3, i[1]-3, config.TILE_WIDTH*1.5, config.TILE_WIDTH*1.5))

    def __init__(self, display):
        self.color = (124, 252, 0)
        self.draw_snake(display)

    def mov_body(self):
        self.longBoi.insert(0, self.lastPosition)
        del self.longBoi[-1]

    def draw_snake(self, display):
        pygame.draw.rect(display, self.color, (self.head_position[0], self.head_position[1], config.TILE_WIDTH, config.TILE_WIDTH))
        for snek in self.longBoi:
            pygame.draw.rect(display, self.color, (snek[0], snek[1], config.TILE_WIDTH, config.TILE_WIDTH))

    def direction(self, keyEvent):
        if keyEvent == "up" and (not self.speed[1] == 1):
            self.speed = [0, -1]
        if keyEvent == "left" and (not self.speed[0] == 1):
            self.speed = [-1, 0]
        if keyEvent == "down" and (not self.speed[1] == -1):
            self.speed = [0, 1]
        if keyEvent == "right" and (not self.speed[0] == -1):
            self.speed = [1, 0]

    def collisionCheck(self):
        for body in self.longBoi:
            if self.head_position == body:
                pygame.quit()

    def move(self):
        self.lastPosition = self.head_position.copy()
        borderCol.borderCol(self.head_position, self.speed)
        self.head_position[0] += self.speed[0] * (config.TILE_WIDTH + config.TILE_SPACING)
        self.head_position[1] += self.speed[1] * (config.TILE_WIDTH + config.TILE_SPACING)
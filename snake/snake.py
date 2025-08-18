import config
import pygame


class SnakeSegment:
    def __init__(self, position, color, is_active):
        self.position = position
        self.color = color
        self.is_active = is_active

    def draw(self, display):
        tile_width = config.TILE_WIDTH
        scalar = tile_width + config.TILE_SPACING
        color = self.color
        if not self.is_active:
            color = (154, 202, 0)
        pygame.draw.rect(
            display,
            color,
            (
                self.position[0] * scalar,
                self.position[1] * scalar,
                tile_width,
                tile_width,
            ),
        )


class Snake:
    def __init__(self):
        color = (124, 252, 0)
        self.color = color
        self.long_boi = [SnakeSegment([0, 0], color, True)]
        self.direction = [0, 1]
        self.prev_direction = self.direction

    def move(self, wall_collision):
        self.prev_direction = self.direction
        head = self.long_boi[0]
        head_position = head.position
        x_next = head_position[0] + self.direction[0]
        y_next = head_position[1] + self.direction[1]

        wrap_around = False
        number_of_tiles_height = config.NUMBER_OF_TILES_HEIGHT
        number_of_tiles_width = config.NUMBER_OF_TILES_WIDTH

        if not (
            0 <= x_next < number_of_tiles_width and 0 <= y_next < number_of_tiles_height
        ):
            if wall_collision:
                # TODO: fail message instead of quitting
                # exit()
                pass
            wrap_around = True

        for i in range(len(self.long_boi) - 1, 0, -1):
            segment = self.long_boi[i]
            if segment.is_active:
                self.long_boi[i].position = self.long_boi[i - 1].position
            else:
                if segment.position == self.long_boi[i - 1].position:
                    self.long_boi[i].is_active = True

        head.position = [x_next, y_next]
        head_position = head.position
        if wrap_around:
            if head_position[0] <= -1:
                head.position = [number_of_tiles_width - 1, y_next]
            if head_position[1] <= -1:
                head.position = [x_next, number_of_tiles_height - 1]
            if head_position[0] >= number_of_tiles_width:
                head.position = [0, y_next]
            if head_position[1] >= number_of_tiles_height:
                head.position = [x_next, 0]

        # self collision
        for body_segment in self.long_boi[1:]:
            if head_position == body_segment.position:
                if body_segment.is_active:
                    exit()

    def draw(self, display):
        for boi_bits in self.long_boi:
            boi_bits.draw(display)

    def eat(self, foods):
        for food in foods:
            if self.long_boi[0].position == food.position:
                foods.remove(food)
                self.long_boi.append(SnakeSegment(food.position, self.color, False))
                break

    def handle_input(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not self.prev_direction == [1, 0]:
                    self.direction = [-1, 0]
                if event.key == pygame.K_RIGHT and not self.prev_direction == [-1, 0]:
                    self.direction = [1, 0]
                if event.key == pygame.K_DOWN and not self.prev_direction == [0, -1]:
                    self.direction = [0, 1]
                if event.key == pygame.K_UP and not self.prev_direction == [0, 1]:
                    self.direction = [0, -1]

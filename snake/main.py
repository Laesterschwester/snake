import pygame
import grid
import config
import snake
import food


def update_game(dangernoodle):
    if len(food.Food.food) == 0:
        food.Food()
    dangernoodle.move(False)
    dangernoodle.eat(food.Food.food)


def draw(dangernoodle, grid, nomnomnomnomnom, display):
    grid.draw_grid(display)
    nomnomnomnomnom.draw_food(display)
    dangernoodle.draw(display)


def start():
    pygame.init()

    size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    display = pygame.display.set_mode(size)
    display.fill((255, 255, 255, 255))
    clock = pygame.time.Clock()

    new_grid = grid.Grid()
    new_dangernoodle = snake.Snake()
    nomnomnomnomnom = food.Food()

    frameTimer = 0

    while True:
        key_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                key_events.append(event)
            new_dangernoodle.handle_input(key_events)

        time = pygame.time.get_ticks() - frameTimer
        if time >= config.SNAKE_SPEED:
            update_game(new_dangernoodle)
            frameTimer = pygame.time.get_ticks()
        draw(new_dangernoodle, new_grid, nomnomnomnomnom, display)

        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__":
    start()

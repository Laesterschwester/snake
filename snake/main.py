import pygame
import grid
import config
import snake
import food

pygame.init()
size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
display = pygame.display.set_mode(size)

display.fill(
        (255, 255, 255, 255)
    )

clock = pygame.time.Clock()  # Create a clock object to control the frame rate

new_grid = grid.Grid(display)
new_dangernoodle = snake.Snake(display)
nomnomnomnomnom = food.Food()
key_pressed = False

frameTimer = 0

eventQueue = []

while 1:
    display.fill(
        (255, 255, 255, 255)
    )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    new_grid.draw_grid()
    new_dangernoodle.check_Bounds()
    nomnomnomnomnom.draw_food(display)


    if nomnomnomnomnom.foodOnScreen == 0:
        nomnomnomnomnom.addFood(display)

    new_dangernoodle.draw_snake(display)
    if new_dangernoodle.foodInStomach:
        new_dangernoodle.drawStomach(display)

    time = pygame.time.get_ticks() - frameTimer
    if time >= config.SNAKE_SPEED:
        new_dangernoodle.collisionCheck()

        if eventQueue:
            new_dangernoodle.direction(eventQueue[0])
        new_dangernoodle.move()
        if nomnomnomnomnom.foodOnScreen > 0:
            new_dangernoodle.eat(nomnomnomnomnom)
        new_dangernoodle.updateStomach()
        if new_dangernoodle.longBoi:
            new_dangernoodle.mov_body()
        frameTimer = pygame.time.get_ticks()
        if eventQueue:
            eventQueue.pop(0)

    if event.type == pygame.KEYDOWN:
        if len(eventQueue) < 3:
            if event.key == pygame.K_UP and not key_pressed:
                eventQueue.append("up")
                key_pressed = True
            elif event.key == pygame.K_DOWN and not key_pressed:
                eventQueue.append("down")
                key_pressed = True
            elif event.key == pygame.K_LEFT and not key_pressed:
                eventQueue.append("left")
                key_pressed = True
            elif event.key == pygame.K_RIGHT and not key_pressed:
                eventQueue.append("right")
                key_pressed = True

        # Handle key releases
    if event.type == pygame.KEYUP:
        key_pressed = False

    pygame.display.update()

    clock.tick(60)  #Limit the frame rate to 60 frames per second
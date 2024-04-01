import config

def borderCol(head_position, speed):
    if head_position[0] + speed[0] < 0:
        borderColLeft(head_position, speed)

    elif head_position[0] + speed[0]*(config.TILE_WIDTH + config.TILE_SPACING) > config.WINDOW_WIDTH-10:
        borderColRight(head_position, speed)

    elif head_position[1] + speed[1] < 0:
        borderColTop(head_position, speed)

    elif head_position[1] + speed[1]*(config.TILE_WIDTH + config.TILE_SPACING) > config.WINDOW_HEIGHT:
        borderColBot(head_position, speed)


def borderColTop(head_position, speed):
    head_position[1] = config.WINDOW_HEIGHT+config.TILE_SPACING

def borderColBot(head_position, speed):
    #wegen updatae Reihenfolge muss um ein Tile vershoben sein
    head_position[1] = 0 - (config.TILE_WIDTH+ config.TILE_SPACING)

def borderColRight(head_position,speed):
    #wegen updatae Reihenfolge muss um ein Tile vershoben sein
    head_position[0] = 0 - (config.TILE_WIDTH+ config.TILE_SPACING)


def borderColLeft(head_position, speed):
    head_position[0] = config.WINDOW_WIDTH+config.TILE_SPACING
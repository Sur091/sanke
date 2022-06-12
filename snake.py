import pygame as py


def draw_board(surface):
    for i in range(0, width + tile, tile):
        py.draw.line(surface, (0, 0, 0), (i, 0), (i, height))

    for j in range(0, height + tile, tile):
        py.draw.line(surface, (0, 0, 0), (0, j), (width, j))


class Snake:
    def __init__(self):
        self.body = [py.Vector2(width // tile // 2, height // tile // 2)]
        self.dir = right
        self.event = []
        self.eaten = False

    def update(self):
        if self.event:
            k = self.event.pop()
            if k != -self.dir:
                self.dir = k

        temp = py.Vector2(self.body[-1].x, self.body[-1].y)
        for a in range(len(self.body) - 1, 0, -1):
            self.body[a] = py.Vector2(self.body[a - 1].x, self.body[a - 1].y)
        self.body[0] += self.dir
        self.body[0].x %= width // tile
        self.body[0].y %= height // tile

        if self.eaten:
            self.body.append(temp)
            self.eaten = False

    def show(self, surface):
        for a in range(len(self.body)):
            x_, y_ = self.body[a].x * tile, self.body[a].y * tile
            py.draw.rect(surface, (60, 63, 65), py.Rect(x_, y_, tile, tile))
            py.draw.rect(surface, (0, 0, 0), py.Rect(x_, y_, tile, tile), 1)


py.init()

width, height = 420, 300
tile = 30
window = py.display.set_mode((width, height))

# I am really serious, this is all to just define directions.
up = py.Vector2(0, -1)
down = py.Vector2(0, 1)
right = py.Vector2(1, 0)
left = py.Vector2(-1, 0)

directions = {py.K_DOWN: down,
              py.K_UP: up,
              py.K_RIGHT: right,
              py.K_LEFT: left}

running = True
clock = py.time.Clock()
frame_rate = 60
speed = 4
frames = 0

player1 = Snake()

while running:
    window.fill((255, 255, 255))
    clock.tick(frame_rate)
    frames += 1

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key in directions:
                player1.event[0:0] = [directions[event.key]]

        if event.type == py.MOUSEBUTTONDOWN:
            player1.eaten = True

    player1.show(window)
    if frames % (frame_rate // speed) == 0:
        frames = 0
        player1.update()

    draw_board(window)
    py.display.update()

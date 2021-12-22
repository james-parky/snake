'Snake class for snake game'


class Snake:
    'Snake class'

    def __init__(self, start_x=0, start_y=0):
        'Initialiser'
        self.head_x = start_x
        self.head_y = start_y
        self.length = 1
        self.body = [(self.head_x, self.head_y)]

    def move(self, direction, board):
        'Move the snake'
        head_position = {'LEFT': (self.head_x-1, self.head_y),
                         'RIGHT': (self.head_x+1, self.head_y),
                         'UP': (self.head_x, self.head_y-1),
                         'DOWN': (self.head_x, self.head_y+1)}[direction]

        if board.cell_is_snake(head_position) or board.cell_is_wall(head_position):
            return 0

        if board.cell_is_food(head_position):
            self.length += 1
            self.body.insert(0, head_position)
            self.head_x, self.head_y = head_position
            return 1

        self.body.insert(0, head_position)
        self.body.pop()
        self.head_x, self.head_y = head_position
        return 1

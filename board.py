'Game board class for snake game'


class Board:
    'Game board class'

    def __init__(self, width=20, height=20):
        'Initialiser'
        self.width = width
        self.height = height
        self.cells = [['' for x in range(width)] for y in range(height)]

    def update(self, snake):
        'Update the contents of the boards cells'
        self.cells = [[cell if cell == 'f' else '' for cell in row]
                      for row in self.cells]
        for cell in snake.body:
            self.cells[cell[1]][cell[0]] = 's'

    def cell_is_food(self, cell):
        'Check if a board cell contains food'
        return self.cells[cell[1]][cell[0]] == 'f'

    def cell_is_snake(self, cell):
        'Check if a board cell contains the snake'
        return self.cells[cell[1]][cell[0]] == 's'

    def cell_is_wall(self, cell):
        'Check if a boar cell is a wall'
        return not (0 <= cell[0] < self.height and 0 <= cell[1] < self.width)

    def has_food(self):
        'Check if the board contains any food'
        return any('f' in row for row in self.cells)

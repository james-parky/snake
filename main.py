'Snake Game Main class'
from tkinter import messagebox, Tk, Canvas
import random
import sys
from board import Board
from snake import Snake
WIDTH = 500
HEIGHT = 500


class Main:
    'Main game class'

    def __init__(self):
        'Initialise game'
        self.root = Tk('gme')
        self.root.title('Score: 100')
        self.root.geometry(f'{WIDTH}x{HEIGHT}')
        self.root.protocol('WM_DELETE_WINDOW', self.root.destroy)

        self.set_key_bindings()
        self.window = Canvas(self.root, width=WIDTH, height=HEIGHT, bg='black')
        self.window.pack()

        self.board = Board()
        self.snake = Snake(10, 10)
        self.last_direction = 'RIGHT'

    def set_key_bindings(self):
        'Set key bindings for Tkinter'
        self.root.bind('<Left>', self.set_direction)
        self.root.bind('<Right>', self.set_direction)
        self.root.bind('<Up>', self.set_direction)
        self.root.bind('<Down>', self.set_direction)

    def check_food(self):
        'Check if the game board contains food and add some if not'
        if not self.board.has_food():
            food_x, food_y = (random.randint(0, self.board.width-1),
                              random.randint(0, self.board.height-1))
            while self.board.cells[food_y][food_x] != '':
                food_x, food_y = (random.randint(0, self.board.width-1),
                                  random.randint(0, self.board.height-1))
            self.board.cells[food_y][food_x] = 'f'

    def run(self):
        'Main game loop'
        self.root.title(f'Score: {self.snake.length*100}')
        self.check_food()
        self.board.update(self.snake)
        self.draw_grid()
        self.root.after(100, self.move)

    def move(self):
        'Move the snake based on user input'
        if not self.snake.move(self.last_direction, self.board):
            game_over_message_box = messagebox.askquestion(
                "Game Over", "Would you like to play again?")
            if game_over_message_box == 'yes':
                self.root.destroy()
                Main().run()
            else:
                self.root.destroy()
                sys.exit()
        self.run()

    def set_direction(self, event):
        'Set moving direction of the snake'
        self.last_direction = event.keysym.upper()

    def draw_grid(self):
        'Draw the game board'
        cell_dimension = WIDTH/20
        self.window.delete('all')
        for y, row in enumerate(self.board.cells):
            for x, cell in enumerate(row):
                colour = {'': 'black', 's': 'white', 'f': 'red'}[cell]
                self.window.create_rectangle(
                    x*cell_dimension, y*cell_dimension,
                    (x+1)*cell_dimension, (y+1)*cell_dimension,
                    fill=colour, outline='white')


if __name__ == '__main__':
    main = Main()
    main.run()
    main.root.mainloop()

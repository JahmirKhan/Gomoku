from tkinter import *
from gomoku.logic import Possition


class create:
    possition = Possition

    def __init__(self, root, n, square_size):
        self.root = root
        self.n = n
        self.square_size = square_size
        self.w = self.h = self.square_size * self.n

    def panel(self):
        w = h = self.square_size * self.n
        self.table = Canvas(self.root,

                            width=w + 6 * self.square_size,
                            height=h + 6 * self.square_size,
                            bg='#869b56')
        table = self.table
        table.place(x=0, y=0)
        for x in [37 / 2, 5 / 2]:
            for i in range(1, 16):
                panel = table.create_text(x * self.square_size,
                                          (i) * self.square_size + (1) * self.square_size,
                                          text=str(f'{i}'.ljust(2)))
        for y in [1, 34 / 2]:
            for i in range(1, 16):
                table.create_text(self.square_size * (5 / 2) + self.square_size * (i), self.square_size * y,
                                  text=chr(64 + i))

        coords_pos_x = self.square_size * 6
        coords_pos_y = self.square_size * 18

        self.a = Label(self.root, text='x: 7 y: 7', bg='#8c6027', font=('Helvetica', 20))

        self.a.place(x=coords_pos_x + self.square_size / 2, y=coords_pos_y + self.square_size / 2)
        self.moves = Label(self.root, text='Moves: black', bg='#8c6027', font=('Helvetica', 20))
        self.moves.place(x=coords_pos_x + self.square_size * 4 + 10 + self.square_size / 2,
                         y=coords_pos_y + self.square_size / 2)

    def oval(self, x1, y1, size_of_circle, color):
        self.l1.append(self.board.create_oval(x1 * self.square_size - size_of_circle,
                                              y1 * self.square_size - size_of_circle,
                                              x1 * self.square_size + size_of_circle,
                                              y1 * self.square_size + size_of_circle,
                                              fill=color))

    def create_board(self):
        self.board = Canvas(self.root,
                            width=self.w,
                            height=self.h,
                            # cursor='none',
                            bg='#cfa360')
        # Shadow(self.board, color='#00ffff', size=1.03, offset_x=-5)
        w = h = self.square_size * self.n
        board = self.board
        size = self.square_size
        self.l1 = []

        for x in range(15):
            self.l1.append(board.create_line(size / 2 + x * size, size / 2, size / 2 + x * size, size / 2 + 14 * size))
        for y in range(15):
            self.l1.append(board.create_line(size / 2, size / 2 + y * size, size / 2 + 14 * size, size / 2 + size * y))
        size_of_circle = size / 10

        for i in range(3, 12, 4):
            for j in range(3, 12, 4):
                self.oval(i + 0.5, j + 0.5, size_of_circle, 'black')
        board.place(x=3 * size, y=3 / 2 * size)

    def update(self, board, board_n, size_of_circle, player, x, y):

        self.player = player
        player = self.player
        for item in board.find_all():
            if item not in self.l1:
                board.delete(item)
        self.moves.config(text='Moves: ' + ('black' if player == 'white' else 'white'))
        for i in range(len(board_n)):
            for j in range(len(board_n)):
                if board_n[i][j] == 'b':
                    board.create_oval(j * self.square_size + size_of_circle,
                                      i * self.square_size + size_of_circle,
                                      (j + 1) * self.square_size - size_of_circle,
                                      (i + 1) * self.square_size - size_of_circle,
                                      fill='black')
                elif board_n[i][j] == 'w':
                    board.create_oval(j * self.square_size + size_of_circle,
                                      i * self.square_size + size_of_circle,
                                      (j + 1) * self.square_size - size_of_circle,
                                      (i + 1) * self.square_size - size_of_circle,
                                      fill='white')
                elif board_n[i][j] == ' ':
                    print(' ', end=' ')

                elif board_n[i][j] == '3' and player == 'white':
                    board.create_oval(j * self.square_size + size_of_circle,
                                      i * self.square_size + size_of_circle,
                                      (j + 1) * self.square_size - size_of_circle,
                                      (i + 1) * self.square_size - size_of_circle,
                                      outline='#8B0000', width=6, dash=7, fill='red')
                    # board.create_text((j) * self.square_size + size_of_circle * (1 / 2) + 2,
                    #                   (i) * self.square_size + size_of_circle * (1 / 2) + 4,
                    #                   text="33", font=('Courier', 16), fill='red')

    def enter(self, event):
        board = self.board
        square_size = self.square_size
        x = int(event.x / square_size)
        y = int(event.y / square_size)

        # Remove any existing squares
        for item in board.find_all():
            if board.type(item) == 'rectangle':
                board.delete(item)
        # Create new square
        self.board.create_rectangle(x * square_size,
                                             y * square_size,
                                             square_size * (x + 1),
                                             square_size * (y + 1),
                                             outline='green',
                                             dash=8,
                                             width=2)

    def update_coords(self, event):
        x = int(event.x / self.square_size)
        y = int(event.y / self.square_size)
        self.a.config(text=f'x: {x + 1} y: {y + 1}')
        self.enter(event)

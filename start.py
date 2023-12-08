import random
import sys
from tkinter import *
from tkinter.messagebox import showinfo, askyesno


import gomoku.GUI as GUI
import gomoku.logic as logic
from gomoku.Engine import GomokuFish


class Game:
    def run(self):
        self.root.title('Gomoku')
        self.root.minsize(self.square_size * (self.n + 6),
                          self.square_size * (self.n + 6))
        self.root.resizable(False, False)
        self.create.panel()
        self.create.create_board()

        self.p_v_c = askyesno(title='Question!', message='Do you want to play bot?')
        if self.p_v_c:
            self.black_white = (
                askyesno(title='One more question!', message='Are we playing black?'))
        try:
            if not self.black_white and self.p_v_c:
                board = self.create.board
                self.digit_board[7][7] = 'b'
                self.create.update(board, self.digit_board, 27, 'black', 7, 7)
        except:
            pass
        self.color = 'black'
        if self.p_v_c:
            if self.black_white:
                self.color = 'black'
            else:
                self.color = 'white'

        self.create.board.bind('<Button 1>', self.human_moves)
        self.create.board.bind('<Motion>', self.create.enter)
        self.create.board.bind('<Motion>', self.create.update_coords)

        self.root.mainloop()

    def __init__(self, square_size=30, n=15):

        self.y = 7
        self.x = 7
        self.root = Tk()

        self.digit_board = [[' ' for _ in range(n)] for _ in range(n)]
        self.square_size = 30
        self.create = GUI.create(self.root, n, self.square_size)
        self.possition = logic.Possition(self.digit_board, self.x, self.y)

        self.n = n
        self.square_size = square_size
        self.h = self.w = self.square_size * n




    def human_moves(self, event):
        if self.digit_board[int(len(self.digit_board) / 2)][int(len(self.digit_board) / 2)] == ' ':
            self.x = 7
            self.y = 7
        else:
            self.x = int((event.x / self.square_size))
            self.y = int((event.y / self.square_size))
            if (self.digit_board[self.y][self.x] == 'b') or (self.digit_board[self.y][self.x] == 'w') or (self.digit_board[self.y][self.x] == '3' and self.color == 'black'):
                return
        self.make_a_move()


        if self.p_v_c:
            self.bot_moves()

    def bot_moves(self):
        self.gomoku_fish = GomokuFish()
        bot_move = self.gomoku_fish.get_move(self.digit_board, self.x, self.y)
        self.x, self.y = bot_move

        while (self.digit_board[self.y][self.x] == 'b') or (self.digit_board[self.y][self.x] == 'w'):
            print(self.digit_board[self.x][self.y])

            self.x = random.randint(0, 14)
            self.y = random.randint(0, 14)
        try:
            self.make_a_move()

        except:
            pass


    def make_a_move(self):
        x = self.x
        y = self.y
        size_of_circle = self.square_size - 3
        board = self.create.board


        self.digit_board[y][x] = str('b' if self.color == 'black' else 'w')
        self.digit_board = (self.possition.check33(self.digit_board))
        self.create.update(board, self.digit_board, size_of_circle, self.color, x, y)

        self.change_color()

        if self.possition.check_win(self.color, x, y, 5, 5):
            showinfo(title='GAME OVER', message=f'AND THE GAME {"BLACK" if self.black_white else "WHITE"} WON!')
            want_to_play_more = askyesno(message='DO YOU WANT TO PLAY MORE?')
            if not want_to_play_more:
                sys.exit()

            self.root.destroy()


    def change_color(self):
        if self.color == 'black':
            self.color = 'white'
        else:
            self.color = 'black'

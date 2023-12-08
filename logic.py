from tkinter import *


class Possition:
    def __init__(self, board, x, y):
        self.board = board
        self.x = x
        self.y = x

    def move_possible(self, x, y, color):
        if self.board[x][y] == ' ' or ((self.board[x][y]=='3') and (color=='white')):
            return True
        return False

    def check_win(self, color, x, y, n, m):

        player = str('b' if color != 'black' else 'w')
        # direction = [(0,1),(1,0),(1,1),(-1,-1)]

        return self.check_direction(y, x, 0, 1, -n + 1, n, player, m, True) or \
            self.check_direction(y, x, 1, 0, -n + 1, n, player, m, True) or \
            self.check_direction(y, x, 1, 1, -n + 1, n, player, m, True) or \
            self.check_direction(y, x, -1, 1, -n + 1, n, player, m, True)
    def check_six_in_row(self, player, x, y):
        # direction = [(0,1),(1,0),(1,1),(-1,1)]
        return self.check_direction(y, x, 0, 1, -6 + 1, 6, player, 6) or \
            self.check_direction(y, x, 1, 0, -6 + 1, 6, player, 6) or \
            self.check_direction(y, x, 1, 1, -6 + 1, 6, player, 6) or \
            self.check_direction(y, x, -1, 1, -6 + 1, 6, player, 6)

    def check_direction(self, x, y, dx, dy, a, b, player, m, t=True):
        board = self.board
        count = 0
        for i in range(a, b):
            r = x + dx * i
            c = y + dy * i

            if 0 <= r < len(board) and c >= 0 and c < len(board[x]) and board[r][c] == player:
                count += 1

                if count >= m:
                    return t

            else:
                count = 0
        return not t

    def check33(self,digit_board):
        for d in digit_board:
            for i in range(len(d)):
                if d[i] == '3':
                    d[i] = ' '

        for x, row in enumerate(digit_board):
            for y, col in enumerate(digit_board):
                if digit_board[x][y] == ' ':
                    self.get_real_direction(digit_board, x, y)
        return digit_board

    def get_real_direction(self,digit_board, x, y):
        direction = [(1, 0),
                     (0, 1),
                     (1, 1),
                     (-1, 1), ]
        real_direction = [[], [], [], []]
        digit_board[x][y] = 'b'
        for d in direction:
            for i in range(-4, 5):
                r = x + d[0] * i
                c = y + d[1] * i
                if 0 <= r < len(digit_board) and 0 <= c < len(digit_board[x]):
                    real_direction[direction.index(d)].append(digit_board[r][c])

        digit_board[x][y] = ' '

        if self.check22(real_direction, x, y) > 1:
            digit_board[x][y] = '3'
            return digit_board


    def check22(self,real_direction, x, y):
        trips_count = 0

        updated_direction = []
        for d in real_direction:
            updated_d = list(d)

            try:
                updated_d[0] = ' '
                updated_d[-1] = ' '
            except:
                pass
            for i in range(len(updated_d)):
                if updated_d[i] == '3':
                    updated_d[i] = ' '

            idx = [x[0] for x in enumerate(updated_d) if x[1] == 'b']

            if updated_d[0] == 'w' and updated_d[-1] == 'w':
                updated_d.clear()

            try:
                for r in range(1, len(updated_d) - 1):
                    if updated_d[r] == 'b' and (updated_d[r - 1] == 'w' or updated_d[r + 1] == 'w'):
                        updated_d.clear()
            except:
                pass

            if updated_d.count('b') == 3 and (updated_d[idx[0]:(idx[-1] + 1)]).count(' ') <= 1:
                trips_count += 1

            updated_direction.append(''.join(updated_d))

        return trips_count

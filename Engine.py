
from icecream import ic


class GomokuFish:
    def get_move(self, digit_board, x, y) -> object:
        self.digit_board = digit_board
        return self.get_normal_move()

    def get_normal_move(self):
        ic(self.digit_board)
        board = self.digit_board
        for line in board:
            for square in line:
                if square == 'b':
                    ic(square)
                    self.x = line.index(square) + 1
                    self.y = board.index(line) + 1
                    x = self.x
                    y = self.y
                    ic(x,y)
                    return (x, y)





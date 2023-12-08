from tkinter.messagebox import askyesno, showinfo

import gomoku.start as start

if __name__ == '__main__':
    run = True
    while run:
        want_to_play_more = 1
        black_white = 1 

        game = start.Game()
        game.run()

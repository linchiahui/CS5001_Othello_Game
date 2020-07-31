from config import WHITE, BLACK
import random as rnd
import time

SIMULATE_MOUSECLICK = 100


class Computer():
    def __init__(self, cur_board):
        self.board = cur_board

    def behavior(self):
        if self.board.turn == WHITE:
            self.board.get_valid_place(self.board.turn)
            if self.board.valid_move:
                print("AlphaGO is thinking...")
                time.sleep(0.6)
                self.com_move = rnd.choice(self.board.valid_move)
                print("AlphaGO places ", self.com_move)
                pos_x = self.com_move[0] * SIMULATE_MOUSECLICK
                pos_y = self.com_move[1] * SIMULATE_MOUSECLICK
                self.board.place(pos_y, pos_x)

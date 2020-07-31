from board import Board
from game_controller import GameController
from com import Computer
from config import WIDTH, HEIGHT
from score import Score
import time


game_controller = GameController(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT, game_controller)
com = Computer(board)
score = Score(board)



def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 255)
    
    answer = input('enter your name')
    if answer:
        print('hi ' + answer + ', could you beat me?')
    else:
        print('Could you beat me?')
        
    score.record_name(answer)


def draw():
    # show the background with deep green
    background(25, 100, 25)
    
    # show the line with board
    for x in range(100, WIDTH, 100):
        line(x, 0, x, 800)
        strokeWeight(3)
    for y in range(100, HEIGHT, 100):
        line(0, y, 800, y)
        strokeWeight(3)
    
    # show the discs on board
    board.display()
    game_controller.update()
    com.behavior()
    
    if game_controller.black_wins or game_controller.white_wins or game_controller.tie:
        score.record_winner()
  

def mousePressed(): 
    board.place(mouseX, mouseY)
 

def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

### File name => board.py
""" This is docstring """

#import sys
import os
from time import sleep
import numpy as np
from arts import Arts
from scenes import SceneGenerator
from variables import Vars


class Board():
    """_manage the Background _of Game """
    def __init__(self):
        """ This is docstring """
        self._spacing = 5      # For Score Board
        self._padding = 10      # For Score Board
        self._scn_gen = SceneGenerator()
        self._arts = Arts()
        self._vars = Vars()

    def draw(self, fin_matrix, score, life, time):
        """ This is docstring """
        score_board = self._padding * ' '
        score_board += "_mario Score: "
        score_board += str(score)
        score_board += self._spacing * ' '
        score_board += "Life: " + str(life)
        score_board += self._spacing * ' '
        score_board += "Time: " + str(time)

        print(score_board)
        print('\n'.join(''.join(str(cell) for cell in row) for row in fin_matrix))
#        np.savetxt(sys.stdout.buffer, fin_matrix, fmt='%0c')

    def game_over(self):
        """ This is docstring """
        lengthgth = self._vars.get_height()
        breath = self._vars.get_width_of_patch() * self._vars.get_mult_patches()
        length, bre = self._arts.get_game_over_dim()
#        pad = int (breath - b / 2)
        pad = 10
        dim = 0
        while dim < lengthgth - length - 5:
            bckgnd = np.full((lengthgth, breath), '.')
            bckgnd[dim:dim + length, pad:pad + bre] = self._arts.get_game_over()
            print('\n'.join(''.join(str(cell) for cell in row) for row in bckgnd))
            sleep(1/15)
            os.system('cls' if os.name == 'nt'
                      else 'clear')   # Clearing the terminal after every 0.1 sec
            if dim == lengthgth - length - 6:
                dim = 0
            dim += 1

    def winner(self):
        """ This is docstring """
        lengthgth = self._vars.get_height()
        breath = self._vars.get_width_of_patch() * self._vars.get_mult_patches()
        length, bre = self._arts.get_winner_dim()
#        pad = int (breath - b / 2)
        pad = 10
        dim = 0
        while dim < lengthgth - length - 5:
            bckgnd = np.full((lengthgth, breath), '.')
            bckgnd[dim:dim + length, pad:pad + bre] = self._arts.get_winner()
            print('\n'.join(''.join(str(cell) for cell in row) for row in bckgnd))
            sleep(1/15)
            os.system('cls' if os.name == 'nt'
                      else 'clear')   # Clearing the terminal after every 0.1 sec
            if dim == lengthgth - length - 6:
                dim = 0
            dim += 1


#brd = Board()
#while(True):
#    os.system('cls' if os.name=='nt' else 'clear')
#    brd.draw()

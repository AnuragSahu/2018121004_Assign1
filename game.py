#!/usr/bin/python3 game.py
""" This is the main Game.py file"""
import os
import time
import signal
from subprocess import call
from board import Board
from char_scan import CharScan
from alarmexception import AlarmException
from controls import ControlCenter


CHAR_SCANNER = CharScan()

def chk_input(timeout=1):
    """ This function checks for imput"""
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.setitimer(signal.ITIMER_REAL, timeout)
    start_time = time.time()
    try:
        char_input = CHAR_SCANNER()
        signal.alarm(0)
        end_time = time.time()
        while end_time-start_time < 1/20:
            end_time = time.time()
        return char_input
    except AlarmException:
        print(end='')
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

def alarm_handler(signum, frame):
    """ This function handles the alarm """
    raise AlarmException

def main():
    """ This function is called as soon as the python3 game.py is made to run"""
    #var = Vars()
    call(["xdg-open", "/home/anurag/HW/Assignment_1/sound.mp3"])
##        os.startfile("/home/anurag/HW/Assignment_1/sound.mp3")
    board_object = Board()
    cont = ControlCenter()
    score = 0
    tim = 0
    #art = Arts()
    jump_cordinate = 5
    life = 3
    game_win = 0
    way = ''
    while(life > 0 and game_win == 0):
        if tim < 60:  #Time before mario faces enemy
            final_matrix, jump_cordinate, life, score = cont.controls(way,
                                                                      jump_cordinate,
                                                                      life,
                                                                      score)  # Generating scenes
            if jump_cordinate != 5:
                jump_cordinate -= 1
                if jump_cordinate == -5:
                    jump_cordinate = 5
        else:
            final_matrix, jump_cordinate, life, game_win = cont.place_boss_enemy(way,
                                                                                 jump_cordinate,
                                                                                 life,
                                                                                 game_win)
            if game_win == 1:
                break
            if jump_cordinate != 5:
                jump_cordinate -= 1
                if jump_cordinate == -5:
                    jump_cordinate = 5



        score += 1
        tim += 1
        board_object.draw(final_matrix,
                          score,
                          life,
                          int(tim/16)) # Printing the Matrix in to Termial
        way = chk_input()
        os.system('cls' if os.name == 'nt'
                  else 'clear')   # Clearing the terminal after every 0.1 sec

    if game_win == 1:
        board_object.winner()

    board_object.game_over()
if __name__ == '__main__':
    main()

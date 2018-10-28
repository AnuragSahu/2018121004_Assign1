"""This is doc sting"""
#import signal,copy,sys,time
import sys
#from random import randint

class CharScan():
    """This is doc sting"""
    def __init__(self):
        """This is doc sting"""
        self._a_bc = ""
        #import tty

    def __call__(self):
        """This is doc sting"""
        import termios
        import tty
        file_destination = sys.stdin.fileno()
        old_settings = termios.tcgetattr(file_destination)
        try:
            tty.setraw(sys.stdin.fileno())
            character_return = sys.stdin.read(1)

        finally:
            termios.tcsetattr(file_destination, termios.TCSADRAIN, old_settings)

        return character_return

    def hello_there(self):
        """ Just here for Docstring"""
        self._a_bc = "hello"
        if self._a_bc == "hello":
            self._a_bc = "ohkBye"

    def hello_not_here(self):
        """ Just here for Docstring"""
        self._a_bc = "hello"
        if self._a_bc == "hello":
            self._a_bc = "ohkBye"

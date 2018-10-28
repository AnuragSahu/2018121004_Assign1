    # file name ->>  arts.py
"""_this is docstring"""
import numpy as np
from variables import Vars
class Arts():
    """_this is docstring"""
    def __init__(self):
        """_this is docstring"""
        self._small_cloud = np.array([[' ', '.', '-', '(', '`', ' ', ' ', ')', ' ', ' '],
                                      [':', '(', ' ', ' ', ' ', ' ', ' ', ' ', ')', ')'],
                                      ['`', '(', ' ', ' ', ' ', ' ', ')', ' ', ')', ')'],
                                      [' ', '`', ' ', '_', '_', '.', ':', '\'', ' ', ' ']
                                     ])



        self._bird = np.array([[' ', ' ', ' ', ' ', '_', ' ', ' ', ' '],
                               [' ', ' ', '>', '\'', 'o', ')', ' ', ' '],
                               ['/', '/', '/', '(', ' \\', '\\', ',\\', '\\']
                              ])

        self._tree = np.array([[' ', ' ', '/', '\\', ' ', ' '],
                               [' ', '/', '/', '\\', '\\', ' '],
                               ['/', '/', '/', '\\', '\\', '\\'],
                               ['/', '/', '/', '\\', '\\', '\\'],
                               ['/', '/', '/', '\\', '\\', '\\'],
                               ['/', '/', '/', '\\', '\\', '\\'],
                               [' ', ' ', '|', '|', ' ', ' '],
                               [' ', ' ', '|', '|', ' ', ' ']
                              ])

        self._cloud = np.array([list(r"     .-~~~-.       "),
                                list(r"  .-(       )_     "),
                                list(r" /             -.  "),
                                list(r"|                 \\"),
                                list(r" \               .'"),
                                list(r"   \___________.-  ")
                               ])

        self._pipe = np.array([['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
                               ['|', '_', ' ', ' ', ' ', ' ', ' ', ' ', '_', '|'],
                               [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' '],
                               [' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ']
                              ])

        self._mario = np.array([[' ', 'o', ' '],
                                ['/', '|', '\\'],
                                ['/', ' ', '\\']
                               ])

        self._super_mario = np.array([[' ', '_o', ' '],
                                      ['/', '|', '\\'],
                                      [' ', '|', ' '],
                                      ['/', ' ', '\\']
                                     ])

        self._enemy = np.array([[' ', '_', '_', '_', '_', ' '],
                                ['|', '|', '_o', '_o', '|', '|'],
                                ['(', '_', '_', '_', '_', ')']
                               ])

        self._game_over = np.array([list(r"  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______       __  "),
                                    list(r" /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     |  | "),
                                    list(r"|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    |  | "),
                                    list(r"|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     |  | "),
                                    list(r"|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--   |    \    /    |  |____ |  |\  \----.|__| "),
                                    list(r" \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|(__) "),
                                   ])
        self._winner = np.array([list(r"____    __    ____  __  .__   __. .__   __.  _______ .______      "),
                                 list(r"\   \  /  \  /   / |  | |  \ |  | |  \ |  | |   ____||   _  \     "),
                                 list(r" \   \/    \/   /  |  | |   \|  | |   \|  | |  |__   |  |_)  |    "),
                                 list(r"  \            /   |  | |  . `  | |  . `  | |   __|  |      /     "),
                                 list(r"   \    /\    /    |  | |  |\   | |  |\   | |  |____ |  |\  \----."),
                                 list(r"    \__/  \__/     |__| |__| \__| |__| \__| |_______|| _| `._____|"),
                                ])

        self._boss_enemy = np.array([list(r" <(__)> | | |"),
                                     list(r" | \/ | \_|_/"),
                                     list(r" \^  ^/   |  "),
                                     list(r" /\--/\  /|  "),
                                     list(r"/  \/  \/ |  ")
                                    ])

        self._bullet = np.array([list("<<<<")])

        self._vars = Vars()
        self._width = self._vars.get_width_of_patch()
        self._height = self._vars.get_height()

        self._gnd = np.full((3, self._width), '_t')
        self._hole_gnd = np.full((3, self._width), '_t')
        self._hole_gnd [:, 8:14] = ' '

        self._wall = np.chararray((3, 6))
        self._wall[:] = '_w'

        self._sur_wall = np.chararray((3, 6))
        self._sur_wall = '?'

    def get_winner_dim(self):
        """_this is docstring"""
        return self._winner.shape

    def get_winner(self):
        """_this is docstring"""
        return self._winner

    def get_bullet_dim(self):
        """_this is docstring"""
        return self._bullet.shape

    def get_bullet(self):
        """_this is docstring"""
        return self._bullet

    def get_boss_enemy_dim(self):
        """_this is docstring"""
        return self._boss_enemy.shape

    def get_boss_enemy(self):
        """_this is docstring"""
        return self._boss_enemy

    def get_cloud(self):
        """_this is docstring"""
        return self._cloud

    def get_cloud_dim(self):
        """_this is docstring"""
        return self._cloud.shape

    def get_small_cloud(self):
        """_this is docstring"""
        return self._small_cloud

    def get_small_cloud_dim(self):
        """_this is docstring"""
        return self._small_cloud.shape

    def get_pipe_dim(self):
        """_this is docstring"""
        return self._pipe.shape

    def get_pipe(self):
        """_this is docstring"""
        return self._pipe

    def get_mario(self):
        """_this is docstring"""
        return self._mario

    def get_mario_dim(self):
        """_this is docstring"""
        return self._mario.shape

    def get_super_mario_dim(self):
        """_this is docstring"""
        return self._super_mario.shape

    def get_super_mario(self):
        """_this is docstring"""
        return self._super_mario

    def get_gnd(self):
        """_this is docstring"""
        return self._gnd

    def get_wall_dim(self):
        """_this is docstring"""
        return self._wall.shape

    def get_wall(self):
        """_this is docstring"""
        return self._wall

    def get_sur_wall_dim(self):
        """_this is docstring"""
        return self._sur_wall.shape

    def get_sur_wall(self):
        """_this is docstring"""
        return self._sur_wall

    def get_enemy_dim(self):
        """_this is docstring"""
        return self._enemy.shape

    def get_enemy(self):
        """_this is docstring"""
        return self._enemy

    def get_hole_gnd(self):
        """_this is docstring"""
        return self._hole_gnd

    def get_tree_dim(self):
        """_this is docstring"""
        return self._tree.shape

    def get_tree(self):
        """_this is docstring"""
        return self._tree

    def get_bird_dim(self):
        """_this is docstring"""
        return self._bird.shape

    def get_bird(self):
        """_this is docstring"""
        return self._bird

    def get_game_over_dim(self):
        """_this is docstring"""
        return self._game_over.shape

    def get_game_over(self):
        """_this is docstring"""
        return self._game_over

#art = Arts()
#a= art.get_pipe()
#np.savetxt(sys.stdout.buffer,art.get_gnd(), fmt='%s', delimiter='')
#print(a.shape)

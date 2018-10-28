# file name => controls.py
"""This is docstring """

import random
import numpy as np
#from board import Board
from arts import Arts
from variables import Vars
from scenes import SceneGenerator, Scenes
from people import Enemy, Bullet

class ControlCenter():
    """This is docstring """
    def __init__(self):
        self._arts = Arts()
        self._vars = Vars()
        self._scn_gen = SceneGenerator()
        self._abv_gnd = 0
        self._e1 = Enemy()
        _, self._width = Scenes().get_init_dim()
        self._em = 0
        self._mario_place = 0
        self._b1 = Bullet()
        self._bsjump_cord = 20
        self._bsjump_corddef = self._bsjump_cord
        self._pipe_place = ((self._width * 4) - 10)
        #self._steps_taken_back = 0

    def controls(self, way, jump_cord, life, score):
        """This is docstring """
         #### Controls w -> jump  d -> forward   a -> back_wards
         #### _for nothing it return the same thing again

        self._abv_gnd = (5 - abs(jump_cord)) * 2
        if random.randint(0, 100) < 1:
            self._scn_gen.put_pipe()
        if way == 'd':
            moved_scene = self._scn_gen.move_forward_world_scene()
            self._pipe_place -= 3
        elif way == 'a':
            moved_scene = self._scn_gen.move_back_world_scene()
            self._pipe_place += 1
        elif way == 'w':
            moved_scene = self._scn_gen.ret_world()
            if jump_cord == 5:
                jump_cord -= 1
        else:
            moved_scene = self._scn_gen.ret_world()

        mario_placed = np.copy(moved_scene)

        mario_placed = self._scn_gen.put_mario(mario_placed, self._abv_gnd, 0)
        life = self.dist_mario_enemy(jump_cord, life)
#        if(self._pipe_place>0):
#            mario_placed = self.put_pipe(mario_placed,self._pipe_place-self._width)
        if(self._em == 0 and random.randint(0, 20) < 2):
            self._em = 1
            self._e1.set_alive()
            self._e1.set_enemy_place(self._width * 4 - 10)
        if self._em == 1:
            mario_placed, score = self.plce_enemy(mario_placed, score)
        return mario_placed, jump_cord, life, score

    def plce_enemy(self, enemy_less, score):
        """This is docstring """
        if self._e1.is_alive() == 0:
            return enemy_less
        self._e1.set_enemy_height(0)
        _, bre = self._arts.get_enemy_dim()
        if self._e1.get_flag():
            dist = self._width * self._vars.get_mult_patches() - bre - 2
            self._e1.set_enemy_place(dist)
        self._e1.set_enemy_place(self._e1.get_enemy_place() - 2)
        if self._e1.get_enemy_place() == 0:
            score += 10
            self._e1.die()

        if self._e1.get_enemy_place() > self._width:
            dist = self._e1.get_enemy_place() - 2
        else:
            dist = self._e1.get_enemy_place() + 3

        self._e1.set_enemy_place(dist)
        enemy_placed = self._scn_gen.put_enemy(enemy_less,
                                               self._e1.get_enemy_height(),
                                               dist)
        return enemy_placed, score

    def dist_mario_enemy(self, jump_cord, life):
        """This is docstring """
        dist = self._e1.get_enemy_place()
        if(jump_cord == 5 and dist == self._width):
            life -= 1
        if((jump_cord == -4 or jump_cord == -5) and
           (dist >= self._width - 3 and
            dist <= self._width + 3)):
            self._e1.die()
            self._em = 0
        return life


    def place_boss_enemy(self, way, jump_cord, life, game_win):
        """This is docstring """
        mario_above_ground = (5 - abs(jump_cord)) * 2
        boss_above_ground = (self._bsjump_corddef - abs(self._bsjump_cord))
        self._bsjump_cord -= 2
        if self._bsjump_cord < -self._bsjump_corddef:
            self._bsjump_cord = self._bsjump_corddef
        scene = np.copy(self._scn_gen.ret_world())
        if way == 'd':
            self._mario_place += 2
#            if(self._mario_place>= self._width*3):
#               game_win =1
#               return scene,jump_cord,life,game_win
            if self._mario_place + 5 > self._width * 3:
                return scene, jump_cord, life, 1

        elif way == 'a':
            self._mario_place -= 2
        elif way == 'w':
            if jump_cord == 5:
                jump_cord -= 1
        mario_placed = self._scn_gen.put_mario(scene,
                                               mario_above_ground,
                                               self._mario_place)
        mario_placed = self._scn_gen.put_boss_enemy(mario_placed,
                                                    boss_above_ground,
                                                    self._width * 3)
        if(self._b1.bltpst() == 0 and
           random.randint(0, 10) < 7 and
           boss_above_ground < 10):
            self._b1.fire(boss_above_ground, self._width * 3)
        if self._b1.bltpst() == 1:
            length, bre = self._b1.get_bullet_cor()
            self._b1.move_blt()
            mario_placed = self._scn_gen.put_bult(mario_placed, length, bre)
            if(mario_above_ground + 3 >= length and
               mario_above_ground <= length and
               self._mario_place + 3 <= bre and
               self._mario_place >= bre):
                life -= 1
        return mario_placed, jump_cord, life, game_win




#board_object = Board()

#cont = ControlCenter()
#fin_matrix = cont.controls('w')
#board_object.draw(fin_matrix,1,1,1)

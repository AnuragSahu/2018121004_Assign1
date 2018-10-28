# scenes.py
"""this is doc string"""

import random
import numpy as np
from arts import Arts
from variables import Vars

class Scenes():
    """this is doc String"""
    # All the _different components are here to set the
    # components like _trees and all to set into 20 * 22 matrix
    # called patch
    def __init__(self):
        """this is doc String"""
        self._vars = Vars()
        self._width = self._vars.get_width_of_patch()
        self._height = self._vars.get_height()
        self._space = np.full((self._height, self._width), ' ')
        self._asc = Arts()
        self._gnd_height = self._vars.get_height_of_ground()
        self._sift_pipe = 6
        self._sift_wall = 6
        self._wall_height = 5


    def get_init_dim(self):
        """this is doc String"""
        return self._space.shape

    def set_gnd(self):
        """this is doc String"""
        self._space[-self._gnd_height:, :] = self._asc.get_gnd()
        return self._space

    #def set_cloud(self, arr):
    #    """this is doc String"""
    #    length, bre = self._asc.get_cloud_dim()
    #    pdb = random.randint(0, self._width - bre)
    #    pdh = random.randint(0, self._height - length - self._gnd_height)
    #    arr[pdh:pdh + length, pdb:pdb + bre] = self._asc.get_cloud()
    #    return arr


    def set_pipe(self, arr):
        """this is doc String"""
        length, bre = self._asc.get_pipe_dim()
        arr[-(self._gnd_height + length):
            -(self._gnd_height),
            self._sift_pipe:
            self._sift_pipe + bre] = self._asc.get_pipe()
        return arr

    def set_mario(self):
        """this is doc String"""
        length, bre = self._asc.get_mario_dim()
        self._space[-(self._gnd_height + length):-(self._gnd_height), :bre] = self._asc.get_mario()

    def set_super_mario(self):
        """this is doc String"""
        length, bre = self._asc.get_super_mario_dim()
        self._space[-(self._gnd_height + length):
                    -(self._gnd_height), :bre] = self._asc.get_super_mario()

    def set_wall(self, arr):
        """this is doc String"""
        length, bre = self._asc.get_wall_dim()
        arr[-(self._gnd_height +
              self._wall_height +
              length):-(self._gnd_height +
                        self._wall_height), (self._sift_wall):(self._sift_wall +
                                                               bre)] = self._asc.get_wall()
        return arr

    def set_sur_wall(self, arr):
        """this is doc String"""
        length, bre = self._asc.get_wall_dim()
        arr[-(self._gnd_height +
              self._wall_height +
              length): - (self._gnd_height +
                          self._wall_height), (self._sift_wall):(self._sift_wall +
                                                                 bre)] = self._asc.get_sur_wall()
        return arr

    def set_enemy(self):
        """this is doc String"""
        length, bre = self._asc.get_enemy_dim()
        self._space[-(self._gnd_height + length):
                    -(self._gnd_height), -bre:] = self._asc.get_enemy()

    def set_hole_gnd(self, arr):
        """this is doc String"""
        arr[-self._gnd_height:, :] = self._asc.get_hole_gnd()
        return arr

    def set_tree(self, arr):
        """this is doc String"""
        length, bre = self._asc.get_tree_dim()
        arr[-(self._gnd_height + length):
            -(self._gnd_height),
            self._sift_pipe * 2:
            self._sift_pipe * 2 + bre] = self._asc.get_tree()
        return arr


    def set_small_cld(self, arr):
        """this is doc String"""
        length, bre = self._asc.get_small_cloud_dim()
        arr[:length, :bre] = self._asc.get_small_cloud()
        return arr


class SceneGenerator:
    """this is doc String"""
    # _has the components to render all the above
    # generated scenecs into one scene (_world scene of 22 * 80)
    # and display screen of 22 * 40
    def __init__(self):
        """this is doc String"""
        self._scn = Scenes()
        self._vars = Vars()
        self._height, self._width = self._scn.get_init_dim()
        self._show_width = self._width * self._vars.get_mult_patches()
        self._canvas = np.full((self._height, self._show_width), ' ')
        self._world = np.full((self._height, self._show_width * 2), ' ')
        self._gnd = self._scn.set_gnd()
        self._tree = self._scn.set_tree(np.copy(self._gnd))
        self._small_cld = self._scn.set_small_cld(np.copy(self._gnd))
        self._tree_cld = self._scn.set_tree(np.copy(self._small_cld))
        self._small_cld_tree = self._scn.set_small_cld(np.copy(self._tree))
        self._trans = 0
        self._stt = 0
        self._gnd_height = 3

        self._hol_gnd = self._scn.set_hole_gnd(np.copy(self._small_cld))
        self._hol = self._scn.set_hole_gnd(np.copy(self._gnd))
        self._pipe = self._scn.set_pipe(np.copy(self._gnd))
        self._pipe_cld = self._scn.set_small_cld(np.copy(self._small_cld))
        self.start_world_scene()

        self._arts = Arts()

    def first_scene(self):
        """this is doc String"""
        # _hard_coded _initial Scene
        blank = self._canvas
        blank[:, :self._width] = self._scn.set_small_cld(np.copy(self._scn.set_gnd()))
        blank[:,
              self._width:self._width *
              2] = self._scn.set_tree(np.copy(self._scn.set_gnd()))
        blank[:,
              self._width *
              2:self._width *
              3] = self._scn.set_small_cld(np.copy(self._scn.set_gnd()))
        blank[:,
              self._width *
              3:self._width *
              4] = self._scn.set_sur_wall(np.copy(self._scn.set_gnd()))
        return blank

    def give_patch(self):
        """this is doc String"""
        randon_int = random.randint(1, 10)
        return {
            1: self._small_cld,
            2: self._small_cld,
            3: self._tree,
            4: self._gnd,
            5: self._small_cld_tree,
            6: self._small_cld,
            7: self._small_cld_tree,
            8: self._small_cld,
            9: self._small_cld,
            10: self._small_cld}[randon_int]


#    def rand_scenes(self):
#        """this is doc String"""
#        blank = np.copy(self._canvas)
#        for i in range(4):
#            blank[:, self._width * i:self._width * (i + 1)] = self.give_patch()
#        return blank

#   def start_world_scene(self):
#       """this is doc String"""
#        self._world[:, :self._show_width] = self.first_scene()
#        self._world[:, self._show_width:self._show_width * 2] = self.rand_scenes()
#        return self._world

    def rand_scenes(self):
        """this is doc String"""
        blank = np.copy(self._canvas)
        for i in range(4):
            blank[:, self._width * i:self._width * (i + 1)] = self.give_patch()
        return blank

    def start_world_scene(self):
        """this is doc String"""
        self._world[:, :self._show_width] = self.first_scene()
        self._world[:, self._show_width:self._show_width * 2] = self.rand_scenes()
        return self._world

    def move_forward_world_scene(self):
        """this is doc String"""
        if self._stt == 20:
            self._world[:, :self._show_width + self._width * 3] = self._world[:, self._width:]
            self._world[:, self._show_width + self._width * 3:] = self.give_patch()
            self._stt = 0

        self._stt += 2
        return self._world[:, self._stt:self._show_width + self._stt]

    def move_back_world_scene(self):
        """this is doc String"""
        if self._stt == 0:
            return self.ret_world()

        self._stt -= 2
        return self._world[:, self._stt:self._show_width + self._stt]

    def ret_world(self):
        """this is doc String"""
        return self._world[:, self._stt:self._stt + self._show_width]

    def put_mario(self, tmp, hgh, place):
        """this is doc String"""
        length, bre = self._arts.get_mario_dim()
        tmp[-(self._gnd_height + hgh + length):
            -(self._gnd_height + hgh),
            self._width + place:bre + place +
            self._width] = self._arts.get_mario()
        return tmp

    def put_enemy(self, tmp, hgh, place):
        """this is doc String"""
        length, bre = self._arts.get_enemy_dim()
        tmp[-(self._gnd_height + hgh + length):
            -(self._gnd_height + hgh),
            place:bre + place] = self._arts.get_enemy()
        return tmp

    def put_boss_enemy(self, tmp, hgh, place):
        """this is doc String"""
        length, bre = self._arts.get_boss_enemy_dim()
        tmp[-(self._gnd_height + hgh + length):
            -(self._gnd_height + hgh),
            place:bre + place] = self._arts.get_boss_enemy()
        return tmp

    def put_bult(self, tmp, hgh, place):
        """this is doc String"""
        length, bre = self._arts.get_bullet_dim()
        tmp[-(self._gnd_height + hgh + length):
            -(self._gnd_height + hgh),
            place:place + bre] = self._arts.get_bullet()
        return tmp

    def put_pipe(self):
        """this is doc String"""
        length, bre = self._arts.get_pipe_dim()
        self._world[-(self._gnd_height + length):
                    -(self._gnd_height),
                    self._show_width:self._show_width + bre] = self._arts.get_pipe()

# file name variables.py
"""this is doc String"""
class Vars():
    """this is doc String"""
    def __init__(self):
        """this is doc String"""
        self._height = 42
        self._width_of_patch = 30
        self._height_of_ground = 3
        self._pad_from_above = 3
        self._mult_patches = 4

    def get_mult_patches(self):
        """this is doc String"""
        return self._mult_patches

    def get_height(self):
        """this is doc String"""
        return self._height

    def set_height(self, var):
        """this is doc String"""
        self._height = var

    def get_width_of_patch(self):
        """this is doc String"""
        return self._width_of_patch

    def set_width_of_patch(self, var):
        """this is doc String"""
        self._width_of_patch = var

    def get_height_of_ground(self):
        """this is doc String"""
        return self._height_of_ground

    def get_pad_from_above(self):
        """this is doc String"""
        return self._pad_from_above

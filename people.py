"""This is doc string"""
from abc import ABC, abstractmethod
from arts import Arts


class Person(ABC):
    """This is doc string"""
    def __init__(self):
        """Nothing"""

    @abstractmethod
    def move(self, dist_abc):
        """This is doc string"""
        # Lets to charcter to move
        pass

#    @abstractmethod
#    def attack(self):
        # Lets the character to attack if it can
#        pass

    @abstractmethod
    def die(self):
        """This is doc string"""
        # How the character dies
        pass

class Hero(Person):
    """This is doc string"""
    def __init__(self):
        self._lives = 3
        self._score = 0
        self._head = [' ', 'o', 'o', ' ']
        self._body = ['[', '|', '|', '}']
        self._legs = [' ', '}', '{', ' ']

        print(self._head)
        print(self._body)
        print(self._legs)

    def move(self, dist_abc):
        """This is doc string"""
        dist_abc = 0
        print(dist_abc)

 #   def attack(self):
 #       print("Attacking")

    def die(self):
        """This is doc string"""
        self._lives -= 1


class Enemy(Person):
    """This is doc string"""
    def __init__(self):
        self._lives = 1
        self._height_above_ground = 0
        self._place = 0
        self._arts = Arts()
        self._flg = 1

    def set_flag(self):
        """This is doc string"""
        return True

    def get_flag(self):
        """This is doc string"""
        if self._flg == 1:
            self._flg = 0
            return True
        return False

    def is_alive(self):
        """This is doc string"""
        return self._lives

    def set_alive(self):
        """This is doc string"""
        self._lives = 1

    def get_enemy_height(self):
        """This is doc string"""
        return self._height_above_ground

    def set_enemy_height(self, he_ht):
        """This is doc string"""
        self._height_above_ground = he_ht

    def get_enemy_place(self):
        """This is doc string"""
        return self._place

    def set_enemy_place(self, pls):
        """This is doc string"""
        self._place = pls

    def get_enemy_dim(self):
        """This is doc string"""
        return self._arts.get_enemy_dim

    def move(self, dist_abc):
        """This is doc string"""
        if dist_abc == "left":
            self._place = self._place - 2

        else:
            self._place = self._place + 2

#    def attack(self):

    def die(self):
        """This is doc string"""
        self._lives -= 1


class BossEnemy(Person):
    """This is doc string"""
    def __init__(self):
        self._lives = 3
        self._height_above_ground = 0
        self._place = 0
        self._arts = Arts()
        self._flg = 1
        self._bullet_pos = 0
        self._bullet_hgh = 3

    def move_bullet(self):
        """This is doc string"""
        self._bullet_pos -= 1

    def get_bullet_pos(self):
        """This is doc string"""
        return self._bullet_pos, self._bullet_hgh

    def set_bullet_hgh(self, hgh):
        """This is doc string"""
        self._bullet_hgh = hgh

    def set_flag(self):
        """This is doc string"""
        return True

    def get_flag(self):
        """This is doc string"""
        if self._flg == 1:
            self._flg = 0
            return True
        return False

    def is_alive(self):
        """This is doc string"""
        return self._lives

    def set_alive(self):
        """This is doc string"""
        self._lives = 1

    def get_enemy_height(self):
        """This is doc string"""
        return self._height_above_ground

    def set_enemy_height(self, high_gnd):
        """This is doc string"""
        self._height_above_ground = high_gnd

    def get_enemy_place(self):
        """This is doc string"""
        return self._place

    def set_enemy_place(self, pls):
        """This is doc string"""
        self._place = pls

    def get_enemy_dim(self):
        """This is doc string"""
        return self._arts.get_enemy_dim

    def move(self, dist_abc):
        """This is doc string"""
        if dist_abc == "left":
            self._place = self._place - 2

        else:
            self._place = self._place + 2

#    def attack(self):

    def die(self):
        """This is doc string"""
        self._lives -= 1


class Bullet():
    """This is doc string"""
    def __init__(self):
        """This is doc string"""
        self._hgh = 5
        self._place = 0
        self._pst = 0

    def fire(self, hgh, place):
        """This is doc string"""
        self._pst = 1
        self._hgh = hgh
        self._place = place

    def move_blt(self):
        """This is doc string"""
        self._place -= 1
        if self._place < 0:
            self._pst = 0

    def get_bullet_cor(self):
        """This is doc string"""
        return self._hgh, self._place

    def bltpst(self):
        """This is doc string"""
        return self._pst



#mario = Hero()
#mario.move()
#mario.attack()
#mario.die()

from vel import Vel
from math import cos, sin, pi


class Pos:
    bot = 0
    left = 0

    def __init__(self, left=0, bot=0):
        self.left = left
        self.bot = bot

    def __str__(self):
        return 'Pos(%.2f, %.2f)' % (self.left, self.bot)

    def __add__(self, v):
        if type(v) != Vel:
            return self
        p = Pos(self.left, self.bot)
        p.left += v.rate * cos(v.angle * pi / 180)
        p.bot += v.rate * sin(v.angle * pi / 180)
        return p

    def is_in(self, r):
        return self.left >= r.left and self.left <= r.left + r.width and \
                self.bot >= r.bot and self.bot <= r.bot + r.height

    def is_on_edge(self, r):
        return self.left == r.left or self.left == r.left + r.width or \
                self.bot == r.bot or self.bot == r.bot + r.height

    def mid_pos(self, p):
        return Pos((self.left + p.left) / 2, (self.bot + p.bot) / 2)

from pos import Pos


class Rct(Pos):  # rectangle
    width = 0
    height = 0

    def __init__(self, left=0, bot=0, width=0, height=0):
        self.left = left
        self.bot = bot
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rct(%.2f, %.2f, %.2f, %.2f)' % (self.left, self.bot, self.width, self.height)

    def include(self, p):
        return p.is_in(self)

    def is_on_edge(self, p):
        return p.is_on_edge(self)

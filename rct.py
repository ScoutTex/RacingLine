from pos import Pos
from vel import Vel


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

    def crush_hline(self, hp0, hp1, p0, p1):
        if p0.bot == p1.bot:
            return (p0.bot == hp0.bot
                    and p0.left <= hp1.left
                    and p1.left >= hp0.left)
        x = p0.left + (hp0.bot - p0.bot) * (p1.left - p0.left) / (p1.bot - p0.bot)
        return (x >= hp0.left and x <= hp1.left)

    def crush_vline(self, vp0, vp1, p0, p1):
        hp0 = Pos(vp0.bot, vp0.left)
        hp1 = Pos(vp1.bot, vp1.left)
        p0_ = Pos(p0.bot, p0.left)
        p1_ = Pos(p1.bot, p1.left)
        return self.crush_hline(hp0, hp1, p0_, p1_)

    def crush(self, p0, p1):
        if type(p1) == Vel:
            p1 = p0 + p1
        pld = Pos(self.left, self.bot)
        prd = Pos(self.left + self.width, self.bot)
        plu = Pos(self.left, self.bot + self.height)
        pru = Pos(self.left + self.width, self.bot + self.height)
        return (self.crush_hline(pld, prd, p0, p1)
                or self.crush_hline(plu, pru, p0, p1)
                or self.crush_vline(pld, plu, p0, p1)
                or self.crush_vline(prd, pru, p0, p1))

class Pos:
    bot = 0
    left = 0

    def __init__(self, left=0, bot=0):
        self.left = left
        self.bot = bot

    def __str__(self):
        return 'Pos(%.2f, %.2f)' % (self.left, self.bot)

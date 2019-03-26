class Pos:
    bot = 0
    left = 0
    def __init__(self, left=0, bot=0):
        self.left = left
        self.bot = bot
    def __str__(self):
        return 'Pos(%.2f, %.2f)'%(self.left, self.bot)

class Rct(Pos): #rectangle
    width = 0
    height = 0
    def __init__(self, left=0, bot=0, width=0, height=0):
        self.left = left
        self.bot = bot
        self.width = width
        self.height = height
    def __str__(self):
        return 'Rct(%.2f, %.2f, %.2f, %.2f)'%(self.left, self.bot, self.width, self.height)


class Track:
    race_area = Rct()
    start_point = Pos()
    goal_area = Rct()
    barriers = []

    def read(self, file):
        with open(file, 'r') as f:
            self.race_area.width, self.race_area.height = [int(x) for x in next(f).split()]
            self.start_point.left, self.start_point.bot = [int(x) for x in next(f).split()]
            self.goal_area.left, self.goal_area.bot, self.goal_area.width, self.goal_area.height = [int(x) for x in next(f).split()]
            barrier_lines = int(next(f))
            self.barriers.clear()
            for _ in range(barrier_lines):
                temp = Rct()
                temp.left, temp.bot, temp.width, temp.height = [int(x) for x in next(f).split()]
                self.barriers.append(temp)

    def __init__(self, track_file=''):
        self.race_area.left = 0
        self.race_area.bot = 0
        if len(track_file) > 1:
            self.read(track_file)

    def __str__(self):
        s = ''
        s += 'race area: ' + self.race_area.__str__() + '\n'
        s += 'start point: ' + self.start_point.__str__() + '\n'
        s += 'goal area: ' + self.goal_area.__str__() + '\n'
        s += 'barriers:\n'
        for barrier in self.barriers:
            s += '    ' + barrier.__str__() + '\n'
        return s

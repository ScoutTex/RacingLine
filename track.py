from pos import Pos
from rct import Rct


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

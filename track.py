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
        s += '=== Track Object ===\n'
        s += 'race area: ' + str(self.race_area) + '\n'
        s += 'start point: ' + str(self.start_point) + '\n'
        s += 'goal area: ' + str(self.goal_area) + '\n'
        s += 'barriers:\n'
        for i in range(len(self.barriers)):
            s += '    %d: %s' % (i, str(self.barriers[i]))
        for barrier in self.barriers:
            s += '    ' + str(barrier) + '\n'
        return s

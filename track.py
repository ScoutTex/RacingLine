from pos import Pos
from rct import Rct
from vel import Vel
import math


class Track:
    race_area = Rct()
    start_point = Pos()
    goal_area = Rct()
    barriers = []

    def is_track_file(self, track_file):
        if track_file[-3:] != '.tk':
            print('ERROR: wrong track file format, should be *.tk')
            return False
        else:
            return True

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
        if self.is_track_file(track_file):
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

    def race(self, rl):
        p = Pos(self.start_point.left, self.start_point.bot)
        v = Vel(rl.start.rate, rl.start.angle)
        p.left += v.rate * math.cos(v.angle * math.pi / 180)
        p.bot += v.rate * math.sin(v.angle * math.pi / 180)
        step_cnt = 1
        goal_cnt = -1
        for s in rl.steps:
            v += s
            p.left += v.rate * math.cos(v.angle * math.pi / 180)
            p.bot += v.rate * math.sin(v.angle * math.pi / 180)
            if p.is_in(self.goal_area):
                goal_cnt = step_cnt
                break
            p_last = Pos(p.left, p.bot)
            step_cnt += 1
        if goal_cnt == -1:
            return -1
        sum = float(goal_cnt)
        step_length = 1 / 2
        if p.is_on_edge(self.goal_area):
            return sum
        p0 = Pos(p_last.left, p_last.bot)
        p1 = Pos(p.left, p.bot)
        for _ in range(30):
            pm = p0.mid_pos(p1)
            if pm.is_on_edge(self.goal_area):
                return sum - step_length
            step_length /= 2
            if pm.is_in(self.goal_area):
                p1 = Pos(pm.left, pm.bot)
                sum -= step_length
            else:
                p0 = Pos(pm.left, pm.bot)
        return sum

from vel import Vel


class Racingline:
    step = []

    def read(self, file):
        with open(file, 'r') as f:
            t = [int(x) for x in next(f).split()]
            self.start = Vel(t[0], t[1])
            steps = int(next(f))
            for _ in range(steps):
                t = [int(x) for x in next(f).split()]
                self.step.append(Vel(t[0], t[1]))

    def __init__(self, racingline_file=''):
        if len(racingline_file) > 1:
            self.read(racingline_file)
        else:
            self.start = Vel(0, 0)
            self.step = []

    def __str__(self):
        s = ''
        s += '=== Racingline Object ===\n'
        s += 'start: %s\n' % str(self.start)
        s += 'steps: %d\n' % len(self.step)
        for i in range(len(self.step)):
            s += '    %d: %s\n' % (i, str(self.step[i]))
        return s

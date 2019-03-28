from vel import Vel


class Racingline:
    steps = []

    def is_racingline_file(self, racingline_file):
        if racingline_file[-3:] != '.rl':
            print('ERROR: wrong racingline file format, should be *.rl')
            return False
        else:
            return True

    def read(self, file):
        with open(file, 'r') as f:
            t = [int(x) for x in next(f).split()]
            self.start = Vel(t[0], t[1])
            steps = int(next(f))
            for _ in range(steps):
                t = [int(x) for x in next(f).split()]
                self.steps.append(Vel(t[0], t[1]))

    def __init__(self, racingline_file=''):
        if self.is_racingline_file(racingline_file):
            self.read(racingline_file)
        else:
            self.start = Vel(0, 0)
            self.steps = []

    def __str__(self):
        s = ''
        s += '=== Racingline Object ===\n'
        s += 'start: %s\n' % str(self.start)
        s += 'steps: %d\n' % len(self.steps)
        for i in range(len(self.steps)):
            s += '    %d: %s\n' % (i, str(self.steps[i]))
        return s

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
        if type(racingline_file) is str and self.is_racingline_file(racingline_file):
            self.read(racingline_file)
        elif type(racingline_file) is Racingline:
            self.copy(racingline_file)
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

    def copy(self, rl):
        self.start = Vel(rl.start.rate, rl.start.angle)
        self.steps = []
        for i in range(len(rl.steps)):
            self.steps.append(Vel(rl.steps[i].rate, rl.steps[i].angle))

class RacingResult():
    def __init__(self, tk, rl):
        self.track = tk
        self.racingline = rl
        self.time = 0
        self.finished = False

    def race(self):
        [self.time, self.finished] = self.track.race(self.racingline)

    def __eq__(self, rr):
        if self.time != rr.time:
            return False
        for i in range(int(self.time)):
            if self.racingline.steps[i] != rr.racingline.steps[i]:
                return False
        return True

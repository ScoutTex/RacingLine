from pos import Pos


class Racingline:
    start_speed = 0
    start_angle = 0
    step = []

    def read(self, file):
        with open(file, 'r') as f:
            self.start_speed, self.start_angle = 
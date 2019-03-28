class Vel:  # velocity
    rate = 0
    angle = 0

    def __init__(self, rate=0, angle=0):
        self.rate = rate
        self.angle = angle

    def __str__(self):
        return "Vel(%.2f, %.2f)" % (self.rate, self.angle)

    def __add__(self, v1):
        self.rate += v1.rate
        self.angle += v1.angle

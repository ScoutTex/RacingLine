class Vel:  # velocity
    rate = 0
    angle = 0
    
    def __init__(self, rate=0, angle=0):
        self.rate = rate
        self.angle = angle
    
    def __str__(self):
        return "Vel(%.2f, %.2f)" % (self.rate, self.angle)

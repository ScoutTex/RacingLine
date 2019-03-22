class Pos:
    top = 0
    left = 0
    def __init__(self, left = 0, top = 0):
        self.left = left
        self.top = top
        
class Rct(Pos): #rectangle
    width = 0
    height = 0
    def __init__(self, left = 0, top = 0, width = 0, height = 0):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

class track:
    race_area = Rct()
    start_point = Pos()
    goal_area = Rct()
    barriers = []

    def read(self, file):
        with open(file, 'r') as f:
            self.race_area.width, self.race_area.height = [int(x) for x in next(f).split()]
            self.start_point.left, self.start_point.top = [int(x) for x in next(f).split()]
            self.goal_area.left, self.goal_area.top, self.goal_area.width, self.goal_area.height = [int(x) for x in next(f).split()]
            barrier_lines = int(next(f))
            self.barriers.clear()
            for _ in range(barrier_lines):
                temp = Rct()
                temp.left, temp.top, temp.width, temp.height = [int(x) for x in next(f).split()]
                self.barriers.append(temp)
    
    def __init__(self):
        self.race_area.left = 0
        self.race_area.top = 0
        
    def __str__(self):
        s = ''
        s += 'race area: ' + self.race_area.width + '* ' + self.race_area.height + '\n'
        s += 'start point: ' + self.start_point.left + ', ' + self.start_point.top + '\n'
        s += 'goal area: (' + self.goal_area.left + ', ' + self.goal_area.top + ', ' + self.goal_area.width + ', ' + self.goal_area.height + ')\n'
        s += 'barriers:\n'
        for bar in self.barriers:
            s += '    (' + bar.left + ', ' + bar.top + ', ' + bar.width + ', ' + bar.height + ')\n'

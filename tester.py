from pos import Pos
from vel import Vel
from rct import Rct
from track import Track
from drawer import Drawer
from racingline import Racingline


 
# d = Drawer(Track('tracks/simple_straight/simple_straight.tk'), [Racingline('tracks/simple_straight/rl01.rl')])
# d.draw()

# tk = Track('tracks/simple_straight/simple_straight.tk')
# rl = Racingline('tracks/simple_straight/rl01.rl')
# print(tk.race(rl))

r = Rct(200,100,300,300)
p0 = Pos(100,200)
p1 = Pos(300, 1)

print(r.crush(p0,p1))
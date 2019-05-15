from pos import Pos
from vel import Vel
from rct import Rct
from track import Track
from drawer import Drawer
from racingline import Racingline
from evolutioner import Evolutioner



# d = Drawer(Track('tracks/simple_straight/simple_straight.tk'), [Racingline('tracks/simple_straight/rl01.rl')])
# d.draw()

tk = Track('tracks/simple_straight/simple_straight.tk')
rl = Racingline('tracks/simple_straight/rl01.rl')
# print(tk.race(rl))
# 
# d = Drawer(tk, [rl])
# d.draw()

rls = Evolutioner.evolution(rl)


for rl in rls:
    print(rl)
    print(tk.race(rl))
print(rls)

d = Drawer(tk, rls)
d.draw()
from track import Track
from drawer import Drawer
from racingline import Racingline

d = Drawer(Track('tracks/simple_straight/simple_straight.tk'), [Racingline('tracks/simple_straight/rl01.rl')])
d.draw()

from pos import Pos
from vel import Vel
from rct import Rct
from track import Track
from drawer import Drawer
from racingline import Racingline
from evolutioner import Evolutioner


tk = Track('tracks/simple_straight/simple_straight.tk')
rl = Racingline('tracks/simple_straight/rl01.rl')

rls = [rl]
for i in range(100):
    rls = Evolutioner.evolution(rls)
    results = []
    for rl in rls:
        result = tk.race(rl)
        if not result[0]:
            continue
        else:
            results.append([result, rl])
    results.sort(key=lambda x: x[0][0])
    if len(results) > 100:
        results = results[:100]
    rls.clear()
    for result in results:
        rls.append(result[1])
    
    print('generation: %3d, best time: %5.2f' % (i, results[0][0][0]))

d = Drawer(tk, rls)
d.draw()
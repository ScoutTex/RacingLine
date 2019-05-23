from track import Track
from drawer import Drawer
from racingline import Racingline
from evolutioner import Evolutioner
from racingresult import RacingResult


def main():
    # tk = Track('tracks/simple_straight/simple_straight.tk')
    # rl = Racingline('tracks/simple_straight/rl01.rl')
    # tk = Track('tracks/simple_90/simple_90.tk')
    # rl = Racingline('tracks/simple_90/rl01.rl')
    tk = Track('tracks/simple_90_narrow/simple_90_narrow.tk')
    rl = Racingline('tracks/simple_90_narrow/rl01.rl')

    # d = Drawer(tk, [rl])
    # d.draw()

    rls = [rl]
    evolution_generation_cnt = 1200
    for generation in range(evolution_generation_cnt):
        rls = Evolutioner.evolution(rls)
        results = []
        for rl in rls:
            res = RacingResult(tk, rl)
            res.race()
            if not res.finished:
                continue
            else:
                results.append(res)
        results.sort(key=lambda x: x.time)
        j = 1
        while True:
            if j >= len(results):
                break
            elif results[j] == results[j-1]:
                del results[j]
            else:
                j += 1
        if generation < 500:
            max_len = 1
        elif generation < 800:
            max_len = 2
        elif generation < 1000:
            max_len = 5
        elif generation < 1100:
            max_len = 10
        elif generation < 1150:
            max_len = 20
        else:
            max_len = 50
        if len(results) > max_len:
            results = results[:max_len]
        rls.clear()
        for res in results:
            rls.append(res.racingline)

        print('generation: %4d, best time: %7.3f' % (generation, results[0].time))

    d = Drawer(tk, rls[:1])
    d.draw()


if __name__ == '__main__':
    main()

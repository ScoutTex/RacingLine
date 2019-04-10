from racingline import Racingline
from random import randrange, uniform


class Evolutioner:
    @staticmethod
    def evolution(rl, grow_ratio=5, max_d_rate=1, max_d_angle=10):
        rls = []
        if type(rl) is list:
            for rl0 in rl:
                rl0_s = Evolutioner.evolution(rl0)
                for rl0_s_ in rl0_s:
                    rls.append(rl0_s_)
        elif type(rl) is Racingline:
            rls.append(rl)
            for _ in range(grow_ratio):
                rl1 = Racingline(rls[0])
                change_step = randrange(len(rl.steps))
                change_rate = bool(randrange(2))
                if change_rate:
                    rate = rl1.steps[change_step].rate
                    rate += uniform(-max_d_rate, max_d_rate)
                    # rate += randrange(-max_d_rate, max_d_rate, 1/1000)
                    if rate > max_d_rate:
                        rate = max_d_rate
                    if rate < -max_d_rate:
                        rate = -max_d_rate
                    rl1.steps[change_step].rate = rate
                else:  # change angle
                    angle = rl1.steps[change_step].angle
                    angle += uniform(-max_d_angle, max_d_angle)
                    # angle += randrange(-max_d_angle, max_d_angle, 1/100)
                    if angle > max_d_angle:
                        angle = max_d_angle
                    if angle < -max_d_angle:
                        angle = -max_d_angle
                    rl1.steps[change_step].angle = angle
                rls.append(rl1)
        return rls

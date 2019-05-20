from racingline import Racingline
from random import randrange, uniform


class Evolutioner:
    @staticmethod
    def evolution_list(rls_raw, grow_ratio=5, max_d_rate=1, max_d_angle=10):
        rls = []
        for rl_raw in rls_raw:
            rl_raw_evo = Evolutioner.evolution(rl_raw, grow_ratio, max_d_rate, max_d_angle)
            for rl_raw_evo0 in rl_raw_evo:
                rls.append(rl_raw_evo0)
        return rls

    @staticmethod
    def evolution(rl, grow_ratio=5, max_d_rate=1, max_d_angle=10):
        rls = []
        if type(rl) is list:
            rls = Evolutioner.evolution_list(rl, grow_ratio, max_d_rate, max_d_angle)
        elif type(rl) is Racingline:
            rls.append(rl)
            for _ in range(grow_ratio):
                rl1 = Racingline(rls[0])
                rl2 = Racingline(rls[0])
                change_step = randrange(len(rl.steps))
                # change both rate and angle in same step
                # change_rate = bool(randrange(2))
                # change rate
                rate = rl1.steps[change_step].rate
                rate += uniform(-max_d_rate, max_d_rate)
                if rate > max_d_rate:
                    rate = max_d_rate
                if rate < -max_d_rate:
                    rate = -max_d_rate
                rl1.steps[change_step].rate = rate
                rls.append(rl1)
                # change angle
                angle = rl2.steps[change_step].angle
                angle += uniform(-max_d_angle, max_d_angle)
                if angle > max_d_angle:
                    angle = max_d_angle
                if angle < -max_d_angle:
                    angle = -max_d_angle
                rl2.steps[change_step].angle = angle
                rls.append(rl2)
        return rls

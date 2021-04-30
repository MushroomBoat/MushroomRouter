from utils import *
import math
import numpy as np


class Foil:
    coefficient = 0
    twaMin = 0
    twaMax = 0
    twaMerge = 0
    twsMin = 0
    twsMax = 0
    twaMerge = 0
    twsMerge = 0
    speedRatio = 0

    def foiling_factor(self, tws, twa):
        speed_steps = [0, self.twsMin - self.twsMerge, self.twsMin, self.twsMax, self.twsMax + self.twsMerge, math.inf]
        twa_steps = [0, self.twaMin - self.twaMerge, self.twaMin, self.twaMax, self.twaMax + self.twaMerge, math.inf]
        foil_mat = [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, self.speedRatio, self.speedRatio, 1, 1],
            [1, 1, self.speedRatio, self.speedRatio, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]]
        return interp2d_linear(twa, tws, twa_steps, speed_steps, foil_mat)






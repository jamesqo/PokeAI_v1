import math

class Stats(object):
    def __init__(self,
                 base_stats,
                 level,
                 nature,
                 ivs,
                 evs):
        self.base_stats = base_stats
        self.level = level
        self.nature = nature
        self.ivs = ivs
        self.evs = evs

        self._nature_array = nature.toarray()

    def __getitem__(self, index):
        # Formulas come from https://bulbapedia.bulbagarden.net/wiki/Statistic#In_Generation_III_onward
        if index == 0:
            return self.max_hp
        elif index == 1:
            return self.attack
        elif index == 2:
            return self.defense
        elif index == 3:
            return self.sp_attack
        elif index == 4:
            return self.sp_defense
        elif index == 5:
            return self.speed
        
        raise IndexError(f"Index out of range: {index}")

    @property
    def max_hp(self):
        # TODO: Do we have to account for Shedinja here?
        base, iv, ev = self.base_stats[0], self.ivs[0], self.evs[0]
        num = 2 * base + iv + math.floor(ev / 4)
        denom = 100
        return math.floor(num / denom) + self.level + 10

    @property
    def attack(self):
        return self._calc_stat(1)

    @property
    def defense(self):
        return self._calc_stat(2)

    @property
    def sp_attack(self):
        return self._calc_stat(3)

    @property
    def sp_defense(self):
        return self._calc_stat(4)

    @property
    def speed(self):
        return self._calc_stat(5)

    def _calc_stat(self, index):
        assert index != 0
        base, iv, ev = self.base_stats[index], self.ivs[index], self.evs[index]
        num = 2 * base + iv + math.floor(ev / 4)
        denom = 100
        return math.floor((math.floor(num / denom) + 5) * self._nature_array[index])

from party import Party

class Player(object):
    def __init__(self, mon_0, mon_1, mon_2, mon_3, mon_4, mon_5):
        self.mon_0 = mon_0
        self.mon_1 = mon_1
        self.mon_2 = mon_2
        self.mon_3 = mon_3
        self.mon_4 = mon_4
        self.mon_5 = mon_5

        self.party = Party([mon_0,
                            mon_1,
                            mon_2,
                            mon_3,
                            mon_4,
                            mon_5])

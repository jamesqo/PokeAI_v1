class Party(object):
    def __init__(self, mons):
        self.mons = mons

    def __getitem__(self, index):
        return self.mons[index]

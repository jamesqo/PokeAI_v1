from stats import Stats

class Pokemon(object):
    def __init__(self, species, level, nature, ivs, evs, ability, current_hp, status):
        self.species = species
        self.ability = ability
        self.stats = Stats(lookup_base_stats(species),
                           level=level,
                           nature=nature,
                           ivs=ivs,
                           evs=evs)
        self.current_hp = current_hp
        self.status = status

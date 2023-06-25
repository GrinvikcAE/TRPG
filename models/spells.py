class Spell:

    def __init__(self, name, description: str = '', heal_amount: int = 0,
                 damage_amount: int = 0, type_spell='', vampiric=False):
        self.type = 'Spell'
        self.name = name
        self.description = description
        self.heal_amount = heal_amount
        self.damage_amount = damage_amount
        self.type_spell = type_spell
        self.vampiric = vampiric

    def __setattr__(self, key: str, value):
        self.__dict__[key] = value

    def save(self):
        return self.__dict__

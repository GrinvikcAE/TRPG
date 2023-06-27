class Creatures:
    def __init__(self):
        self.type = 'Creature'

    class Alive:

        def __init__(self, name: str, level: int = 1, strength: int = 1, agility: int = 1, intelligence: int = 1,
                     wisdom: int = 1, shield: int = 0, current_hp: int = 100, armor: int = 0, spells=None,
                     inventory=None, npc: bool = False, god: bool = False, enemy: bool = False, dead: bool = False):
            if spells is None:
                spells = []
            self.type = 'Alive'
            self.name = name
            self.level = level
            self.strength = strength
            self.agility = agility
            self.intelligence = intelligence
            self.wisdom = wisdom
            self.shield = shield
            self.max_hp = self.calc_max_hp()
            self.current_hp = current_hp
            self.armor = armor
            self.spells = spells
            self.inventory = inventory
            self.npc = npc
            self.god = god
            self.enemy = enemy
            self.dead = dead

        def __setattr__(self, key: str, value):
            self.__dict__[key] = value

        def save(self):
            return self.__dict__

        # @property
        def calc_max_hp(self) -> int:
            self.max_hp = 97 + self.strength * 3
            return self.max_hp

        def add_strength(self, x: int):
            self.strength += x
            self.max_hp = self.calc_max_hp()

        def add_agility(self, x: int):
            self.agility += x

        def add_intelligence(self, x: int):
            self.intelligence += x

        def add_wisdom(self, x: int):
            self.wisdom += x

        def add_shield(self, x: int):
            self.shield += x

        def add_armor(self, x: int):
            self.armor += x

    class Undead:

        def __init__(self, name):
            self.type = 'Undead'
            self.name = name
            self.strength = 1
            self.agility = 1
            self.intelligence = 1
            self.wisdom = 1
            self.shield = 0
            self.hp = 97 + self.strength * 3
            self.armor = 0
            self.spells = []
            self.inventory = []
            self.npc = False
            self.god = False

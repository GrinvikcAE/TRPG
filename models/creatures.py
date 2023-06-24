class Creatures:
    def __init__(self):
        self.type = 'Creature'

    class Alive:
        type: str
        name: str
        level: int
        strength: int
        agility: int
        intelligence: int
        wisdom: int
        max_hp: int
        current_hp: int
        shield: int
        armor: int
        # spells: list
        # inventory: dict
        npc: bool
        god: bool
        enemy: bool
        dead: bool

        def __init__(self, name, level=1, strength=1, agility=1, intelligence=1, wisdom=1,
                     shield=0, current_hp=100, armor=0, spells=None, inventory=None,
                     npc=False, god=False, enemy=False, dead=False):
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

        def __setattr__(self, key, value):
            self.__dict__[key] = value

        def save(self):
            return self.__dict__

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
        name: str
        strength: int
        agility: int
        intelligence: int
        wisdom: int
        hp: int
        shield: int
        armor: int
        # spells: dict
        # inventory: dict
        npc: bool
        god: bool

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

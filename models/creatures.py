class Creatures:
    def __init__(self):
        self.type = 'Creature'

    class Alive:
        name: str
        strength: int
        agility: int
        intelligence: int
        wisdom: int
        hp: int
        shield: int
        armor: int
        inventory: dict
        npc: bool
        god: bool

        def __init__(self, name):
            self.type = 'Alive'
            self.name = name
            self.strength = 1
            self.agility = 1
            self.intelligence = 1
            self.wisdom = 1
            self.shield = 0
            self.hp = 100 + self.strength * 3 + self.shield
            self.armor = 0
            self.inventory = {}
            self.npc = False
            self.god = False

        def add_strength(self, x: int):
            self.strength += x
            self.hp = 100 + self.strength * 3 + self.shield

        def add_agility(self, x: int):
            self.agility += x

        def add_intelligence(self, x: int):
            self.intelligence += x

        def add_wisdom(self, x: int):
            self.wisdom += x

    class Undead:
        name: str
        strength: int
        agility: int
        intelligence: int
        wisdom: int
        hp: int
        shield: int
        armor: int
        inventory: dict
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
            self.hp = 100 + self.strength * 3 + self.shield
            self.armor = 0
            self.inventory = {}
            self.npc = False
            self.god = False


bob = Creatures.Alive(name='Bob')
print(bob.agility)
bob.add_agility(5)
print(bob.agility)
# print(bob.strength)
# print(bob.hp)
# bob.add_strength(4)
# print(bob.strength)
# print(bob.hp)
# bob.add_strength(5)
# print(bob.strength)
# print(bob.hp)
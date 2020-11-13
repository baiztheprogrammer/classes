class Demon:
    def __init__(self,name,size,type,home,health):
        self.name = name
        self.size = size
        self.type = type
        self.home = home
        self.health = health
        self.wings = True
        self.horns = True


    def attack_demon(self,damage):
        result = 20 - damage
        print (f"Demon has hit minion for {damage} damage!")
        print(f'Minion health left: {result}')
        if damage >= 20:
            print('Minion has died, Demon victory!')

    def description(self):
        print(f"Name:{self.name} - Size:{self.size} - Type:{self.type} - Home:{self.home} - Health:{self.health} - Wings:{self.wings} - Horns:{self.horns}")


class Minion(Demon):
    def __init__(self,name,size,type,home,health,tail):
        super().__init__(name,size,type,home,health)
        self.tail = tail
        self.wings = False
        self.horns = False

    def attack_minion(self, damage):
        result = doom.health - damage
        print(f"Minion has hit Demon for {damage} damage!")
        print(f'Demon health left: {result}')
        if damage >= doom.health:
            print(f'Demon has died,Minion victory!')


    def description(self):
        print(f"Name:{self.name} - Size:{self.size} - Type:{self.type} - Home:{self.home} - Health:{self.health} - Tail:{self.tail} - Wings:{self.wings} - Horns:{self.horns}")

doom = Demon('doom','Tall','Hunter','Hell',50)
minion = Minion('naix','Small','Passive','Forest',20,'Long')
minion.attack_minion(20)

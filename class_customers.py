class Person:
    def __init__(self, name, sex, race, position):
        self.name = name
        self.sex = sex
        self.race = race
        self.position = position
        self.weight = 0
        self.height = 0
        self.health = 0
        self.health = True
        self.attack = 5
        self.damage = 0
        self.defence = 0

    def description(self):
        print(f'Имя персонажа - {self.name}, пол - {self.sex}, раса - {self.race}, позиция - {self.position}, рост - {self.weight}, вес - {self.height},'
              f'здоровье - {self.health}, урон - {self.damage}, защита - {self.defence}')


class Human(Person):
    def __init__(self, name = 'Adam', sex = 'male', race = 'human', position = 'earth'):
        super().__init__(name, sex, race, position)
        self.weight = 180
        self.height = 85
        self.health = 1000
        self.damage = 140
        self.defence = 80
        self.warrior = True
        self.agility = True
        self.live = True

    def description(self):
        print(f'Имя персонажа - {self.name}, пол - {self.sex}, раса - {self.race}, позиция - {self.position}, рост - {self.weight}, вес - {self.height},'
            f'здоровье - {self.health}, урон - {self.damage}, защита - {self.defence}, воин - {self.warrior}, умение:ловкость - {self.agility}')

    def set_health_hum(self, hum_health):
        if 0 < hum_health <= 1000:
            print('Человек выиграл!')
        else:
            print('Человек проиграл в равной битве!')


class Orc(Person):
    def __init__(self, name = 'Ultazar', sex = 'male', race = 'orc', position = 'drenor'):
        super().__init__(name, sex, race, position)
        self.weight = 220
        self.height = 140
        self.health = 800
        self.damage = 230
        self.defence = 50
        self.warrior = True
        self.strength = True
        self.live = True

    def description(self):
        print(f'Имя персонажа - {self.name}, пол - {self.sex}, раса - {self.race}, позиция - {self.position}, рост - {self.weight}, вес - {self.height},'
            f'здоровье - {self.health}, урон - {self.damage}, защита - {self.defence}, воин - {self.warrior}, умение:сила - {self.strength}')

    def set_health_orc(self, orc_health):
        if 0 < orc_health <= 1000:
            print('Орг выиграл!')
        else:
            print('Орг проиграл в равной битве!')

human = Human()
human.set_health_hum(10)
human.description()
orc = Orc()
orc.set_health_orc(10)
orc.description()

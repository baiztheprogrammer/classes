class Person:
    def __init__(self,name,sex,race,role):
        self.name = name
        self.sex = sex
        self.race = race
        self.role = role
        self.position = 0
        self.health = 100
        self.damage = 10
        self.armor = 5
        self.level = 0

    def move(self,new_position):
        if new_position > 0:
            self.position = new_position
        else:
            print('cant move there')

    def experience(self,xp):
        exp_list = [200,600,1800,2400,5000]
        for exp in exp_list:
            if xp > exp:
                self.level += 1
                xp -= exp
                self.health += 100
                self.damage += 5
                self.armor += 5

    def death(self):
        if self.health <= 0:
            print('you died,hahahahaha,loser,noob')

    def plate(self,item):
        if item == 'common':
            self.health += 50
            self.armor += 5

    def sword(self,item):
        if item == 'common':
            self.damage = self.damage + 20
        elif item == 'legendary' and self.level < 4:
            print('you cant use this legendary item')
        else:
            self.damage = self.damage + 200

    def description(self):
        print(self.name,self.sex,self.race,self.role,self.position,f"Health:{self.health},Damage:{self.damage},Armor:{self.armor},Level:{self.level}")

class Warrior(Person):
    def __init__(self,name,sex,race,role='Warrior'):
        super().__init__(name,sex,race,role)
        self.position = 20
        self.health = 500
        self.armor = 20
        self.damage = 20

class Fight:
    def __init__(self,health,damage):
        self.health = health
        self.damage = damage

    def __add__(self,other):
        result = self.health - other.damage
        return result

warrior = Warrior('Leonidas','M','Human')
warrior2 = Warrior('Achilles','M','Human')
warrior.experience(500)
warrior2.experience(6000)
warrior2.sword('legendary')
fight1 = Fight(warrior.health,warrior2.damage)
fight2 = Fight(warrior2.health,warrior.damage)
result1,result2 = 1,1
while result1 > 0 and result2 > 0:
    result1 = fight1 + fight2
    result2 = fight2 + fight1
    fight1 = Fight(result1,warrior.damage)
    fight2 = Fight(result2,warrior2.damage)
    print(result1,result2)
if result1 > 0:
    print(f"{warrior.name} has won")
else:
    print(f"{warrior2.name} has won")



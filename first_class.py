class Human:
    def __init__(self,name):
        self.name = name
        self.age = 0

    def change_age(self,num):
        if num > 0:
            self.age = num
        else:
            print('what?')
new_human = Human(name='maksim')
new_human1 = Human(name='emir')
new_human1.change_age(-20)
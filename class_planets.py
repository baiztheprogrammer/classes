class Planet:
    def __init__(self,name,size,color):
        self.name = name
        self.size = size
        self.color = color
        self.temp = -150
        self.water = False
        self.humanity = False
        self.oxygen = False
    def description(self):
        print(f"name:{self.name} ,size:{self.size} ,color:{self.color} ,temp:{self.temp} ,water:{self.water} ,humanity:{self.humanity} ,oxygen:{self.oxygen} ")

    def set_humanity(self):
        self.humanity = True
        self.oxygen = True
        self.water = True
        self.temp = 15

    def population(self,people):
        if self.humanity and self.water and self.oxygen:
            if people > 0:
                self.humanity = people
            else:
                'dont play around'
        else:
            'impossible to live'
            

earth = Planet('earth',20,"blue")
earth.set_humanity()
earth.population(10)
earth.description()
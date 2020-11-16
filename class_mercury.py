class Planet:
    def __init__(self,name,position):
        self.name = name
        self.form = 'shape'
        self.position = position
        self.temp = 0
        self.size = 0

    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size)

class Mercury(Planet):
    def __init__(self,position,name='Mercury'):
        super().__init__(name,position)
        self.temp = 120
        self.size = 'small'


class Jupiter(Planet):
    def __init__(self,position,name='Jupiter'):
        super().__init__(name,position)
        self.temp = 230
        self.size = 'medium'
        self.diamond_rain = True
    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size,self.diamond_rain)

class Saturn(Planet):
    def __init__(self,position,name='Saturn'):
        super().__init__(name,position)
        self.temp = -100
        self.size = 'medium'
        self.rings = True
        self.count_rings = 7

    def description(self):
        print(self.name,self.form,self.position,self.temp,self.size,self.count_rings)


mercury = Mercury('Solar System')
mercury.description()
jupiter = Jupiter('Solar System')
jupiter.description()
saturn = Saturn('Solar System')
saturn.description()


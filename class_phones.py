class Phone:
    def __init__(self,name,model,color,year,state):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.state = state
        self.memory = 33
        self.price = 1000
        self.battery = 0
        self.touchid = 5
        self.locked = False



    def set_battery(self,charge):
        if not self.locked:
            if 0<charge<=100:
                self.battery = charge
            else:
                print('what?')

    def unlock(self,tries):
        if 0<tries<=self.touchid:
            print('you logged in')
        else:
            self.locked = True
            print('phone is blocked')

    def loser(self,accidents):
        if accidents > 5:
            print('you idiot,you broke your phone')
        else:
            print(self.name, self.model, self.color, self.year, self.state, self.memory, self.price, self.battery,
                  self.touchid, self.locked)




iphone = Phone('iphone','pro max','space grey','2019','new')
iphone.price = 1100
iphone.loser(6)


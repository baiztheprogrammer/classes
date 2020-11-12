class Demon:
    def __init__(self,name,size,type,home):
        self.name = name
        self.size = size
        self.type = type
        self.home = home
        self.wings = True
        self.horns = True

    def description(self):
        print(f"Name:{self.name} - Size:{self.size} - Type:{self.type} - Home:{self.home} - Wings:{self.wings} - Horns:{self.horns}")


class Minion(Demon):
    def __init__(self,name,size,type,home):
        self.name = name
        self.size = size
        self.type = type
        self.home = home
        self.tail = True
        self.wings = False
        self.horns = False

    def description(self):
        print(f"Name:{self.name} - Size:{self.size} - Type:{self.type} - Home:{self.home} - Wings:{self.wings} - Horns:{self.horns} - Tail:{self.tail}")

    def sleep(self):
        if sleep = True:





baiz = Demon('doom','Tall','Hunter','Hell')
baiz.description()
minion = Minion('naix','Small','Passive','Forest')
minion.description()


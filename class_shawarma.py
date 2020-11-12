class Shawarma:
    def __init__(self,meat,size,vegetables,hunger):
        self.meat = meat
        self.hunger = hunger
        self.size = size
        self.vegetables = vegetables
        self.ketchup = True
        self.mayo = False
        self.ff = False
    def description(self):
        print(f"meat:{self.meat} ,hunger:{self.hunger}, size:{self.size}, vegetables:{self.vegetables}, ketchup:{self.ketchup}, mayo:{self.mayo},ff:{self.ff}")

    def mixed(self):
        self.meat = 'chicken,beef'
        self.ketchup = True
        self.mayo = True
        self.ff = True

oasis = Shawarma('chicken','20','medium','lettuce,tomatoes,onions')
point = Shawarma('beef','15','small','lettuce,onions')
point.mayo = True
narynskaya = Shawarma('chicken','18','large','lettuce,onions,tomatoes')
narynskaya.mayo = True
damduu = Shawarma('chicken','25','large','lettuce,tomatoes,onions')
damduu.mixed()
oasis.description()
point.description()
narynskaya.description()
damduu.description()
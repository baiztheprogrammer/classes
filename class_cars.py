class Car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        self.fuel = 0
    def description(self):
        print(self.name,self.model,self.year)
    def patrol(self,new_fuel):
        self.fuel = self.fuel + new_fuel
    def start(self):
        print('car is ready')
    def stop(self):
        print('car is dead')

new_car = Car('range rover','sport','2019')
print(new_car.fuel)
new_car.patrol(20)
print(new_car.fuel)
new_car.patrol(20)
print(new_car.fuel)
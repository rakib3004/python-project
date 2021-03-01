class Car:
    CarId=10000
    CarName=''

    def __init__(self,name):
        self.CarName=name
        print(self.CarName,'is launching!!!')

    def CarCounter(self):
        self.CarId=self.CarId+1
        print('Number of Buying Car:',self.CarId)

class CarDiller(Car):
    revenue = 0
    def profit(self):
        self.revenue=self.revenue+41500
        self.CarCounter()
        print(self.CarName,'have', self.revenue,'earns')

iCar = Car('Audi')

for icar in range(10):
    iCar.CarCounter()

jCar = Car('Tesla')

for jcar in range(7):
    jCar.CarCounter()


kCar = CarDiller('Tata Company')
for kcar in range(7):
    kCar.profit()


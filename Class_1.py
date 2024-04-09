class House:

    def __init__(self):
        self.floor = 0

    def numberOfFloors(self):
        self.floor = 10


my_house = House()
my_house.numberOfFloors()
print('Текущий этаж равен ', my_house.floor)



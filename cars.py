class Car():
    def __init__(self, model, age, volume, price, mileage, wheel = 4 ):
        self.model = model
        self.age = age
        self.volume = volume
        self.price = price
        self.mileage = mileage
        self.wheel = wheel
    def description(self):
        print('Модель машины:', self.model)
        print('Год выпуска:', self.age)
        print('Объем двигателя:', self.volume)
        print('Цена:', self.price, '$')
        print('Пробег:', self.mileage, 'км')
        print('Количество колес:', self.wheel)
class Truck(Car):
    def __init__(self, model, age, volume, price, mileage, wheel = 8):
        super().__init__(model, age, volume, price, mileage, wheel = 4)
        self.wheel = wheel

car1 = Car('Toyota', 2012, 1.8, 2000,30)
car2 = Truck('ВАЗ', 2010, 2.0, 4000,100)
car1.description()
car2.description()
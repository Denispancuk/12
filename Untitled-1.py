class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"Транспорт: {self.brand} {self.model}, Рік: {self.year}"

    def honk(self):
        return "Звук транспорту!"

class Car(Transport):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def info(self):
        return f"Машина: {self.brand} {self.model}, Рік: {self.year}, Пальне: {self.fuel_type}"

    def honk(self):
        return "Дзвінок машини"

class Bicycle(Transport):
    def __init__(self, brand, model, year, gear_count):
        super().__init__(brand, model, year)
        self.gear_count = gear_count

    def info(self):
        return f"Велосипед: {self.brand} {self.model}, Рік: {self.year}, Передачі: {self.gear_count}"

    def honk(self):
        return "Дзвінок велосипеду!"

car = Car("Peugeot", "3008", 2012, "Бензин")
bicycle = Bicycle("Ukraine", "2101", 1960, 1)

print(car.info())
print(car.honk())

print(bicycle.info())
print(bicycle.honk())

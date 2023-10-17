# Дз
# 1
# class Fruits:
#     def __init__(self, name, color, weigh):
#         self.name = name
#         self.color = color
#         self.weigh = weigh

#     def info(self):
#         print(f"имя фрукта: {self.name}, цвет этова фрукта: {self.color}, вес этого фрукта {self.weigh}гр ")


# apple = Fruits("яблоко", "красный", 200)
# apple.info()
# cherry = Fruits("вишня", "темно-красный", 100)
# cherry.info()
# banana = Fruits("банан", "желтый", 300)
# banana.info()

# 2
# class Car:
#     def __init__(self,model, year, color):
#         self.model = model
#         self.year = year
#         self.color = color

#     def drive(self,city):
#         self.city = city
#         print(f"модель вашей машины: {self.model},год вашей машины: {self.year},  с наслождением едет в город:  {self.city}")


# BMW = Car("BMW F90",2017, "темно-синий" )
# BMW.drive("Бишкек")

# доп задание
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.fuel = 0  

    def refuel(self, liters):
        if liters > 40:
            print("Вы не можете заправить больше 40 литров за раз.")
        else:
            self.fuel += liters
            print(f"Бак заполнен на {liters} литров. Всего топлива: {self.fuel} литров")

    def drive(self, city, distance):
        fuel_needed = distance / 10  
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
            print(f"Машина - {self.model} едет в {city}. Остаток топлива: {self.fuel} литров")
        else:
            max_distance = self.fuel * 10
            print(f"Машина не может проехать в {city}. Максимальное расстояние: {max_distance} км")


my_car = Car("BMW M5 F90 ", 2017, "темно-синий")
my_car.refuel(40)
my_car.drive("бишкек", 200)

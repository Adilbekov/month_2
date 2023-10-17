class My_Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def __str__(self):
        return f"Your car setting\ncar name: {self.name}\ncar model: {self.model}\ncar color: {self.color}"

    def sound_car(self):
        print('gaz: att attt!! aaatttttt!!!!')

    def chek(self):
        print("Cheeeeek!!!!")

if __name__ == "__main__":
    car = My_Car('buggtti', 'Viron', 'balack',)
    print(car)
    car.sound_car()
    car.chek()
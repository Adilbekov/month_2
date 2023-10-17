# Декомпозиция - разделение кода по модулям
# from calculator import div as divition # Мы можем переименновывать во время импортов (чтобы избежать конфликтов)
# divition(10,5)



# from calculator import add, sub, mult, div  # точечный иморт
# print(add(5,10))
# print(add(20, 80))

# print(sub(50,30))
# print(sub(1000, 90))

# mult(1785461285,4154852)
# mult(123456789,987654321)

# div(10, 5)
# div(10000000000000,5)




# import calculator # иморт модуля

# print(calculator.sub(100,50))
# calculator.mult(100,10)



# from calculator import*  # Из модуля имортируем всё

# print(add(852,8451))
# print(sub(5000,1000))
# div(1000, 5)
# mult(1000,2433)


from my_car import My_Car

class My_Car_2(My_Car):
    def __init__(self, name, model, color, hp):
        super().__init__(name, model, color)
        self.hp = hp

    def __str__(self):
        return super().__str__() + f"\nand hp: {self.hp}"

mersedes = My_Car_2('Mersedes', 'W-211', 'white', "2000+")
print(mersedes)
mersedes.sound_car()
mersedes.chek()
 

BMW = My_Car('Alpina', 'm3 compitition', 'blue')
print(BMW)
BMW.sound_car()
BMW.chek()

# Кастомные модули: calkulator, my_car
# Встроенные модули: random , math, datetime, time
# Внешние модули: termcolor
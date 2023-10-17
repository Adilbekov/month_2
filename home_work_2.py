# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married

#     def introduce_myself(self):
#         print(f' Hallo!! My name is {self.fullname}, I am {self.age} year old, and I am {self.is_married}')


# # doni = Person('Doni', 15, 'not married')
# # doni.introduce_myself()


# # class Student(Person):
# #     def __init__(self,fullname, age, is_married):
# #         Person.__init__(self, fullname, age, is_married)

# #     def average_value(self):
# #         uroki = {"algebra": 4, "fizika": 3, "fizra": 5}
# #         for i,auf in uroki.items():
# #             c = uroki.values()
# #             b = sum(c) / len(c)  
# #         print(f"ваш средний балл: {b}")
    

# # aidar = Student("Aidar", 16, "not married")
# # aidar.introduce_myself()
# # aidar.average_value()



# class Teacher(Person):
#     def __init__(self, fullname, age, is_married,experiense, salary):
#         super().__init__(fullname, age, is_married, )
#         self.experiense = experiense
#         self.salary = salary

#     def zp(self):
#         for i in range(self.experiense):
#             self.salary += 3000
#         print(f"Ваша зарплата стала: {self.salary}")

# a = Teacher('Doni', 22, 'not married', 5, 40000)
# a.introduce_myself()
# a.zp()
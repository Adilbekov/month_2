import sqlite3 

car = sqlite3.connect("car_sistem.db")
cursor = car.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS my_car (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR (100) NOT NULL,
               model VARCHAR (200) NOT NULL,
               color VARCHAR (150) NOT NULL,
               car_cost DOUBLE (11.2) NOT NULL DEFAULT 0.0,      
               payment_method VARCHAR (100) NOT NULL,
               payment VARCHAR (100) NOT NULL
);
""")


class Car():
    def __init__(self):
        self.name = None
        self.model = None
        self.color = None
        self.car_cost = 0.0
        self.payment_method = None
        self.payment = None

    def data(self, name, model, color, car_cost, payment_method, payment):
        cursor.execute(f"""INSERT INTO my_car (name, model, color, car_cost, payment_method, payment)
                       VALUES ('{name}', '{model}', '{color}', '{car_cost}', '{payment_method}', '{payment}');""")
        car.commit()

# carr = Car()
# carr.data('bmw', 'e-60', 'black', 100000.00, 'наличными', 'вся смма')

car.commit()
car.close()


user = sqlite3.connect("sistem.db")
c = user.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS client_data (
          name VARCHAR (100) NOT NULL,
          sername VARCHAR (100) NOT NULL,
          age INTEGER NOT NULL,
          number INTEGER NOT NULL,
          gmail VARCHAR (200) NOT NULL,
          password VARCHAR (100)
);""")


class Person():
    def __init__(self):
        self.name = None
        self.sername = None
        self.age = 0
        self.number = 0
        self.gmail = None
        self.password = None

    def regist(self, name, sername, age, number, gmail, password):
        c.execute(f"""INSERT INTO client_data (name, sername, age, number, gmail, password)
                  VALUES ('{name}', '{sername}', '{age}', '{number}', '{gmail}', '{password}');""")
        
        user.commit()
        user.close()
        

people = Person()
people.regist('Erbol', 'Adilbekov', 16, 996776001124, 'adilbekovv@gmail.com', "m5")
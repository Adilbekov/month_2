class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    # 
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu_2):
        self.cpu = cpu_2

    # 
    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, memory_2):
        return self.memory == memory_2
    
    def __str__(self):
        return f"your computer cpu: {self.cpu}, your computer memory: {self.memory}GB "
    
    def info(self):
        print("\nyour laptops after the change:  ")
    
    
    # 
    def __add__(self, other):
        return self.cpu + other.memory
    
    def __sub__(self, other):
        return self.cpu - other.memory
    
    def __mul__(self, other):
        return self.cpu * other.memory
    
    def __floordiv__(self, other):
        return self.cpu // other.memory
    
    def __truediv__(self, other):
        return self.cpu / other.memory
    
    # 

    def __gt__(self, other): # больше чем (">")
        return self.cpu > other.memory 

    def __lt__(self, other): # меньше чем ("<") - less than
        return self.cpu > other.memory

    def __eq__(self, other): # равно ("==") - equals
        return self.cpu == other.memory

    def __ne__(self, other): # не равно ("!=") - not equals
        return self.cpu != other.memory

    def __ge__(self, other): # больше или равно (">=")
        return self.cpu >= other.memory

    def __le__(self, other): # меньше или равно ("<=")
        return self.cpu <= other.memory
    
hp = Computer(256,1000)
acer = Computer(512, 1000)

# print(acer)
# print(hp)
# acer.info()

# print(hp + acer)
# print(hp - acer)
# print(hp * acer)
# print(hp // acer)
# print(hp / acer)

# print(hp > acer)
# print(hp < acer)
# print(hp == acer)
# print(hp != acer)
# print(hp >= acer)
# print(hp <= acer)

# 

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    
    @sim_cards_list.setter
    def sim_cards_list(self, simka):
        self.__sim_cards_list = simka

    

    def __call__(self, sim_card_number, call_to_number):
        call_to_number = int(input('choose numper phone: +996'))
        sim_card_number = int(input('choose sim cards: 1  or  2\n'))

        if sim_card_number == 1:
            print(f'cal numbers {call_to_number} \n choose sim cards {self.sim_cards_list[0]}')
        elif sim_card_number == 2:
            print(f'cal numbers {call_to_number} \n choose sim cards {self.sim_cards_list[1]}')
        else:
            print('Sory\n Error sintax!!!')

# iphone = Phone(sim_cards_list = ['O!', 'Beeline!'])
# iphone.__call__(776001124,1)


class SmartPhone(Computer, Phone):
    def __init__(self, memory):
        super().__init__(self, memory)

    def __cal__(self, lokation):
        print(f"Simulating route to --{lokation}-- using GPS.")

    def __str__(self):
        return f"your have {self.memory}GB \nnow your have: "

    def __add__(self, other):
        return self.memory + other.memory
    
# 
yser = SmartPhone(None)
yser.__cal__("Chon-Alai")

acer = SmartPhone(1000)
add_memory = SmartPhone(1000)
print(acer)
print(f'{acer + add_memory}GB!!')
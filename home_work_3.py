class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    # use geter in metod
    @property
    def make_computation(self):
        return self.__make_computation

    
    # use geter and setter in atribut: cpu
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, cpu_2):
        self.cpu = cpu_2
    
    # use geter and setter in atribut: cpu
    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, memory_2):
        return self.__memory == memory_2


    def __make_computation(self):
        print(f'positive result: {self.__cpu + self.__memory}')
        print(f'minus result: {self.__cpu - self.__memory}')
        print(f'division result: {self.__cpu / self.__memory}')
        print(f'mult result: {self.__cpu * self.__memory}')


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    
    @sim_cards_list.setter
    def sim_cards_list(self, simka):
        self.__sim_cards_list = simka

    def call(self, sim_card_number, call_to_number):
        call_to_number = int(input('choose numper phone: +996'))
        sim_card_number = int(input('choose sim cards: 1  or  2\n'))
        if sim_card_number == 1:
            print(f'cal numbers {call_to_number} \n choose sim cards {self.sim_cards_list[0]}')
        elif sim_card_number == 2:
            print(f'cal numbers {call_to_number} \n choose sim cards {self.sim_cards_list[1]}')
        else:
            print('Sory\n Error sintax!!!')


class SmartPhone(Computer, Phone):
    def __init__(self, memory):
        super().__init__(self, memory)
    def user_gps(self, lokation):
        print(f"Simulating route to {lokation} using GPS.")

    def add_memory(self, add):
        add += self.memory
        print(f'we have {self.memory}GB, now we have {add}GB!!')

# 10(1)
# acer = Computer(4, 512)
# acer.make_computation()

# # 10(2)
# iphone = Phone(sim_cards_list = ['O!', 'Beeline!'])
# iphone.call(996776001124,2)

# # 10(3)
# user = SmartPhone(512)
# user.user_gps('Batken')
# user.add_memory(488)

# user = SmartPhone(1000)
# user.user_gps("USA")
# user.add_memory(1000)

# all metots  are used??

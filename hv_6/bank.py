class Bank:
    def __init__(self):
        self.user_balans = 0

    def __str__(self):
        return f"Your balans is: {self.user_balans}$$$\n "

    def replenishmet(self):
        new_balans = int(input("Enter amout:\n"))
        self.user_balans += new_balans
        print(f"your new balans after replenishmet: {new_balans}$$$\nThank you that for useing our sistem!!\n")
        
    def conclusion(self):
        new_balans = int(input("Enter amout: "))
        self.user_balans -= new_balans
        print(f"your new balans after conclusion: {new_balans}$$$\n`Thank you that for useing our sistem!!\n")

    def do(self):
            while True:
                user1 = int(input('whot do you wont to do?\n1-info balans\n2-replenish\n3-conclusion\n'))
                if user1 == 1:
                    print(self.__str__())
                elif user1 == 2:
                    print(self.replenishmet())
                elif user1 == 3:
                    print(self.conclusion())
                else:
                    print("Syntax error!")
                    break
            


if __name__ == "__main__":
    beka = Bank()
    beka.do()
    # beka.replenishmet()
    # beka.conclusion()
    # print(beka)
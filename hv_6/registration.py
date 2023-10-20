import random
def regist():
    while True:
        user_name = input("Enter your name:\n")
        user_age = int(input("Enter your age: \n"))
        if user_age < 18:
            print("It too early for you")
            break
        else:
            user_number = int(input("Enter your number: \n+996"))
            pin = random.randint(10000, 99999)
            print(f"Your pin: {pin}")
            pin1 = input("Enter your pin: \n")
            if pin1 == pin:
                next
            else:
                print("")
            pin_cod = input("Come up pin-code: \n")
            pin_cod2 = input("Confirmation pin-code: \n")
            if len(pin_cod) != 4:
                print("The pin code short")
            elif pin_cod == 1234:
                print("pin code usually and nise")
            elif pin_cod != pin_cod2:
                print("pin cods different")
            elif pin_cod == pin_cod2:
                print("Congratulations! You finished registrate in our bank")
                break
            else:
                print('Error sintax!')
                break

if __name__ == "__main__":
    regist()
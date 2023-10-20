from registration import regist
from bank import *
person = Bank()
def exit(): 
    user = input("what your name?\n")
    bank_sistem1 = print(f"Hallo {user}!!!")
    bank_sistem = int(input("Wont to use our banking banking system?\nChoose operation: 1-yes or 2-no\n"))
    if bank_sistem == 1:
        print("Oy very well! Then let's start registration!!")
    elif bank_sistem == 2:
        print("hahaha you will still use our site!\nThen let's stsrt registration!!")
    else:
        print("Sintax Error!!!")

exit()
regist()
man = int(input("Okay!\nwe have opened a bank card for you!!!\nWont to use? Select operetion: 1-yes or 2no\n"))
if man == 1:
    print(person.do())
else:
    print("Okay thanks for everything see you again!!!")

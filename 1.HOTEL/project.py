d = {
    'E': {'milk': [60, 0], 'cream': [75, 0], 'latte': [100, 0]},
    'C': {'milk': [80, 0], 'cream': [90, 0], 'latte': [125, 0]},
    'L': {'milk': [100, 0], 'cream': [125, 0], 'latte': [150, 0]}
   }

class Espresso:
    def milk(self):
        e_milk_quantity=int(input("How many Espresso Milk: "))
        t1 = d['E']['milk'][1] + e_milk_quantity
        d['E']['milk'][1] = t1
        print(t1)
    def cream(self):
        e_cream_quantity = int(input("How many Espresso Cream: "))
        t2 = d['E']['cream'][1] + e_cream_quantity
        d['E']['cream'][1] = t2
        print(t2)
    def latte(self):
        e_latte_quantity = int(input("How many Espresso Latte: "))
        t3 = d['E']['latte'][1] + e_latte_quantity
        d['E']['latte'][1] = t3
        print(t3)
class cappuccino:
    def milk(self):
        print("c : milk")
        c_milk_quantity = int(input("How many cappuccino Milk: "))
        t4 = d['E']['milk'][1] + c_milk_quantity
        d['C']['milk'][1] = t4
        print(t4)
    def cream(self):
        print("c : cream")
        c_cream_quantity = int(input("How many  cappuccino Cream: "))
        t5 = d['C']['cream'][1] + c_cream_quantity
        d['C']['cream'][1] = t5
        print(t5)
    def latte(self):
        print("c : latte")
        c_latte_quantity = int(input("How many cappuccino Latte: "))
        t6 = d['C']['latte'][1] + c_latte_quantity
        d['C']['latte'][1] = t6
        print(t6)

class latte:
    def milk(self):
        l_milk_quantity = int(input("How many latte Milk: "))
        t7 = d['L']['milk'][1] + l_milk_quantity
        d['L']['milk'][1] = t7
        print(t7)
    def cream(self):
        l_cream_quantity = int(input("How many latte Cream: "))
        t8 = d['L']['cream'][1] + l_cream_quantity
        d['L']['cream'][1] = t8
        print(t8)
    def latte(self):
        l_latte_quantity = int(input("How many latte Latte: "))
        t9 = d['L']['latte'][1] + l_latte_quantity
        d['L']['latte'][1] = t9
        print(t9)
E = Espresso()
C = cappuccino()
L = latte()
while True:
    print()
    print("----------------HOTEL MANAGEMENT--------------------")
    print(" 1.ESPRESSO \n 2.CAPPUCCINO \n 3.LATTE")
    choice = int(input("enter the choice : "))
    if choice == 1:
        print("**********    ESPRESSO  **************")
        print(" 1.MILK: RS 60 \n 2.CREAM: RS 75  \n 3.LATTE : RS 100 ")
        Es_choice = int(input("enter the choice : "))
        if Es_choice == 1:
            E.milk()
        elif Es_choice == 2:
            E.cream()
        elif Es_choice == 3:
            E.latte()
        else :
            print("please choose valid item ")
    elif choice == 2:
        print("**********    CAPPUCCINO  **************")
        print(" 1.MILK: RS 80 \n 2.CREAM: RS 90  \n 3.LATTE : RS 125 ")
        CA_choice = int(input("enter the choice : "))
        if CA_choice == 1:
            C.milk()
        elif CA_choice == 2:
            C.cream()
        elif CA_choice == 3:
            C.latte()
        else :
            print("please choose valid item ")
    elif choice == 3:
        print("**********    LATTE  **************")
        print(" 1.MILK: RS 100 \n 2.CREAM: RS 125  \n 3.LATTE : RS 150 ")
        LA_choice = int(input("enter the choice : "))
        if LA_choice == 1:
            L.milk()
        elif LA_choice == 2:
            L.cream()
        elif LA_choice == 3:
            L.latte()
        else:
            print("please choose valid item ")
    else:
        print("please enter the valid item ")
    con = int(input("do you want to conitnue  press 1"))
    if con != 1:
        break
for key,value in d.items():
    for key1,value1 in value.items():
        if value1[1]>0:
            print(key,key1,value1[0],value1[1],value1[0]*value1[1])

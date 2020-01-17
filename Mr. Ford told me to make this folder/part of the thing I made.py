import myClass as mc

accs = []

name = input("What is your name: ")
bank = input("How much would you like to deposit: ")
passs = input("What would you like to make your password: ")

accs.append(mc.Account(name, bank, passs))

checkName = input("What is your name: ")
checkPasss = input("What is your password: ")

if checkName == name and checkPasss == passs:
            print("Welcome, " + name)
            ddposit = input ("How much money would you like to put in: ")
            wwithdrawl = input ("How much will you withdarw today?")

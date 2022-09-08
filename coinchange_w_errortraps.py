#coinchange program with error traps and input validation

"""A program to calculate the value of some change in dollars"""
import math
from Crypto import Random
from Crypto.Hash import SHA256

def quarter():
    """enter _quarters"""
    print("entering quarters function")

#   
    digitsmax = int(9)
    digitsmin = int(1)
    msg1 = "Quarters: "
    print("Please enter the count of each coin type to max of ", digitsmax)
#   
    quarters = int(checkinginput(digitsmax, digitsmin, msg1))
    print(type(quarters))
    print("exiting quarters function")
    return quarters

def checkinginput(digitsmax, digitsmin, msg1):
    """get input"""
    while True:
        try:
            a = input(msg1)
            a_len = len(a)
#           
            if digitsmax >= a_len >= digitsmin:
                print("a= ", int(a))
                return int(a)
            else:
                print('Invalid input!')
        except ValueError:
            print('Name error!Please enter a', digitsmax, 'digit number')
        except SyntaxError:
            print('Syntax Error!Please try again!')
    return int(0)

def main():
    coin_ex()
    

def coin_ex():
    """main function"""
    print("entering main routine")
    print("Change Counter")
    print()
    quarters1 = quarter()
    print(type(quarters1))
    print("quarters entered", quarters1)
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = quarters1 * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print()
    print("The total value of your change is", total)
    print("exiting main routine")

main()

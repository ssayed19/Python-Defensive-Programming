#convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell
import sys

def main():
    celsius = float(input("What is the Celsius temperature? "))
    celcius = float(celsius)

    if celsius > int(100) or celsius < 0:
        sys.exit("Value must be between 0 and 100") 
    temptype = type (celsius)
    print (temptype)
    fahrenheit = (9/5) * celsius + 32
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")
main()
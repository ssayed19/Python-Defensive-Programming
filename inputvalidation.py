def checkingInput():
    while True:
        try:
            inpt = str(input("enter a value:" ))
            if inpt.isnumeric():
                if inpt == "3" or inpt == "5" or inpt == "7":
                    return inpt
                else:
                    print('Invalid input!(a)')
            elif inpt.isalpha():
                if inpt == str("a").upper() or inpt == str("A").lower() or inpt ==str("k").lower():
                    return inpt
                else:
                    print('Invalid input!(b)')
            else:
                print('Invalid input!(c)')
        except NameError:
            print('Name error!Please try again!')
        except SyntaxError:
            print('Syntax Error!Please try again!')

checkingInput()
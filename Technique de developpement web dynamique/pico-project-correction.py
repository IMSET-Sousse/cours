divZero = "Erreur Division par zero"

while True:
    op = input("Donner operation (+, -, *, /, //, %, **, /q)")
    if op == '/q':
        print("Program terminated")
        break

    x = float(input("Donner X: "))
    y = float(input("Donner Y: "))

    if op == '+':
        S = x + y
        print(str(x) + " + " + str(y) + " = " + str(S))
    elif op == '-':
        S = x - y
        print(str(x) + " - " + str(y) + " = " + str(S))
    elif op == '*':
        S = x * y
        print(str(x) + " * " + str(y) + " = " + str(S))
    elif op in ['/', '//', '%']:
        if y == 0:
            print(divZero)
        elif op == '/':
            S = x / y
            print(str(x) + " / " + str(y) + " = " + str(S))
        elif op == '//':
            S = x // y
            print(str(x) + " // " + str(y) + " = " + str(S))
        elif op == '%':
            S = x % y
            print(str(x) + " % " + str(y) + " = " + str(S))
    elif op == '**':
        S = x ** y
        print(str(x) + " ** " + str(y) + " = " + str(S))
    else:
        print("operation non suporté")
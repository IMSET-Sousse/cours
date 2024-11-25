x = float(input("Donner X: "))
y = float(input("Donner Y: "))
op = input("Donner Operation (+, -, *, /)")

if op == '+':
    S = x + y
    print(str(x) + " + " + str(y) + " = " + str(S))
elif op == '-':
    S = x - y
    print(str(x) + " - " + str(y) + " = " + str(S))
elif op == '*':
    S = x * y
    print(str(x) + " * " + str(y) + " = " + str(S))
elif op == '/':
    if y == 0:
        print("Erreur Devision par zero")
    else:
        S = x / y
        print(str(x) + " / " + str(y) + " = " + str(S))
else:
    print("operation non suporté")
while True:
    SB = float(input("Salaire de base: "))
    nHS = float(input("Heures supplémentaires: "))
    tHS = float(input("Taux majoré (1.75 ou 2.00): "))
    P = float(input("Primes: "))
    OP = input("Opération (B, C, N, E, F, /q): ")


    # Calcul
    taux_horaire = SB / 173.33
    hs = nHS * tHS * taux_horaire
    SBrut = SB + hs + P


    CS_cnss = SBrut * 0.0918
    CS_am = SBrut * 0.0182
    CS = CS_cnss + CS_am

    SN = SBrut - CS

    CP = SBrut * 0.1657
    CE = SBrut * CP



    # Affichage
    if OP == "B":
        print("Salaire brut total = ", SBrut)
    elif OP == "C":
        print("Cotisations sociales = ", CS)
    elif OP == "N":
        print("Salaire net = ", SN)
    elif OP == "E":
        print("Coût employeur = ", CE)
    elif OP == "F":
        print("=== FICHE DE PAIE TUNISIENNE ===")
        print("Salaire de base:         ",SB," TND")
        print("Heures supplémentaires:   ",hs," TND")
        print("Primes:                   ",P," TND")
        print("---------------------------")
        print("Salaire brut:            ",SBrut," TND")
        print("Cotisations CNSS (9.18%):  ",CS_cnss," TND")
        print("Assurance maladie (1.82%):  ",CS_am," TND")
        print("---------------------------")
        print("Salaire net:             ",SN," TND")
        print("Charges patronales:       ",CP," TND")
        print("Coût employeur:          ",CE," TND")
        print("=============================")
    elif OP == "/q":
        break
    else:
        print("Opération invalide")
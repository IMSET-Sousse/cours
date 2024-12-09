# Projet RH : Calculateur de Paie

# Demander les informations à l'utilisateur
salaire_base = float(input("Salaire de base: "))
heures_sup = float(input("Heures supplémentaires: "))
taux_majore = float(input("Taux majoré (1.75 ou 2.00): "))
primes = float(input("Primes: "))

# Calculs
taux_horaire = salaire_base / 173.33

while True:
    operation = input("Opération (B, C, N, E, F, /q): ")
    
    if operation == '/q':
        break
        
    # Calculs
    salaire_brut = salaire_base + (heures_sup * taux_horaire * taux_majore) + primes

    cotisations_cnss = salaire_brut * 0.0918
    cotisations_maladie = salaire_brut * 0.0182
    cotisations = cotisations_cnss + cotisations_maladie
    
    salaire_net = salaire_brut - cotisations
    
    cotisations_patronales = salaire_brut * 0.1657
    cout_employeur = salaire_brut + cotisations_patronales
    
    heures_sup_montant = heures_sup * taux_horaire * taux_majore

    if operation == 'B':
        print(f"Salaire brut total = {salaire_brut:.1f}")
        
    elif operation == 'C':
        print(f"Cotisations sociales = {cotisations:.2f}")
        
    elif operation == 'N':
        print(f"Salaire net = {salaire_net:.2f}")
        
    elif operation == 'E':
        print(f"Coût employeur = {cout_employeur:.2f}")
        
    elif operation == 'F':
        charges_patronales = salaire_brut * 0.1657
        cout_employeur = salaire_brut + charges_patronales
        
        print("=== FICHE DE PAIE TUNISIENNE ===")
        print(f"Salaire de base:         {salaire_base:.2f} TND")
        print(f"Heures supplémentaires:   {heures_sup_montant:.2f} TND")
        print(f"Primes:                   {primes:.2f} TND")
        print("---------------------------")
        print(f"Salaire brut:           {salaire_brut:.2f} TND")
        print(f"Cotisations CNSS (9.18%): {cotisations_cnss:.2f} TND")
        print(f"Assurance maladie (1.82%): {cotisations_maladie:.2f} TND")
        print("---------------------------")
        print(f"Salaire net:            {salaire_net:.2f} TND")
        print(f"Charges patronales:      {charges_patronales:.2f} TND")
        print(f"Coût employeur:         {cout_employeur:.2f} TND")
        print("=============================")
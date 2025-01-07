def convertisseur(input):
    inch = 2.54  # Conversion d'un pouce en centimètres
    centimeters = float(input) * inch  # Conversion de la valeur d'entrée. 
    
    # Avec la fonction float, j’ai élargi les possibilités pour que la fonction puisse gérer à la fois des nombres entiers et des nombres à virgule. Cela rend le programme plus flexible et adapté à des cas où l’utilisateur pourrait entrer des valeurs comme 5.5 pouces ou 7.25 pouces.
    # L’idée est d’anticiper des besoins potentiels afin d'éviter les désagréments du terminal ;).

    print(centimeters)  # Affichage du résultat

# Appels de la fonction avec différentes valeurs

convertisseur(5)
convertisseur(7)

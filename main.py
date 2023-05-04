print("Calcul d'un prêt immobilier ou d'un crédit a la consommation")
mont=int(input("Entrez le montant du prêt ou crédit: "))
taux=int(input("entrez le taux annuel en %: "))
annee=int(input("entrez le nombre d'années : "))
tauxmens=(taux/100)/12
mens=(mont*tauxmens*((1+tauxmens)**(12*annee)))/(((1+tauxmens)**(12*annee))-1)
montint=(mens*annee*12)-20000
mens=round(mens,2)
montint=round(montint,2)
print("La mensulaité avec intérêts est de :", mens)
print("Le montant des intérêts remboursés sont de :",montint)
print("Le taux mensuel est de ",tauxmens)
print("Tableau d'amortissement : ")
print("Mois - Mensualité - Intérêts - Capital rembousé - Capital restant du - Intérêts remboursés")
for i in range(0,24):
    print(i," - ", mens," - ",)
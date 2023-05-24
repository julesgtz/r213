import math
import pandas

montant = float(input("Entrer le montant du prêt ou crédit: "))
taux = float(input("Entrer le taux annuel en %: ")) / 100
annee = float(input("Entrer le nombre d'année: "))

taux_periodique = (1 + taux)**(1/12) - 1
mois = math.ceil(annee * 12)
mensualite = (montant * taux_periodique * ((1 + taux_periodique)**mois)) / (((1 + taux_periodique)**mois) - 1)
i_sum = mensualite * mois - montant
    

print(f"La mensualité avec intérêts est de {round(mensualite, 2)} euros.")
print(f"Le montant des intérêts remboursés sont de {round(i_sum, 2)} euros.")
print(f"Le taux mensuel est de {round(taux_periodique, 4)}.")

tableau = pandas.DataFrame({"Mensualité":[round(mensualite, 2)]*mois}, columns=["Mois", "Mensualité", "Intérêts", "Capital remboursé",
                                    "Capital restant du", "Intérêts remboursés"])
capital_restant = montant
interet_rembourse = 0
for i in range(mois):
    tableau.iloc[i, 0] = i + 1
    interet = taux_periodique * capital_restant
    tableau.iloc[i, 2] = interet

    capital_rembourse = mensualite - interet
    tableau.iloc[i, 3] = capital_rembourse

    capital_restant = capital_restant - capital_rembourse
    tableau.iloc[i, 4] = capital_restant

    interet_rembourse = interet_rembourse + interet
    tableau.iloc[i, 5] = interet_rembourse

print(tableau)

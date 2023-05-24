import math

placement = float(input("Entrer le placement de départ: "))
montant = float(input("Entrer le montant du versement mensuel: "))
taux = float(input("Entrer le taux annuel en %: ")) / 100
annee = float(input("Entrer le nombre d'années: "))

taux_periodique = (1 + taux)**(1/12) - 1
mois = math.ceil(annee * 12)

capital = placement
for i in range(mois):
    capital = capital + montant
    capital = capital * (1 + taux_periodique)

invest = placement + (montant * mois)
interet = capital - invest
    
print(f"Le capital acquis avec intérêts est de {round(capital, 2)} euros au bout de {int(annee)} ans avec des versements mensuels de {int(montant)} euros.")
print(f"Les intérêts gagnés au taux annuel de {round(taux * 100, 1)} % sont de {round(interet, 2)} euros.")
print(f"Sans placement avec intérêts le capital acqui serait de {round(invest, 2)} euros.")

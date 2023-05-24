placement = float(input("Entrer le placement de départ: "))
montant = float(input("Entrer le montant du versement mensuel: "))
taux = float(input("Entrer le taux annuel en %: ")) / 100
annee = int(input("Entrer le nombre d'années: "))

capital = placement
for i in range(annee):
    capital = (capital + (montant * 12)) * (1 + taux)

invest = placement + (montant * 12 * annee)
interet = capital - invest
    
print(f"Le capital acquis avec intérêts est de {round(capital, 2)} euros au bout de {annee} ans avec des versements mensuels de {int(montant)} euros.")
print(f"Les intérêts gagnés au taux annuel de {round(taux * 100, 1)} % sont de {round(interet, 2)} euros.")
print(f"Sans placement avec intérêts le capital acqui serait de {round(invest, 2)} euros.")

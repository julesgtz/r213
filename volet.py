import math

longueur = 2.4
lame_ferme = 0.036
lame_deploye = 0.04
d = 0.06

nb_lame_ferme = math.ceil(longueur / lame_ferme)
print(f"{nb_lame_ferme} lames « entières » sont nécessaires pour le tablier en position fermé.")

longueur_enroule = nb_lame_ferme * lame_deploye
print(f"La longueur à enrouler est donc de {round(longueur_enroule, 2)}m.")

l = 0
for i in range(2):
    l = l + (math.pi * d)
    d = d + ((0.0075 + 0.0015) * 2)

print(f"La nouvelle longueur à enrouler est de {round(longueur_enroule + l, 2)}m.")

l_init = l
c = 2
while l < (longueur_enroule + l_init):
    l = l + (math.pi * d)
    d = d + ((0.0075 + 0.0015) * 2)
    c += 1

print(f"La longueur enroulée est de {round(l, 2)}m, soit {c} tours et un diamètre de {round(d * 100, 2)}cm.")


d = float(input(f"Entrez le diamètre de l'axe en mm: "))/1000
n_tour = int(input("Entrez le nombre de tours: "))
print("\nCalcul de la longueur L pour chaque tour:")

l = 0
for i in range(n_tour):
    l = l + (math.pi * d)
    d = d + ((0.0075 + 0.0015) * 2)
    print(f"Tour {i + 1} - Diamètre [mm]: {int(d * 1000)} - Longueur enroulée [mm]: {int(l * 1000)}")

print(f"\nCalcul de la longueur L par formule: {round(l * 1000, 2)}")

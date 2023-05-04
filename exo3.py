print("Calcul du capital acquis et de ses intérêts versés lorsque les intérêts sont calculés une fois par an.")
plstart=int(input("Entrez le placement de départ : "))
versmens=int(input("Entrez le montant du versement mensuel : "))
txa=float(input("Entrez le taux annuel en % : "))
annee=int(input("entrez le nombre d'années : "))
acquis=(plstart+12*versmens)*((txa+100)/100)

for i in range(annee-1):
    acquis = (acquis + versmens*12)*((txa+100)/100)
capital=plstart+(versmens*annee*12)
intg=acquis-capital
print("Le capital acquis avec intérêts est de ",round(acquis,2),"euros a bout de ",annee,"ans avec des versements mensuels de",versmens,"euros")
print("Les intérêts gagnés au taux annuel de",txa,"% sont de",round(intg,2),"euros")
print("Sans placement avec intérêts le capital acquis serait de",capital,"euros")
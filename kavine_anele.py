
# kavinės čekis ir pvm 

#Užduotis:1. nuskaitykite keturių užsakymų kainas (float), apskaičiuokite sumą
#2. pridėkite 10 % arbat pinigių ir padalykite sumą po lygiai.
# Atspausdinkite su dviem skaičiais po kablelio. (f"{x:.2f}")
#3. Apskaičiuokite kiek iš sumos yra pvm, PVM-21%
# 4.PAkeisti programa taip, kad užsakymu skaičius nežinomas


#Čekis 
cekis = [3.95, 6.00, 8.00, 4.65, 3.60, 3.69]

def bendra_suma(cekis):
    suma = 0
    for i in range(len(cekis)):
        suma += cekis[i]
        
    return suma
print("Bendra čekio suma:", f"{bendra_suma(cekis): .2f}")

# Arbatpinigiai 

suma = bendra_suma(cekis)

def arbatpinigiai(suma):
    su_arbata = suma + (suma*0.1)
    return su_arbata

print("Su arbatpinigais:", f"{arbatpinigiai(suma): .2f}")

# PVM SKAIČIAVIMAS

def pvm(suma): 
    pvms= (suma*21)/100
    return pvms
print("Kiek sumos yra PVM:", f"{pvm(suma): .2f}")
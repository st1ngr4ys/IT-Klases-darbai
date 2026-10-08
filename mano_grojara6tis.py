groj = ["w deszczu maleńkich żółtych kwiatów", "going up the country", "Lovecats"] #numatau, kad atspausdins visą sarašą su skliaustais ir kableliais 

groj.append("historie d'1 soir")
groj.remove("going up the country")

n = len(groj)
print("Kiek dainų: ",n)
print("Mano grojaraštis: ", end="")
for i in range(len(groj)-1):
   print(groj[i], end=", ")
#    break
print(f"{groj[n-1]}.")
#----------------------------------------------------

#tuple yra nepakeičiamas (nei el. pozicijų pakeisi, nei pačių el.) elementų sarašas.
#Rašomas su () arba be skliaustų,
#butinai el. turi būt skiriami ','
#pvz tuple = ("daiktas",) <-- kablelis būtinas!
#tuple vienam saraše gali turėti skirtingus duomenų tipus (str, int, boolean, float)

daina = ("Lovecats", "The Cure", 3.38,)
sarasas = ["Lovecats", "The Cure", 3.38]

print("\n")
print( sarasas[0], sarasas[1], sarasas[2])

print(daina[0], daina[1], daina[2])

# daina[0] = "kita daina" TypeError: 'tuple' object does not support item assignment 

sarasas[0] = "w deszczu maleńkich żółtych kwiatów"

print(sarasas)

# Mieloji mokytoja Monika, jūs esate mano 'asistentas',
# Kodėl yra rodoma klaida bandaydami pakeisti tuple el., o list el. ne, 
# nes tuple yra nekintantis el. sarašas.  

#----------------------------------------------------

Dainu_sar = [("Lovecats", "The Cure", 3.38), ("w deszczu maleńkich żółtych kwiatów", "Myslovitz", 4.35),
              ("going up the country", "Canned heat", 2.51), ("historie d'1 soir", "Bibi Flash", 4.37)]

Dainu_sar.append(("I'm affraid of americans", "David Bowie", 5.00,))

nr = 0
for char, char, num in Dainu_sar:
   nr += 1
   print(nr,". ", f"{char}-{char}({num})") #jei naudociau DI nebuciau tokia laiminga su situo kodu rn

sum = 0.0
for i in range(len(Dainu_sar)):
    t = Dainu_sar[i]
    sum = sum + t[2]
    
print("Grojarascio trukme: ",sum) #turetu but - 19.61

#as tingiu defint funkcijas 

# eee nu davai, netingėk
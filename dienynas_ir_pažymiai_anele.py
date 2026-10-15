# Perskaitykite visus pažymius į sąrašą (naudoti: with open, read().split()). fin
# Raskite: kiekį, sumą, vidurkį, mažiausią ir didžiausią pažymį, kiek yra dešimtukų. fin
# Raskite, kuriame sąrašo indekse pirmą kartą pasitaiko pažymys 4 (tiesinė paieška, nenaudokite index). fin
# Kiek procentų pažymių yra ne mažesni už 8?
# Įrašykite rezultatus į rezultatai.txt. Paleiskite programą antrą kartą ir papildykite failą, o ne perrašykite.

with open("pazymiai.txt", "r") as f:
    pazymiai= f.read().split()

    for i in range(len(pazymiai)):
        pazymiai[i] = int(pazymiai[i])

    print("Pažymių sarašas:", pazymiai)

    kiekis = len(pazymiai)
    print("Pažymių kiekis:", kiekis)

    def suma(pazymiai):
        suma = 0
        for i in range(kiekis):
            suma += pazymiai[i]
        return suma
    print ("Pažymių suma:",suma(pazymiai))

    def vidurkis(pazymiai):
        vid = 0
        vid = suma(pazymiai)//kiekis
        return vid
    print("Pažymių vidurkis:", vidurkis(pazymiai))

    def maziausias(pazymiai):
        min = pazymiai[0]
        for i in pazymiai: 
            if i < min:
                min = i
        return min
    
    print ("Mažiausias pažymys:",maziausias(pazymiai))

    def didziausias(pazymiai):
            max = pazymiai[0]
            for i in pazymiai: 
                if i > max:
                    max = i
            return max
    print("Didžiausias pažymys:",didziausias(pazymiai))

    def kiek10tuku(pazymiai):
        tuku = 0
        for i in pazymiai:
            if i == 10:
                tuku += 1
        return tuku
    print("Kiek dešimtuku iš viso:",kiek10tuku(pazymiai))


    ketvertas = 4
    def ties_paieska(pazymiai, ketvertas):
        for i in range(kiekis):
            if pazymiai[i] == ketvertas:
                return i
        return False 
    print("Pirmo 4-to indeksas:",ties_paieska(pazymiai, ketvertas))

    def procentai(kiekis,pazymiai):
        morethan = 0
        for i in pazymiai:
            if i >= 8:
                morethan +=1
        return morethan 

    print("kiek pažymių daugiau už 8, procentaliai:", (procentai(kiekis,pazymiai)*100)//kiekis, "%")

    with open("rezultatai.txt", "a") as rez:
        rez.writelines([str(kiekis),"\n", str(suma(pazymiai))])
        rez.close()

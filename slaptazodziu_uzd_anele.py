with open("slaptazodziai.txt", "r") as f: #pasizymeti ka daro kaip atidaro faila
    slap_list = f.read().split() #["vfv"vf","fff"]
    kiekis = len(slap_list)

    print(slap_list)
#1. Parašykite funkciją ivertink(slaptazodis),
# kuri grąžina taškus 0–5: ilgis ≥ 10, yra didžioji raidė, mažoji raidė, skaitmuo, specialus simbolis. 
#2. Atmeskite slaptažodžius iš „draudžiamų“ sąrašo (123456, qwerty, slaptazodis…).
#3. Išrūšiuokite failo slaptažodžius į „silpnas / vidutinis / stiprus“.

    def ivertinimas(slapt):
        sk = False
        ilgis = False
        d = False
        m = False
        char = False
        if len(slapt) >= 10:
            ilgis = True

        for i in slapt:
            if i.isdigit():
                sk = True 

        for i in slapt:
            if not i.isalnum() and not i.isalpha():
                char = True

        for i in slapt:
            if i.isupper():
                d = True

        for i in slapt:
            if i.islower():
                m = True

            return ilgis, sk, char, d, m

print(ivertinimas(slap_list[5]))


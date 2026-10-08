n=0
m=1
while n<500:
    print(n)
    x=m+n
    n=m
    m=x

2. 
i=1
while i>0 :
    i=i+1
    print(i)



3. 
slap=""
while slap != "Coding_is_fun":
    slap=input("iveskite teisinga splatazodi: ")
    if slap != "Coding_is_fun":
        print("Neteisinga bandykite dar karta")
    else:
        print("Teisinga!")

4.
i= 10
while i>=1:
    print(i)
    i=i-1
print("start!")

5.
deze=["juoda", "balta","juoda","juoda","balta", "juoda", "juoda", "balta", "balta", "balta","juoda", "balta","juoda","balta", "juoda", "juoda"]
juodi=[]
balti=[]
while len(deze)>0:
    kam=deze.pop()
    if kam == "juoda":
        juodi.append(kam)
    else:
        balti.append(kam)
print("Juodu kamuoliu sk",(len(juodi)))
print("Baltu kamuoliu sk",(len(balti)))

6.
sk=(input("Iveskite teigiama sk, jei norite uzbaigti iveskite q: "))


while sk != "q" and int(sk)>1:
    sk = int(sk)
    if sk % 2 == 0:
        sk = sk // 2
    else:
         sk = sk*3 + 1
print(sk)


def gauk_slaptazodi():
    slap=""
    while slap != "Coding_is_fun":
        slap=input("iveskite teisinga splatazodi: ")
        return slap
   
gauk_slaptazodi()


def patikrink_slaptazodi(userinput):
    slap=""
    if slap != "Coding_is_fun":
        print("Neteisinga bandykite dar karta")
    else:
        print("Teisinga!")
   


patikrink_slaptazodi(userinput="")
gauk_slaptazodi()

bfakjbf

    

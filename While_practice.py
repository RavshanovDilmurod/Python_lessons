""" 

Sana 15:03:26 yil 

Ustoz: Anvar Narzullayev

Mavzu: While, ro'yhatlar va lug'atlar

"""

print("Do'stlaringizni ro'yhatini tuzamiz")

ismlar = []

n = 1

while True:
    
    savol = f"{n}-do'stingizni ismini kiriting"
    
    ism = input(savol)
    
    ismlar.append(ism)
    
    takrorlash = input("Yana ism qo'shasizmi ? (ha/yo'q)")
    
    n += 1
    if takrorlash != "ha":
        break
    
print("Do'stlaringiz ro'yhati:")

for ism in ismlar:
    
    print(ism.title())    
    
    
    
    
    
    
    
    
    
    
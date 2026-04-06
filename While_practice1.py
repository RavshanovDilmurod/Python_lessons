"""
06:04:26 Yil

Mavzu: While , Ro'yhat va lug'atlar

Ustoz: Anvar Narzullayev

"""
print("Do'stlaringizni ro'yhatini tuzamiz :)")

names = []

n = 1

while True:

    question = f"{n}-do'stingizni ismini kiriting: "

    name = input(question)

    names.append(name)

    again = input("Yana ism kiritasizmi ? Ha/Yo'q ")

    n += 1

    if again != "Ha":

        break

print("Do'stlaringizni ro'yhati:")

for name in names:

    print(name.title())
""" 

Sana 03:03:26 yil 

Ustoz : Anvar Narzullayev 

Mavzu: Dictionary ( pythonda lug'at tushunchasi )

 """
 
# en_uz = {'hello':'salom', 'bye':'xayr', 'apple':'olma',}

# # print(en_uz['hello'])

# fruits = {'olma':'15000', 'uzum':'10000', 'nok':'12000'}

# teacher = {'name':'Anvar Narzullayev', 'yosh':'50', 't_yil':'1976'}

# print(teacher['name'].title(), teacher['yosh'], "yoshda va", teacher['t_yil'], "da tug'ilgan")

user_data = []

name = input("Ismingizni kiriting:_")

name = name.title()

age = input("Yoshingizni kiriting:_")

birth = input("Tug'ilgan yilingizni kiriting:_")

user_data.append(name)

user_data.append(age)

user_data.append(birth)

# print(user_data)

print("Ma'lumotlaringizdan birini so'rang: ism, yosh, t_yil tarzda yozing !")

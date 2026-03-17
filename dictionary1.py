# """
# Sana 05:03:2026 yil

# Ustoz: Anvar Narzullayev

# Mavzu: Working with a dictionary

# """

# name = {  
        
#         "name":"Abdulloh",
        
#         "age":"21",
        
#         "birth":"2005"
        
#         }

# for key, value in name.items():
    
#     print("Kalit:", key )
    
#     print("Qiymat:", value)
    
#     print("\n")        
    
udata = {  
    
    'user':'device',
             
    'useer':'devicee', 

    'useeer':'deviceee'
    
               }

# for u, d in user_device.items():
    
#     print("Nomi:", u.title() )
    
#     print("Qurilmasi:", d.title() )

#     print("\n") 

print("Foydalanuvchi nomi:")

for i in udata:
    
    print(i.title())
    

shop = {
        
        'apple':'15k',
        
        'banana':'12k',
        
        'grape':'10k',
        
        'peach':'25k',
        
        'apricot':'5k'
        
        }

list = ['peach', 'apple', 'uzum', 'anor']


for i in shop:
    
    if i in list:
            
        print(i.title(), shop[i])
        
for b in list:
    
    if b not in shop:
        
        print("Uzr do'konimizda", b, "yo'q edi")
    
for i in sorted(shop):
    
    print(i.title())

print(shop.values())

udevice = {
    
    'user':'iphone',
    
    'useer':'galaxy',
    
    'useeer':'nokia',
    
    'useeeer':'galaxy',
    
    'useeeeer':'iphone'
    
    }

print("Foydalanuvchilarimiz foydalanadigan qurrilmalar nomi:")

for i in set(udevice.values()):
    
    print(i.title())

toy = { "ball", "car", "ball" }









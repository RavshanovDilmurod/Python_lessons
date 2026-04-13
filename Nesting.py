"""
Sana 05:03:26 yil 11:52 pm

Ustoz: Anvar Narzullayev 

Mavzu: Nesting

"""
car0 = { 
        'model':'damas',
        
        'rang':'oq',
        
        'yil':'2018',
        
        'narxi':'15.000$'
        }

car1 = {
        'model':'lasetti',
        
        'rang':'qora',
        
        'yil':'2015',
        
        'narxi':'12.000$'
        }

car2 = {    
        'model':'matis',
        
        'rang':'blue',
        
        'yil':'2020',
        
        'narxi':'13.000$'
        }

cars =[ car0, car1, car2 ]

for car in cars:

    print(f'{car['model'].title()} ' 

          f'{car['rang']} rang '

          f'{car['yil']} - yil '

          f'{car['narxi']}')



"""
    Sana 07:05:26 yil

    Mavzu: Funksiyalar

    Ustoz: Anvar Narzullayev

"""


# def hello_world(name):
#
#     print(f"Assalomu aleykum {name.title()}")
#
# hello_world("Hasan")
#
# hello_world("Husan")
#
# hello_world("Akbar")

def toliq_ism_yasa(ism="anvar", familiya="narzullayev"):
    toliq_ism = F"{ism.title()} {familiya.title()}"

    return toliq_ism


talaba = toliq_ism_yasa('anvar', 'narzullayev')

print(talaba)

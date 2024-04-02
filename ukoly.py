# 1)

# def fizzbuzz():
#     cislo = int(input("Zadej číslo: "))
#     if cislo % 3 == 0 and cislo % 5 == 0:
#         return("FizzBuzz")

#     elif cislo % 3 == 0:
#         return("fizz")

#     elif cislo % 5 == 0:
#         return("buzz")

#     else:
#         return(cislo)
    
# print(fizzbuzz())







# 3) Vypiš největší číslo ze tří zadaných čísel
# def nejvetsi_cislo(cislo, cislo2, cislo3):

#     if cislo > cislo2 and cislo > cislo3:
#         return(cislo)

#     elif cislo2 > cislo and cislo2 > cislo3:
#         return(cislo2)

#     elif cislo3 > cislo and cislo3 > cislo2:
#         return(cislo3)

# # cislo = int(input("Zadej číslo: "))
# # cislo2 = int(input("Zadej druhé číslo: "))
# # cislo3 = int(input("Zadej třetí číslo: "))
    
# print(nejvetsi_cislo(input("Zadej číslo: "), input("Zadej druhé číslo: "), input("Zadej třetí číslo: ")))







# 4) Průměr z čísel
# import random
# def prumer_cisel():
#     cisla = []
#     for i in range(random.randint(1, 50)):
#         cisla.append(random.randint(1, 100))
#     pocet_cisel = len(cisla)
#     print(f"Seznam čísel: {cisla}")
#     print(f"Počet čísel v seznamu: {pocet_cisel}")
#     prumer_cisel = sum(cisla) / pocet_cisel
#     return(f"Průměr čísel v seznamu: {prumer_cisel}")

# print(prumer_cisel())







# 5) Funkce nejdelsi_string, která pro 2 zadané textové řetězce vrátí ten nejdelší string
# def nejdelsi_string(string, string2):
#     if len(string) > len(string2):
#         return(string)
#     elif len(string2) > len(string):
#         return(string2)
    
# print(nejdelsi_string(input("Napiš string:"), input("Napiš další string: ")))










# 6) Funkce spoj_stringy, která vrátí nový string vytvořený spojením dvou zadaných stringů seznamem. 
#Jednotlivé stringy jsou spojeny definovaným pojítkem. Využijte i vlastní implementaci bez funkce join().

# def veta():
#     stringy = []
#     strink = str(input("Napiš slovo nebo větu: "))
#     string_2 = str(input("Napiš druhé slovo nebo větu: "))

#     stringy.append(strink)
#     stringy.append(string_2)
#     veta = " ".join(stringy)
#     return (veta)

# print(veta())





#nebo¸





# def veta():
#     strink = str(input("Napiš slovo: "))
#     string_2 = str(input("Napiš druhé slovo: "))

#     face = "(☞ ͡° ͜ʖ ͡°)☞ "

#     veta = f"{strink} {face} {string_2}."
#     return (veta)
# print(veta())




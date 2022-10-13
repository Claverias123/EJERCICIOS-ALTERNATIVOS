#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
from pickle import TRUE


l=(input("Dime una letra\n"))

if l.isupper()==True:
    print("La letra está en mayúscula")
else:
    print("La letra está en minúscula")

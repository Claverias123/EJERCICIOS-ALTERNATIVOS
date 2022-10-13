#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1=int(input("Dime el primer número\n"))
num2=int(input("Dime el segundo número\n"))

if(num2>0):
    print("La división entre ambos es igual a", num1/num2)
if(num2==0):
    print("La división no se puede hacer")
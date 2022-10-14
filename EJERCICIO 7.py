
base=int(input("Dime la base\n"))
exp=int(input("Dime el exponente\n"))

if(exp>0):
    print("El resultado es igual a", base**exp)
if(exp==0):
    print("El resultado es igual a 1")
if(exp<0):
    print("El resultado es igual a", base**-exp)


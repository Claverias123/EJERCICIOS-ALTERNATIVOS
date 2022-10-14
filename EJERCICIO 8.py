

nt=int(input("Dime tu nota\n"))
ed=int(input("Dime tu edad\n"))
car=input("Dime tu género\n")

if(nt>=5) and (ed>=18) and (car=="F"):
    print("ACEPTADO")
elif(nt>=5) and (ed>=18) and (car=="M"):
    print("PROBABLE")
else:
    print("NO ACEPTABLE")

    

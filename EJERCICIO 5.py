#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
usu=input("Dime el usuario\n")
con=input("Dime la contraseña\n")

if(usu=="pepe") and (con=="asdasd"):
    print("Has entrado al sistema")
else:
    print("Error 404")

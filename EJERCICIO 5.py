

usuSecreto="Pepe"
contSecreto="1234"
usuario = input("Dime tu usuario: ")
contrasena= input("Dime tu contraseña: ")

while (usuSecreto!=usuario or contSecreto!=contrasena) :
 if(usuSecreto!=usuario) :
    print("Error en el ususario") 
    usuario = input("Dime tu usuario: ")
 elif (contSecreto!=contrasena):
    print("Error en la contraseña") 
    usuario = input("Dime tu contraseña: ")

print("Usuario y Contraseña correctos")
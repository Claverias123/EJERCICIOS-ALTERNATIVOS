
num1 = (int)(input("Dime un número:\n"))
num2 = (int)(input("Dime otro número:\n"))
num3 = (int)(input("Dime otro número:\n"))
if num1>num2 and num1>num3:
    if num2>num3:
        print("El orden de mayor a menor sería:", num1, "mayor que", num2, "y mayor que", num3)
    else:
        print("El orden de mayor a menor sería:", num1, "mayor que", num3, "y mayor que", num2)
if num2>num1 and num2>num3:
    if num1>num3:
        print("El orden de mayor a menor sería:", num2, "mayor que", num1, "y mayor que", num3)
    else:
        print("El orden de mayor a menor sería:", num2, "mayor que", num3, "y mayor que", num1)        
if num3>num1 and num3>num2:
    if num1>num2:
        print("El orden de mayor a menor sería:", num3, "mayor que", num1, "y mayor que", num2)
    else:
        print("El orden de mayor a menor sería:", num3, "mayor que", num2, " y mayor que", num1)     
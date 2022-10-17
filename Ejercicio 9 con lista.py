vNum=[]

num=int(input("Dime el 1º número\n"))
vNum.append(num)
num=int(input("Dime el 2º número\n"))
vNum.append(num)
num=int(input("Dime el 3º número\n"))
vNum.append(num)

vNum.sort(reverse=True)
print(vNum)
print("EL mayor es", vNum[0])
ultimo=len(vNum)
print("EL menor es", vNum[ultimo-1])

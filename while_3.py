import random

#input

print("-------------------------------------------")
n = int(input("Ingrese un numero entre (1-100): "))
print("-------------------------------------------")

# processing

maq = random.randint(1,100)

i = 1

while n != maq:
    if n < maq:
        print("--------------------------------")
        print("El valor es mayor a el elegido")
        print("--------------------------------")
    else:
        print("--------------------------------")
        print("El valor es menor a el elegido")
        print("--------------------------------")

    print("--------------------------------------------")
    n = int(input("ingrese un numero entre (1-100): ")) 
    print("--------------------------------------------") 


    i += 1

    print("----------------------------------------------------------------")
    print("felicidades ganaste, tuviste {i} intentoss antes de llegar aqui ")
    print("----------------------------------------------------------------")




        
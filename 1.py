# Escribir un programa que lea tres números. Despues debe leer un cuarto número e indicar si el número coincide con alguno de los introducidos con aterioridad, utilizar if y for.

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer numero:"))
num_4 = int(input("Ingrese el cuarto numero "))

coincide = False
for num in [num_1, num_2, num_3]:
    if num == num_4:
        coincide = True
        break
if coincide:
    print("El numero 4 coincide con alguno introducido con anterioridad.")
else:
    print("el numero 4 no coincide con alguno de los introducidos con anterioridad")
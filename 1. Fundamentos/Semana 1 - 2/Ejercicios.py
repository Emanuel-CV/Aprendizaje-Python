# 1. Escribir un programa que pida al usuario su nombre y edad, y luego imprima un mensaje personalizado.

print("Ejercicio 1\n")

nombre = input("Escriba su nombre: ")

print(f"Hola {nombre}. Bienvenido al Roadmap de Python!\n\n")


# 2. Crear un programa que calcule la suma, resta, multiplicación y división de dos números ingresados por el usuario.

print("Ejercicio 2\n")

primer_numero = int(input("Digite el primer numero: "))
segundo_numero = int(input("Digite el segundo numero: "))

print(f"Suma: {primer_numero + segundo_numero}")
print(f"Resta: {primer_numero - segundo_numero}")
print(f"Multiplicacion: {primer_numero * segundo_numero}")
print(f"Division: {primer_numero / segundo_numero}\n\n")

# 3. Escribir un script que determine si un número ingresado es par o impar.

print("Ejercicio 3\n")

numero = int(input("Digite un numero: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")
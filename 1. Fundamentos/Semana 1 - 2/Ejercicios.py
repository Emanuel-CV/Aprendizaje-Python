

# 1. Escribir un programa que pida al usuario su nombre y edad, y luego imprima un mensaje personalizado.

def ejercicio1()  -> None:

    print("Ejercicio 1\n")

    nombre = input("Escriba su nombre: ")

    print(f"Hola {nombre}. Bienvenido al Roadmap de Python!\n\n")


# 2. Crear un programa que calcule la suma, resta, multiplicación y división de dos números ingresados por el usuario.

def ejercicio2() -> None:
    print("Ejercicio 2\n")

    primer_numero = int(input("Digite el primer numero: "))
    segundo_numero = int(input("Digite el segundo numero: "))

    print(f"Suma: {primer_numero + segundo_numero}")
    print(f"Resta: {primer_numero - segundo_numero}")
    print(f"Multiplicacion: {primer_numero * segundo_numero}")
    print(f"Division: {primer_numero / segundo_numero}\n\n")

# 3. Escribir un script que determine si un número ingresado es par o impar.

def ejercicio3() -> None:
    print("Ejercicio 3\n")

    numero = int(input("Digite un numero: "))

    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

# 4. Realizar un programa que convierta temperaturas de Celsius a Fahrenheit.

def ejercicio4() -> None:
    temp_celsius = float(input("\nDigite la temperatura actual en grados Celsius °: "))

    temp_fahrenheit = (temp_celsius * 1.8) + 32

    print(f"\nCelsius: {str(temp_celsius)}C°")
    print(f"Fahrenheit: {str(temp_fahrenheit)}F°\n")

# 5. Desarrollar un script que calcule el área de un círculo dado su radio.

from math import pi

def ejercicio5() -> None:
    radio = float(input("\nDigite el radio del círculo: "))

    area = pi * (radio**2)

    print(f"\nEl área del círculo es {area}")




if __name__ == "__main__":
    # ejercicio1()
    # ejercicio2()
    # ejercicio3()
    # ejercicio4()
    ejercicio5()
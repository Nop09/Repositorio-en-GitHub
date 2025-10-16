import math  # Para usar funciones matemáticas (como raíz cuadrada)

print("=== CALCULADORA COMPLETA ===")

while True:
    print("""
Selecciona una operación:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. Módulo (resto)
7. Raíz cuadrada
8. Salir
""")

    opcion = input("Elige una opción (1-8): ")

    if opcion == "8":
        print("Gracias por usar la calculadora.")
        break

    # Para la raíz cuadrada solo se necesita un número
    if opcion == "7":
        num = input("Introduce un número: ")
        if num.replace(".", "", 1).isdigit():
            num = float(num)
            if num >= 0:
                print(f"Resultado: √{num} = {math.sqrt(num)}")
            else:
                print("Error: no se puede calcular la raíz de un número negativo.")
        else:
            print("Error: entrada no válida.")
        continue

    # Para las demás operaciones se necesitan dos números
    num1 = input("Introduce el primer número: ")
    num2 = input("Introduce el segundo número: ")

    # Validar que los dos sean números
    if not (num1.replace(".", "", 1).isdigit() and num2.replace(".", "", 1).isdigit()):
        print("Error: por favor, introduce solo números.")
        continue

    num1 = float(num1)
    num2 = float(num2)

    # Realizar la operación según la opción
    if opcion == "1":
        print(f"Resultado: {num1} + {num2} = {num1 + num2}")
    elif opcion == "2":
        print(f"Resultado: {num1} - {num2} = {num1 - num2}")
    elif opcion == "3":
        print(f"Resultado: {num1} × {num2} = {num1 * num2}")
    elif opcion == "4":
        if num2 != 0:
            print(f"Resultado: {num1} ÷ {num2} = {num1 / num2}")
        else:
            print("Error: no se puede dividir entre cero.")
    elif opcion == "5":
        print(f"Resultado: {num1}^{num2} = {num1 ** num2}")
    elif opcion == "6":
        print(f"Resultado: {num1} % {num2} = {num1 % num2}")
    else:
        print("Error: opción no válida.")
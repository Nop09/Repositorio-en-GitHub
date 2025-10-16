# Formulario en consola: Nombre, Apellido y Edad

# Pedir los datos al usuario
nombre = input("Ingrese su nombre: ").strip()
apellido = input("Ingrese su apellido: ").strip()
edad = input("Ingrese su edad: ").strip()

# Verificar que la edad sea un número
if edad.isdigit():
    edad = int(edad)
    print("\n--- DATOS INGRESADOS ---")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"Edad: {edad} años")
else:
    print("\n Error: la edad debe ser un número válido.")
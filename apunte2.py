# ==============================================================================
# EJERCICIO DE PRÁCTICA 2: SISTEMA DE GESTIÓN DE ENTRADAS - TEATRO MUNICIPAL
# Aplica: Menú con while, Tip 2 (validación numérica), Tip 3 (try/except)
# ==============================================================================

print("¡Bienvenido al sistema de gestión de entradas del Teatro Municipal!")

CAPACIDAD_MAXIMA = 150
entradas_disponibles = 150
historial_ventas = 0
opcion = 0

while opcion != 5:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1.- Entradas disponibles.")
    print("2.- Comprar entradas.")
    print("3.- Devolver entradas.")
    print("4.- Historial de ventas.")
    print("5.- Salir.")

    # Validar opción del menú con try/except (Tip 3)
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Ha ocurrido un error: debe ingresar un número entero.")
        opcion = 0
        continue

    # Opción 1: Mostrar disponibles
    if opcion == 1:
        print(f"Actualmente hay {entradas_disponibles} entradas disponibles.")

    # Opción 2: Comprar (Restar stock, sumar historial)
    elif opcion == 2:
        try:
            cantidad = int(input("Ingrese la cantidad de entradas a comprar: "))
            if cantidad <= 0:
                print("Error: La cantidad debe ser mayor a 0.")
            elif cantidad > entradas_disponibles:
                print(f"No hay suficiente capacidad disponible. Solo quedan {entradas_disponibles} entradas.")
            else:
                entradas_disponibles -= cantidad
                historial_ventas += cantidad
                print(f"¡Compra exitosa! Has adquirido {cantidad} entradas.")
        except ValueError:
            print("Ha ocurrido un error: debe ingresar un número entero.")

    # Opción 3: Devolver (Sumar stock sin pasar el máximo, restar historial)
    elif opcion == 3:
        try:
            cantidad = int(input("Ingrese la cantidad de entradas a devolver: "))
            if cantidad <= 0:
                print("Error: La cantidad a devolver debe ser mayor a 0.")
            elif (entradas_disponibles + cantidad) > CAPACIDAD_MAXIMA:
                print(f"Error: No se puede superar la capacidad máxima del teatro ({CAPACIDAD_MAXIMA} entradas).")
            else:
                entradas_disponibles += cantidad
                historial_ventas -= cantidad
                print(f"Devolución procesada. Se han liberado {cantidad} entradas.")
        except ValueError:
            print("Ha ocurrido un error: debe ingresar un número entero.")

    # Opción 4: Historial de la sesión
    elif opcion == 4:
        print(f"Total de entradas vendidas activas en esta sesión: {historial_ventas}")

    # Opción 5: Salir
    elif opcion == 5:
        print("Gracias por utilizar nuestro software, hasta la próxima.")

    # Opción fuera de rango (ej: 8 o -1)
    else:
        print("Opción inválida. Por favor elija entre 1 y 5.")
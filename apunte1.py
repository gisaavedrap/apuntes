# ==============================================================================
# EJERCICIO DE PRÁCTICA 1: REGISTRO DE VEHÍCULOS EN TALLER MECÁNICO
# Aplica: Tip 1 (len), Tip 2 (entero positivo), Tip 3 (try/except), Tip 4 (espacios)
# ==============================================================================

# Contadores automáticos
autos_antiguos = 0
autos_modernos = 0

# 1. Validar cantidad de vehículos a registrar (Entero positivo + try/except)
cantidad = 0
while cantidad <= 0:
    try:
        cantidad = int(input("¿Cuántos vehículos desea registrar?: "))
        if cantidad <= 0:
            print("¡Herramienta inválida! Ingresa un entero positivo para continuar el registro.")
    except ValueError:
        print("¡Herramienta inválida! Ingresa un entero positivo para continuar el registro.")
        cantidad = 0

# 2. Ciclo de registro por cada vehículo
for i in range(cantidad):
    print(f"\n--- Registro del vehículo {i + 1} ---")
    
    # Validar Código de Chasis: mínimo 8 caracteres y sin espacios
    codigo_valido = False
    while not codigo_valido:
        codigo = input("Ingrese el código de chasis (mínimo 8 caracteres, sin espacios): ")
        
        # Verificamos largo mínimo (Tip 1) y que no tenga espacios (Tip 4)
        if len(codigo) >= 8 and " " not in codigo:
            codigo_valido = True
        else:
            print("¡Código incorrecto! Debe tener al menos 8 caracteres y no contener espacios.")

    # Validar Años de Antigüedad (Entero positivo + try/except)
    antiguedad = 0
    while antiguedad <= 0:
        try:
            antiguedad = int(input("Ingrese los años de antigüedad del vehículo: "))
            if antiguedad <= 0:
                print("¡Error mecánico! Ingresa un número entero positivo para la antigüedad.")
        except ValueError:
            print("¡Error mecánico! Ingresa un número entero positivo para la antigüedad.")
            antiguedad = 0

    # 3. Clasificación del vehículo
    if antiguedad > 10:
        print(f"Vehículo {codigo} clasificado como: Auto Clásico.")
        autos_antiguos += 1
    else:
        print(f"Vehículo {codigo} clasificado como: Auto Moderno.")
        autos_modernos += 1

# 4. Salida final
print(f"\n¡El taller cuenta con {autos_antiguos} Autos Clásicos y {autos_modernos} Autos Modernos! ¡A reparar!")
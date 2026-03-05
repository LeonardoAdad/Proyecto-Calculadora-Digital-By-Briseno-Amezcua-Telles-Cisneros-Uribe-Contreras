"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:
- Estudiante 1: [Leonardo Adad Briseño Amezcua] - Estructura Principal y Gestión de Datos
- Estudiante 2: [Diego Telles Cisneros] - Funciones Matemáticas
- Estudiante 3: [Maximo Fernando Uribe Contreras] - Conversores y Sistema de Historial

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

import os
from datetime import datetime

# Variable global para almacenar historial (lista de strings)
historial = []

# ============================================
# SECCIÓN 1: FUNCIONES MATEMÁTICAS (Estudiante 2)
# ============================================

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero.")
    return a % b

def potencia(a, b):
    return a ** b


# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS (Estudiante 2)
# ============================================

def decimal_a_binario(numero):
    if numero == 0:
        return "0"  
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero //= 2
    return binario




def decimal_a_hexadecimal(numero):

    if numero == 0:

        return "0"  
    
    hexadecimal = ""
    caracteres = "0123456789ABCDEF"    

    while numero > 0:
        residuo = numero % 16
        hexadecimal = caracteres[residuo] + hexadecimal
        numero //= 16
        
    return hexadecimal


def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        bit = binario[longitud - 1 - i]
        if bit == '1':
            decimal += 2 ** i
    return decimal
 
def hexadecimal_a_decimal(hexadecimal):
    hexadecimal = hexadecimal.upper()
    decimal = 0
    caracteres = "0123456789ABCDEF"
    longitud = len(hexadecimal)

    for i in range(longitud):
        
        digito = hexadecimal[longitud - 1 - i]
        valor = caracteres.find(digito)

        if valor == -1:

            raise ValueError(f"Carácter inválido en hexadecimal: {digito}")
        decimal += valor * (16 ** i)

    return decimal

# ============================================
# SECCIÓN 3: CONVERSIÓN DE UNIDADES (Estudiante 3)
# ============================================

def kilobytes_a_megabytes(kb):
    return kb / 1024

def megabytes_a_gigabytes(mb):
    return mb / 1024

def gigabytes_a_megabytes(gb):
    return gb * 1024

def megabytes_a_kilobytes(mb):
    return mb * 1024

def kilobytes_a_bytes(kb):
    return kb * 1024

def bytes_a_kilobytes(kb):
    return kb / 1024

# ============================================
# SECCIÓN 4: GESTIÓN DE HISTORIAL (Estudiante 3)
# ============================================

def agregar_al_historial(operacion, num1, num2, resultado):
    global historial

    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Diccionario de simbolos
    simbolos = {
        "Suma": "+",
        "Resta": "-",
        "Multiplicación": "*",
        "División": "/",
        "Módulo": "%",
        "Potencia": "**"
    }

    simbolo = simbolos.get(operacion, "?")

    entrada = f"{fecha_hora} | {operacion}: {num1} {simbolo} {num2} = {resultado}"

    historial.append(entrada)

    if len(historial) > 10:
        historial.pop(0)

    guardar_historial_archivo()


def mostrar_historial():
    global historial

    if not historial:
        print("\nEl historial está vacío.")
        return

    print("\nHISTORIAL DE OPERACIONES:")
    print("-" * 50)

    for i, operacion in enumerate(historial, start=1):
        print(f"{i}. {operacion}")


def limpiar_historial():
    global historial
    historial.clear()

# ============================================
# SECCIÓN 5: GESTIÓN DE ARCHIVOS (Estudiante 3)
# ============================================

def guardar_historial_archivo():
    global historial

    # Comprobar si existe la carpeta y crear una si no existe
    if not os.path.exists("datos"):
        os.makedirs("datos")

    with open("datos/historial.txt", "w", encoding="utf-8") as archivo:
        for linea in historial:
            archivo.write(linea + "\n")


def cargar_historial_archivo():
    global historial

    if os.path.exists("datos/historial.txt"):
        with open("datos/historial.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

            historial.clear()

            for linea in lineas:
                historial.append(linea.strip())

            if len(historial) > 10:
                historial[:] = historial[-10:]


# ============================================
# SECCIÓN 6: VALIDACIÓN (Estudiante 1)
# ============================================

def validar_numero(mensaje):
    """Solicita y valida un número (acepta decimales)."""
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print(" Error: Ingrese un número válido.")

def validar_numero_entero(mensaje):
    """Solicita y valida un número entero al usuario."""
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print(" Error: Ingrese un número entero válido.")
# ============================================
# SECCIÓN 7: MENÚS (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("   CALCULADORA MULTIFUNCIONAL v2.0")
    print("="*60)
    print("\nMENÚ PRINCIPAL:")
    print("1. Calculadora Básica")
    print("2. Conversor de Unidades de Datos")
    print("3. Calculadora de Sistemas Numéricos")
    print("4. Ver Historial")
    print("5. Limpiar Historial")
    print("6. Salir")
    print("-"*60)
 
def menu_calculadora_basica():
    """Menú y lógica de la calculadora básica"""
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo (residuo)")
    print("6. Potencia")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione operación: ")

    if opcion == "7":
        return
    
    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print(" Opción inválida.")
        return

    num1 = validar_numero("Ingrese el primer número: ")
    num2 = validar_numero("Ingrese el segundo número: ")

    try:
        if opcion == "1":
            resultado = sumar(num1, num2)
            operacion = "Suma"
        elif opcion == "2":
            resultado = restar(num1, num2)
            operacion = "Resta"
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            operacion = "Multiplicación"
        elif opcion == "4":
            resultado = dividir(num1, num2)
            operacion = "División"
        elif opcion == "5":
            resultado = modulo(num1, num2)
            operacion = "Módulo"
        elif opcion == "6":
            resultado = potencia(num1, num2)
            operacion = "Potencia"

        print(f"\n El resultado es: {resultado}")
        agregar_al_historial(operacion, num1, num2, resultado)

    except ValueError as e:
        print(f"\n Error: {e}")


def menu_conversor_unidades():
    """Menú y lógica del conversor de unidades"""
    print("\n--- CONVERSOR DE UNIDADES DE DATOS ---")
    print("1. Bytes a Kilobytes")
    print("2. Kilobytes a Megabytes")
    print("3. Megabytes a Gigabytes")
    print("4. Gigabytes a Megabytes")
    print("5. Megabytes a Kilobytes")
    print("6. Kilobytes a Bytes")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "7":
        return
        
    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print(" Opción inválida.")
        return

    valor = validar_numero_entero("Ingrese la cantidad a convertir: ")

    if opcion == "1":
        resultado = bytes_a_kilobytes(valor)
        print(f"\n {valor} Bytes = {resultado:.4f} Kilobytes")
    elif opcion == "2":
        resultado = kilobytes_a_megabytes(valor)
        print(f"\n {valor} Kilobytes = {resultado:.4f} Megabytes")
    elif opcion == "3":
        resultado = megabytes_a_gigabytes(valor)
        print(f"\n {valor} Megabytes = {resultado:.4f} Gigabytes")
    elif opcion == "4":
        resultado = gigabytes_a_megabytes(valor)
        print(f"\n {valor} Gigabytes = {resultado:.4f} Megabytes")
    elif opcion == "5":
        resultado = megabytes_a_kilobytes(valor)
        print(f"\n {valor} Megabytes = {resultado:.4f} Kilobytes")
    elif opcion == "6":
        resultado = kilobytes_a_bytes(valor)
        print(f"\n {valor} Kilobytes = {resultado:.4f} Bytes")


def menu_sistemas_numericos():
    """Menú y lógica de conversión de sistemas numéricos"""
    print("\n--- CALCULADORA DE SISTEMAS NUMÉRICOS ---")
    print("1. Decimal a Binario")
    print("2. Decimal a Hexadecimal")
    print("3. Binario a Decimal")
    print("4. Hexadecimal a Decimal")
    print("5. Volver al menú principal")

    opcion = input("\nSeleccione una opción: ")

    if opcion == "5":
        return

    try:
        if opcion == "1":
            num = validar_numero_entero("Ingrese el número decimal: ")
            print(f"\n En binario es: {decimal_a_binario(num)}")
        elif opcion == "2":
            num = validar_numero_entero("Ingrese el número decimal: ")
            print(f"\n En hexadecimal es: {decimal_a_hexadecimal(num)}")
        elif opcion == "3":
            binario = input("Ingrese el número binario (solo 0s y 1s): ")
            print(f"\n En decimal es: {binario_a_decimal(binario)}")
        elif opcion == "4":
            hexadecimal = input("Ingrese el número hexadecimal: ")
            print(f"\n En decimal es: {hexadecimal_a_decimal(hexadecimal)}")
        else:
            print(" Opción inválida.")
    except ValueError as e:
        print(f"\n Error: {e}")

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  CALCULADORA MULTIFUNCIONAL - Versión Avanzada".center(58) + "║")
    print("║" + " "*58 + "║")
    print("║" + "  Con historial, funciones y persistencia de datos".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")

    # Cargar historial al iniciar
    cargar_historial_archivo()
    print("\n Historial cargado desde archivo.")

    continuar = True

    while continuar:
        mostrar_menu_principal() # Funciona?

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_calculadora_basica()

        elif opcion == "2":
            menu_conversor_unidades()

        elif opcion == "3":
            menu_sistemas_numericos()

        elif opcion == "4":
            mostrar_historial()

        elif opcion == "5":
            confirmacion = input("\n¿Está seguro de limpiar el historial? (s/n): ")
            if confirmacion.lower() == "s":
                limpiar_historial()
                print(" Historial limpiado.")
                
        elif opcion == "6":
            print("\n Guardando historial...")
            guardar_historial_archivo()
            print(" Historial guardado en datos/historial.txt")
            print("\n¡Gracias por usar la Calculadora Multifuncional!")
            print("¡Hasta pronto! 👋")
            continuar = False

        else:
            print("\n Opción inválida. Por favor seleccione 1-6.")

    print("\nPrograma terminado.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

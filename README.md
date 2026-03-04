Calculadora Multifuncional v2.0

Una calculadora avanzada e interactiva desarrollada en Python con múltiples funcionalidades, historial persistente y manejo de diferentes sistemas numéricos.



- Leonardo Adad Briseño Amezcua - Estructura Principal y Gestión de Datos
- Diego Telles Cisneros - Funciones Matemáticas
- Maximo Fernando Uribe Contreras - Conversores y Sistema de Historial

*Proyecto de Tecnología Digital - Universidad de Guadalajara*

--------------------------------------------------------------------------------------------------------

Características Principales

La calculadora cuenta con 4 módulos principales:

 1. Calculadora Básica
Realiza operaciones matemáticas fundamentales:
- **Suma:** Sumar dos números
- **Resta:** Restar dos números
- **Multiplicación:** Multiplicar dos números
- **División:** Dividir dos números (con validación contra división por cero)
- **Módulo:** Obtener el residuo de una división
- **Potencia:** Elevar un número a una potencia

2. Conversor de Unidades de Datos
Convierte entre diferentes unidades de almacenamiento digital:
- **Bytes ↔ Kilobytes (KB)**
- **Kilobytes ↔ Megabytes (MB)**
- **Megabytes ↔ Gigabytes (GB)**

Conversiones incluidas:
- **Bytes a Kilobytes**
- **Kilobytes a Megabytes**
- **Megabytes a Gigabytes**
- **Gigabytes a Megabytes**
- **Megabytes a Kilobytes**
- **Kilobytes a Bytes**

3. Calculadora de Sistemas Numéricos
Convierte números entre diferentes sistemas de numeración:
- **Decimal ↔ Binario**: Convierte números decimales a binario y viceversa
- **Decimal ↔ Hexadecimal**: Convierte números decimales a hexadecimal y viceversa

4. Sistema de Historial
- **Ver Historial**: Muestra las últimas 10 operaciones realizadas
- **Limpiar Historial**: Elimina todas las operaciones registradas
- **Persistencia**: Guarda automáticamente el historial en `datos/historial.txt`
- **Registro Temporal**: Cada operación incluye fecha y hora exacta

---

 Cómo Usar

 Requisitos
- Python 3.6 o superior
- Sistema operativo: Windows, macOS, Linux

Instalación
1. Descarga los archivos del proyecto
2. No requiere dependencias externas (usa módulos estándar de Python)

Ejecución
En la terminal o PowerShell, ejecuta:
```bash
python calculadora.py
```

 Flujo de Uso

1. **Inicio**: El programa carga automáticamente el historial previo
2. **Menú Principal**: Selecciona una opción (1-6):
   - Opción 1: Accede a Calculadora Básica
   - Opción 2: Accede a Conversor de Unidades
   - Opción 3: Accede a Calculadora de Sistemas Numéricos
   - Opción 4: Visualiza el Historial
   - Opción 5: Limpia el Historial
   - Opción 6: Salir del programa

3. **Operaciones**: 
   - Ingresa los números solicitados
   - El resultado se muestra inmediatamente
   - La operación se guarda en el historial automáticamente

4. **Cierre**: Al salir, el historial se guarda automáticamente en `datos/historial.txt`

---

  Estructura de Archivos

```
calculadora.py           # Archivo principal del programa
README.md               # Este archivo (documentación)
datos/
  └── historial.txt     # Archivo que almacena el historial de operaciones
ejemplos/
  └── Lol.py           # Ejemplos o referencias
```

---

Funciones Clave

Sección 1: Funciones Matemáticas
```python
sumar(a, b)            # Suma dos números
restar(a, b)           # Resta dos números
multiplicar(a, b)      # Multiplica dos números
dividir(a, b)          # Divide dos números
modulo(a, b)           # Obtiene el residuo
potencia(a, b)         # Calcula potencia
```
Sección 2: Conversión de Sistemas Numéricos
```python
decimal_a_binario(numero)              # Convierte decimal a binario
decimal_a_hexadecimal(numero)          # Convierte decimal a hexadecimal
binario_a_decimal(binario)             # Convierte binario a decimal
hexadecimal_a_decimal(hexadecimal)     # Convierte hexadecimal a decimal
```

Sección 3: Conversión de Unidades de Datos
```python
kilobytes_a_megabytes(kb)              # Convierte KB a MB
megabytes_a_gigabytes(mb)              # Convierte MB a GB
gigabytes_a_megabytes(gb)              # Convierte GB a MB
megabytes_a_kilobytes(mb)              # Convierte MB a KB
kilobytes_a_bytes(kb)                  # Convierte KB a Bytes
bytes_a_kilobytes(kb)                  # Convierte Bytes a KB
```

Sección 4: Gestión de Historial
```python
agregar_al_historial(operacion, num1, num2, resultado)  # Agrega operación
mostrar_historial()                    # Muestra últimas 10 operaciones
limpiar_historial()                    # Vacía el historial
guardar_historial_archivo()            # Guarda historial en archivo
cargar_historial_archivo()             # Carga historial desde archivo
```

---

Validación de Entrada

El programa incluye validaciones para:
-  Números inválidos o no numéricos
-  División por cero
-  Módulo por cero
-  Caracteres inválidos en conversiones de sistemas numéricos

Si ocurre un error, el programa lo indica con un mensaje de error  y solicita reintentar.

---

Historial

El historial guarda:
- **Fecha y Hora**: Cuándo se realizó la operación
- **Tipo de Operación**: Suma, Resta, etc.
- **Operandos**: Los números utilizados
- **Resultado**: El resultado de la operación
- **Símbolo**: Representación simbólica de la operación

**Ejemplo de registro:**
```
2026-03-03 14:30:45 | Suma: 10 + 5 = 15
2026-03-03 14:31:12 | División: 100 / 4 = 25.0
2026-03-03 14:32:00 | Decimal a Binario: 8 = 1000
```

**Límite**: El historial almacena máximo 10 operaciones en memoria. Las más antiguas se eliminan automáticamente al exceder este límite.

---

Ejemplos de Uso

Ejemplo 1: Calculadora Básica
```
Seleccione operación: 1 (Suma)
Ingrese el primer número: 15
Ingrese el segundo número: 8
 El resultado es: 23
```
 Ejemplo 2: Conversión de Unidades
```
Seleccione una opción: 2 (Kilobytes a Megabytes)
Ingrese la cantidad a convertir: 2048
 2048 Kilobytes = 2.0 Megabytes
```

Ejemplo 3: Sistemas Numéricos
```
Seleccione una opción: 1 (Decimal a Binario)
Ingrese el número decimal: 42
 En binario es: 101010
```

---

Notas Técnicas

- **Lenguaje**: Python 3.6+
- **Módulos utilizados**: `os`, `datetime`
- **Codificación**: UTF-8
- **Tipo de aplicación**: Consola interactiva
- **Almacenamiento**: Archivos de texto (historial.txt)

---

 Posibles Mejoras Futuras

- Interfaz gráfica (GUI) con Tkinter o PyQt
- Base de datos para historial más extenso
- Operaciones más complejas (trigonometría, logaritmos)
- Cálculo de expresiones matemáticas complejas
- Exportar historial en diferentes formatos (CSV, JSON)
- Soporte para múltiples usuarios con login

---

 Licencia

Proyecto académico - Libre para uso educativo

---


---

**Última actualización**: Febrero 2026  
**Versión**: 2.0

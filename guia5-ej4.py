# Ejercicio 4
# Reemplace el ejercicio 3 por una implementación con parámetros pasados por
# consola usando la librería sys.

import sys 

sueldo = int(sys.argv[1])
rango = int(sys.argv[2])

print("el sueldo es:", sueldo)
print("el rango es:", rango)

if rango == 1:
    resultado = round(sueldo * 0.83, 2)
elif rango == 2:
    resultado = round(sueldo * 1.2, 2)
else:
    resultado = round(sueldo * 5, 2)

print("el resultado es:", resultado)

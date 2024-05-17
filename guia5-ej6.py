print("operaciones posiles:")
print("suma (s)")
print("resta (r)")
print("multiplicacion (m)")
print("division (d)")
      
operacion = input("escriba la letra referencia: ")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "error"

a = float(input("primer numero:"))
b = float(input("segundo numero:"))

if operacion == "s":
        resultado = suma(a, b)
elif operacion == "r":
        resultado = resta(a, b)
elif operacion == "m":
        resultado = multiplicacion(a, b)
else:
        resultado = division(a, b)

print("El resultado es:", resultado)



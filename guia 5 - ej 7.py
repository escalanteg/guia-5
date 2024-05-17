# guia 5 - ej 7

# Cree un programa en Python que imprima la hora del sistema, estado de memoria
# RAM y almacenamiento disponible en la partición montada en “/”.

import datetime
import psutil

hora = datetime.datetime.now().strftime("%H:%M:%S")
print("hora:", hora)

memoria = psutil.virtual_memory()
print("memoria RAM total:", memoria.total / (1024 ** 3), "GB,",
      "memoria RAM disponible:", memoria.available / (1024 ** 3), "GB")

almacenamiento = psutil.disk_usage('/')
print("almacenamiento disponible en la particion '/':", almacenamiento.free / (1024 ** 3), "GB")

#ejercicio 5
# Cree un programa en BASH, que invoque a tres programas en python, donde cada
# uno es un contador (con avance cada un segundo) hasta un número que se pase
# por entrada. Cada programa en python debe imprimir el contador
# segundo-a-segundo.

# a. Identifique el PID de cada proceso python
# b. ¿Los procesos de ejecutan de manera secuencial?, ¿Cómo hacer para que
# corran todos a la vez?


#!/bin/bash

echo "ingrese el número de segundos a los que se corta el conteo:"
read segundos


python3 /home/guada-escalante/Downloads/guia5-ej5-python.py &
pid_1=$!
python3 /home/guada-escalante/Downloads/"guia5-ej5-python(2).py" &
pid_2=$!
python3 /home/guada-escalante/Downloads/"guia5-ej5-python(3).py" &
pid_3=$!



echo "el PID del programa1 es: $pid_1"
echo "el PID del programa2 es: $pid_2"
echo "el PID del programa3 es: $pid_3"


sleep $segundos

kill $pid_1
kill $pid_2
kill $pid_3

#los pogramas se ejecutan todos a la vez. para que sea secuencial habria que poner el "kill" de cada uno antes de comenzar el siguiente.



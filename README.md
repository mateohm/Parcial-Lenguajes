# Parcial-Lenguajes

## Punto 1
 ### 1. Crear el archivo de prueba con tokens:

echo "+\n++\n123\n45.67" > token.txt

 ### 2. Ejecutar el programa AWK:

awk -f token.awk token.txt

### Punto 2

1. Generar el código en C con LEX:

lex lambda.l

2. Compilar el archivo generado:

gcc lex.yy.c -o lambda -ll

3. Crear un archivo de prueba:

echo "square = lambda x: x ** 2" > archivo.txt

4. Ejecutar el analizador:

./lambda < archivo.txt

### Punto 3 

1. Compilar el programa en C:

gcc miprograma.c -o miprograma

2. Crear un archivo de prueba:

echo "arroz arroz arroz pan arroz" > texto.txt

3. Ejecutar el programa con una palabra clave:

./programa texto.txt ejemplo

### Punto 4
1. Compilar y ejecutar el programa en C:

gcc suma.c -o suma
./suma

2. Ejecutar el programa en Python:

python3 suma.py

Comparacion entre Python y C

En la comparación de rendimiento entre un lenguaje compilado (C) y un lenguaje interpretado (Python), se observó que el código en C se ejecutó significativamente más rápido que el de Python. Esto se debe a que C es un lenguaje compilado, lo que significa que su código se traduce directamente a lenguaje de máquina antes de ejecutarse, optimizando el rendimiento. En cambio, Python es un lenguaje interpretado, lo que implica que su código se analiza y ejecuta línea por línea en tiempo de ejecución.

En conclusion C será más rápido porque es compilado.
Python será más lento porque es interpretado.


### Punto 5 

1. Generar los archivos con ANTLR (Python):

antlr4 -Dlanguage=Python3 Complex.g4

2. Ejecutar el analizador con una expresión de prueba:

python3 complex_calc.py



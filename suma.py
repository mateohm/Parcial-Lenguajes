import time

suma = 0
inicio = time.time()

for i in range(1, 100000001):
    suma += i

fin = time.time()
print("Suma en Python:", suma)
print("Tiempo:", fin - inicio, "segundos")

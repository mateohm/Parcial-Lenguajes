#include <stdio.h>
#include <time.h>

int main() {
    long long suma = 0;
    clock_t inicio = clock();

    for (long long i = 1; i <= 100000000; i++) {
        suma += i;
    }

    clock_t fin = clock();
    printf("Suma en C: %lld\n", suma);
    printf("Tiempo: %lf segundos\n", (double)(fin - inicio) / CLOCKS_PER_SEC);
    return 0;
}

#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s archivo key\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (file == NULL) {
        printf("Error al abrir el archivo.\n");
        return 1;
    }

    char palabra[100], linea[1000];
    int contador = 0;

    strcpy(palabra, argv[2]);

    while (fscanf(file, "%s", linea) != EOF) {
        if (strcmp(linea, palabra) == 0) {
            contador++;
        }
    }

    fclose(file);
    printf("La palabra '%s' se repite %d veces en el texto.\n", palabra, contador);
    return 0;
}

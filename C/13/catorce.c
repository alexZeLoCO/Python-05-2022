#include <stdio.h>

/*
Pide la cantidad de numeros a introducir.
Pide los numeros.
Muestra cuantos negativos se han introducido.
*/
int main()
{
    int cantidad_numeros;
    int numero_actual;
    int contador_negativos;

    printf("Cuantos valores se van a introducir? ");
    scanf("%d", &cantidad_numeros);

    if (cantidad_numeros < 0)
    {
        printf("Imposible!");
        printf("Cuantos valores se van a introducir? ");
        scanf("%d", &cantidad_numeros);
    }

    for (int i = 0; i < cantidad_numeros; i++)
    {
        printf("Escribe el numero: ");
        scanf("%d", &numero_actual);

        if (numero_actual < 0)
        {
            contador_negativos = contador_negativos + 1;
        }
    }

    if (contador_negativos == 1)
    {
        printf("Ha escrito %d numero negativos", contador_negativos);
    }
    else
    {
        printf("Ha escrito %d numeros negativos", contador_negativos);
    }
    return 0;
}
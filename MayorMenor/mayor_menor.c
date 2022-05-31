#include <stdio.h>
#include <stdlib.h>

int main()
{
    int objetivo = 150;
    int n;
    int win = 0; // 1 si ha ganado, 0 si no

    for (int ronda = 0; ronda < 5 && !win; ronda++)
    {
        printf("Intentos restantes: %d\nIntroduzca un numero: ", 5 - ronda);
        scanf("%d", &n);

        if (n == objetivo)
        {
            win = 1;
        }
        else
        {
            if (n < objetivo)
            {
                printf("El numero objetivo es mayor que %d.\n", n);
            }
            else
            {
                printf("El numero objetivo es menor que %d.\n", n);
            }
        }
    }
    if (win)
    {
        printf("Enhorabuena! El numero correcto era %d.\n", objetivo);
    }
    else
    {
        printf("Se ha quedado sin intentos! El numero correcto era %d.\n", objetivo);
    }
    return 0;
}
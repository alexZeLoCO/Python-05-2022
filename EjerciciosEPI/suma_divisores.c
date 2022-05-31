#include <stdio.h>

int main()
{
    int n;
    int s;
    s = 0;

    printf("Introduzca un numero: ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            s += i;
        }
    }

    printf("La suma de todos los divisores de %d es %d\n", n, s);
}
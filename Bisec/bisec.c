#include <stdio.h>
#include <math.h>

double f(double x)
{
    return -pow(x, 5) + 2 * pow(x, 4) - 3 * pow(x, 3) + 4 * pow(x, 2) - 5 * x + 7;
}

int main()
{
    int iters;
    double a = -2;
    double b = 2;
    double c = 0;

    printf("Introduce el numero de iteraciones a realizar: ");
    scanf("%d", &iters);

    printf("%f", f(1));

    for (int i = 0; i < iters; i++)
    {
        c = (a + b) / 2;
        if (f(a) * f(c) < 0)
        {
            b = c;
        }
        else
        {
            a = c;
        }
    }

    printf("Tras %d iteraciones, se ha calculado la raiz x=%f, f(x)=%f", iters, c, f(c));
    return 0;
}

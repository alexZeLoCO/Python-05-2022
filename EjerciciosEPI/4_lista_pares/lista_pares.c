#include <stdio.h>

int main () {
	int a;
	int b;

	printf("Introduzca el primer numero: ");
	scanf("%d", &a);

	printf("Introduzca el segundo numero: ");
	scanf("%d", &b);

	printf("Numeros pares entre %d y %d:\n", a, b);

	for (int i = a ; i <= b ; i++)
	{
		if (i % 2 == 0)
		{
			printf("%d\n", i);
		}
	}
	return 0;
}

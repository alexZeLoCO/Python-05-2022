#include <stdio.h>

int main ()
{
	float nota;

	printf("Introduzca nota: ");
	scanf("%f", &nota);

	if (nota < 5)
	{
		printf("Suspenso\n");
	}
	else
	{
		if (nota < 7)
		{
			printf("Aprobado\n");
		}
		else
		{
			if (nota < 9)
			{
				printf("Notable\n");
			}
			else
			{
				printf("Matricula de Honor\n");
			}
		}
	}
	return 0;
}


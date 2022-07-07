#include <stdio.h>

int main () {
	int fila;
	int col;

	printf("Introduzca fila: ");
	scanf("%d", &fila);

	printf("Introduzca columna: ");
	scanf("%d", &col);
	
	if (fila == 1)
	{
		if (col == 1)
		{
			printf("Alfa");
		}
		if (col == 2)
		{
			printf("Beta");
		}
		if (col == 3)
		{
			printf("Lambda");
		}
	}
	if (fila == 2)
	{
		if (col == 1)
		{
			printf("Beta");
		}
		if (col == 2)
		{
			printf("Lambda");
		}
		if (col == 3)
		{
			printf("Alfa");
		}
	}
	if (fila == 3)
	{
		if (col == 1)
		{
			printf("Lambda");
		}
		if (col == 2)
		{
			printf("Alfa");
		}
		if (col == 3)
		{
			printf("Beta");
		}
	}
	return 0;
}



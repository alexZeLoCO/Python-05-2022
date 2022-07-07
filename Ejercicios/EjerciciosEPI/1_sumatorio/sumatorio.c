#include <stdio.h>

int main () {
	int n;
	int numero_actual;
	int suma;

	suma = 0;
	printf("Introduzca el numero de numeros a introducir: ");
	scanf("%d", &n);

	for (int i = 0 ; i < n ; i++)
	{
		printf("Introduzca numero: ");
		scanf("%d", &numero_actual);
		suma+=numero_actual;
	}

	printf("El sumatorio es: %d", suma);
	
	return 0;
}

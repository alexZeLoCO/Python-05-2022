#include <stdio.h>

int main ()
{
	int nNumeros;
	int numero;
	int mayor;
	int menor;
	float media;

	mayor = 0;
	menor = 0;
	media = 0;

	printf("Introduzca el numero de numeros a introducir: ");
	scanf("%d", &nNumeros);

	for (int i = 0 ; i < nNumeros ; i++)
	{
		printf("Introduzca un numero: ");
		scanf("%d", &numero);
		if (numero > mayor || i == 0)
		{
			mayor = numero;
		}
		if (numero < menor || i == 0)
		{
			menor = numero;
		}
		media = media + numero;
	}

	media = media / nNumeros;

	printf("El mayor numero introducido ha sido el %d.\nEl menor numero introducido ha sido el %d.\nLa media de todos los numeros es %f.\n", mayor, menor, media);
	return 0;
}

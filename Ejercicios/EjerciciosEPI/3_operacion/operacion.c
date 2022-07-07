#include <stdio.h>
#include <math.h>

int main () {
	int limite;
	double suma;
	double media;

	suma = 0;
	media = 0;

	printf("Introduzca el limite del sumatorio: ");
	scanf("%d", &limite);

	for (int i = 0 ; i <= 100 ; i++)
	{
		media+=i;
	}
	media/=100;

	printf("Media: %f", media);

	for (int i = 1 ; i <= limite ; i++)
	{
		suma+=(pow(media, i+1)/sqrt(i));
	}

	printf("El sumatorio es: %f", suma);
	return 0;
}

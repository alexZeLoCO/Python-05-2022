#include <stdio.h>
#include <math.h>

int main () {
	int opcion;

	printf("Menu. Seleccione una.\n");
	printf("1. Circulo\n");
	printf("2. Cuadrado\n");
	printf("3. Rectangulo\n");

	printf("~> ");
	scanf("%d", &opcion);

	if (opcion == 1)
	{
		double radio;
		printf("Introduzca radio del circulo: ");
		scanf("%f", &radio);
		printf("Area del circulo de radio %f = %f", radio, pow(radio, 2)*3.141592654);
	}
	if (opcion == 2) 
	{
		double lado;
		printf("Introduzca el lado del cuadrado: ");
		scanf("%f", &lado);
		printf("Area del cuadrado de lado %f = %f", lado, pow(lado, 2));
	}
	if (opcion == 3)
	{
		double ladoA;
		double ladoB;
		printf("Introduzca el lado del rectangulo: ");
		scanf("%f", &ladoA);
		printf("Introduzca el lado del rectangulo: ");
		scanf("%f", &ladoB);
		printf("Area del rectangulo de lados %f y %f = %f", ladoA, ladoB, ladoA*ladoB);
	}
	return 0;
}
	


#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(void) {
	float y, y2;
	for (float i = 1; i <= 20; i += 1) {
		y = exp(i);
	}

	for (float i = 1; i <= 20; i += 0.1) {
		y2 = exp(i);
	}

	printf("%f %f", y, y2);
	return 0;
}

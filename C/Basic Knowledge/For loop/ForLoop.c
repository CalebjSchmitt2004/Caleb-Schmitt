#include <stdio.h>
#include <time.h>

int main() {
	int a;
	int number = 1000000;
	int half = number/2;

	printf("Starting Count To: %d", number);
	clock_t tic = clock();
	for (a = 10; a < number; a += 1) {
		if (a == half) {
			printf("\nHalf way there");
		}
	}
	printf("\nDone");
	clock_t toc = clock();
	printf("\nElapsed: %f seconds\n", (double)(toc - tic) / CLOCKS_PER_SEC);
	getchar();
}

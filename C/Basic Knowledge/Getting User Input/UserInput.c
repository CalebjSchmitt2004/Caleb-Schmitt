#include <stdio.h>

int main() {
	char userInput[100];

	printf("Please put in some text? ");
	gets(userInput);

	printf("You entered: ");
	puts(userInput);
	getchar();

	return 0;
}
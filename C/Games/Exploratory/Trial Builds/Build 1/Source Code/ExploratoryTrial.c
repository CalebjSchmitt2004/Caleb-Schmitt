#include <stdio.h>
#include <Windows.h>

char version[6] = "0.0.1";

void startScreen() {
	printf("\t\t\t\t\t------------------------------------------");
	printf("\n\t\t\t\t\t|         Welcome to Exploratory         |");
	printf("\n\t\t\t\t\t|                                        |");
	printf("\n\t\t\t\t\t|                                        |");
	printf("\n\t\t\t\t\t|Start Game                              |");
	printf("\n\t\t\t\t\t|                                        |");
	printf("\n\t\t\t\t\t|Credits                                 |");
	printf("\n\t\t\t\t\t|                                        |");
	printf("\n\t\t\t\t\t|Documentation                           |");
	printf("\n\t\t\t\t\t|                                        |");
	printf("\n\t\t\t\t\t|Exit                                    |");
	printf("\n\t\t\t\t\t|                                        |");
	printf("\n\t\t\t\t\t|                          Version: %s%s",version,"|");
	printf("\n\t\t\t\t\t------------------------------------------");

	char menuItem[10];
	printf("\n\nWhich menu option would you like to select: ");
	scanf("%s", menuItem);

	if (menuItem == "test") {
		printf("Hello!");
		Sleep(2000);
	}
	else {
		printf("Good bye!");
		Sleep(2000);
	}
}

int main() {
	startScreen();
	return 0;
}
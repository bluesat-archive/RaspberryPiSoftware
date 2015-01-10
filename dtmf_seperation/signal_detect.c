#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int main()
{
	char target[]="11111111";
	char testTarget[]="55555555";
        int position = 0;
        int positionTest = 0;

	int running = TRUE;
	while ( running )
	{
		char in = getchar();

		// Validate the input chars -- only process numbers and letters
		int islegal = FALSE;
		if ( in >= 'a' && in <= 'z' ) islegal = TRUE;
		if ( in >= 'A' && in <= 'Z' ) islegal = TRUE;
		if ( in >= '0' && in <= '9' ) islegal = TRUE;
		
		if ( islegal )
		{
			printf("%c", in);
			if ( in == target[position] )
			{
				printf(" ###");
				position++;
				if ( position == strlen(target))
				{
					// We have a match
					position = 0;
					printf("\n\033[32mMATCH MADE\033[0m\n");
					system("./setPin.py 13 0"); // Turn pin 13 to low
//					system("./setPin.py 26 1"); // Turn pin 26 to high, to indicate sep mech activation
				}
			}
                        else if ( in == testTarget[position]) {
                                printf(" ###");
                                positionTest++;
                                if ( positionTest == strlen(testTarget) )
				{
					// We have a match
					positionTest = 0;
					printf("\n\033[32mTEST SIGNAL CONFIRMED\033[0m\n");
					system("./setPin.py 26 1"); // Turn pin 26 to high, to indicate test signal confirm
				}
                        }
			else 
			{
				position = 0;
                                positionTest = 0;
			}
			printf("\n");
		}
	}

	return 0;
}


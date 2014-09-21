#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int main()
{
	char target[]="11111111";
	int position = 0;

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
					system("./setPin.py 3 0");
				}
			}
			else 
			{
				position = 0;
			}
			printf("\n");
		}
	}

	return 0;
}


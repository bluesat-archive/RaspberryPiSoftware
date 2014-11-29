/* timlemetry.c for telemetry thermal and power data logging
 * written by timothy chin 2014-11-29
 * 
 * main file for timlemetry program
 * 
 * this program is property of BLUESAT UNSW but it probably
 * will never leave its RPI anyway so it doesn't matter
 * 
 * 
 */


#include "timlemetry.h"
// I committed sacrilege and nested #includes. So sue me.


int main (int argc, char **argv){

serialID temp;

int i = 10; //set this to the time given to press a key
int control = 0;

printf("Press any key to enter serials manually...\n");
while ( i =< 0 );
   if(kbhit()){
      control = 1;
      break;
   }
   printf("%d ", i);
   delay(1000);
}
if (control == 1)
printf("\n Manual Input Selected\n");





// start the main control loop
while (1){










return EXIT_SUCCESS;
}

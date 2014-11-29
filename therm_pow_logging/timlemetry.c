/* timlemetry.c for telemetry thermal and power data logging
 * written by timothy chin 2014-11-29
 * 
 * main file for timlemetry program
 * 
 * this program is property of BLUESAT UNSW but it probably
 * will never leave its RPI anyway so it doesn't matter
 * 
 * The init file is called "serials"
 */


#include "timlemetry.h"
// I committed sacrilege and nested #includes. So sue me.
/*
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <conio.h> //these libraries don't exist on linux. Whoops.
//#include <dos.h>

#define DEBUG 1
// Used to turn off debug traces throughout code from one spot, instead of stripping them manually


typedef struct _serialID {
   char serial[20];
   char name[20];
} serialID;
// serialID type contains the unique serial number and the name of each device.
// The name gets printed prefixing the data in the log. Probably use therm1, etc.



time_t g_launchTime;    //hopefully self explanatory
FILE *g_logFile;        //this is the file to be written to
serialID g_sensors[10]; //this is the list of sensors, accessible everywhere

void serialInit();
//  populates the serialID list using file input

*/
int main (int argc, char **argv){

	serialInit();
	printf ("%s, %s",g_sensors[0].serial, g_sensors[0].name);
	

	// start the main control loop
	g_logFile = fopen("telem_Log","a");

	while (1){
	fprintf(g_logFile, "print success!");
	fflush(g_logFile);
	break;
	
	
	
	}

	fclose(g_logFile);


	return EXIT_SUCCESS;
}


void serialInit(){
	FILE *init = fopen("serials","r");
	serialID temp;
	char string[100];
	int i;
	int j = 0;
	char c = fgetc(init);
	while (){
		strcpy(temp.serial,strtok(fgets(string, 100, init)," \n"));
		strcpy(temp.name,strtok(0," \n"));
	}
}

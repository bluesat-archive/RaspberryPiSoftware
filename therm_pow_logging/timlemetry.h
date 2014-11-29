/* timlemetry.h for telemetry thermal and power data logging
 * written by timothy chin 2014-11-29
 * 
 * header file for timlemetry.c
 * 
 * global variables are prefixed with g_
 * 
 * 
 * 
 * 
 */

#ifndef TIMLEMETRY
#define TIMLEMETRY

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
//#include <conio.h> //these libraries don't exist on linux. Whoops.
//#include <dos.h>
#include <curses.h>

#define DEBUG 1
// Used to turn off debug traces throughout code from one spot, instead of stripping them manually


typedef struct serialID {
   char serial[20];
   char name[20];
}
// serialID type contains the unique serial number and the name of each device.
// The name gets printed prefixing the data in the log. Probably use therm1, etc.



time_t g_launchTime;    //hopefully self explanatory
FILE *g_logFile;        //this is the file to be written to
serialID g_sensors[10]; //this is the list of sensors, accessible everywhere

serialID serialInitCMD();
// Returns a initialised serialID using command line input

serialID serialInitFile(FILE *BootFile);
// Returns a initialised serialID using file input








#ENDIF

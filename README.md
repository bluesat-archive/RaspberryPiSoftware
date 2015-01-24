Ballon detachment code for bluesat.org
Version: Stuart_B 1.3
All hail our glorious leader

Features in this version
========================
Stuart_B 1.3 has updates to the installation script to fix the bug of the incorrect module being used.
The module used for clock interfacing previously was rtc_pcf2127a
The module to be used for clock interfacing now is rtc_pcf2127
The install script has been modified to reflect this. Please ensure the command
sudo modprobe rtc_pcf2127
does not cause errors when run.

Stuart_B 1.2 modifies the DTMF signals used. The detachment code is now "1111" and the yellow test LED now 
toggles whenever a 5 is recieved.

Stuart_B 1.1 includes modifications to the code to implement the yellow test LED that switches on 
when the test signal "55555555" is recieved.


Stuart_B 1.0 includes a script which automatically installs all the requisite libraries needed
to operate the Raspberry Pi in flight. The file can be found in
RaspberryPiSoftware/newInstallSetup/EXECUTE_ME
and further documentation can be found in what_do



Function and code overview
==========================

Important components for running:
* compile.sh -- compiles signal_detect.c . You need to do this -- a binary is not included in this git repo.
* manager -- Master script.  Starts, handles and manages everything else


Subcomponents:
* rtl-fm (not included) -- reads raw data from the RTL-sdr dongle
* multimon (not included) -- processes raw RF data -> finds DTMF codes
* multimon_processing -- strips prefixing "DTMF: " text from multimon output
* signal_detect -- looks for a pattern of DTMF tones and executes setPin.py when an expected pattern is found
* setPin.py -- toggles Raspberry Pi GPIO pins




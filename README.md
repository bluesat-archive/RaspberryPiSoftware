Ballon detachment code for bluesat.org
Version: Stuart_B 1.0
All hail our glorious leader

Features in this version
========================
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




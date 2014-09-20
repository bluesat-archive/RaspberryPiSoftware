Ballon detachment code for bluesat.org

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




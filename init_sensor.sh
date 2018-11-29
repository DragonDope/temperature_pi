#!/bin/bash

################################################################################################################
#
# Kleins Skrip um die angeschlossenen Sensoren am 1-Wire Port über einen USB-Seriell-Adapter zu intitialisieren
#
# Creator: DragonDope		Date: 2015-03-02
#
################################################################################################################


sudo digitemp_DS9097 -i -s /dev/ttyUSB0 -l ${PWD}/temperature.tmp -o "%b %d %H:%M:%S Sensor %s C: %.1C" -c digitemp.conf




#####################
#digitemp_DS9097 -h #
#####################

#Usage: digitemp [-s -i -I -U -l -r -v -t -a -d -n -o -c]
#                -i                            Initialize .digitemprc file
#                -I                            Initialize .digitemprc file w/sorted serial #s
#                -w                            Walk the full device tree
#                -s /dev/ttyS0                 Set serial port
#                -l /var/log/temperature       Send output to logfile
#                -c digitemp.conf              Configuration File
#                -r 1000                       Read delay in mS
#                -v                            Verbose output
#                -t 0                          Read Sensor #
#                -q                            No Copyright notice
#                -a                            Read all Sensors
#                -d 5                          Delay between samples (in sec.)
#                -n 50                         Number of times to repeat
#                                              0=loop forever
#                -A                            Treat DS2438 as A/D converter
#                -O"counter format string"      See description below
#                -o 2                          Output format for logfile
#                -o"output format string"      See description below
#                -H"Humidity format string"    See description below
#
#Logfile formats:  1 = One line per sensor, time, C, F (default)
#                  2 = One line per sample, elapsed time, temperature in C
#                  3 = Same as #2, except temperature is in F
#        #2 and #3 have the data separated by tabs, suitable for import
#        into a spreadsheet or other graphing software.
#
#        The format string uses strftime tokens plus 5 special ones for
#        digitemp - %s for sensor #, %C for centigrade, %F for fahrenheit,
#        %R to output the hex serial number, and %N for seconds since Epoch.
#        The case of the token is important! The default format string is:
#        "%b %d %H:%M:%S Sensor %s C: %.2C F: %.2F" which gives you an
#        output of: May 24 21:25:43 Sensor 0 C: 23.66 F: 74.59
#
#        The counter format string has 2 special specifiers:
#        %n is the counter # and %C is the count in decimal.
#        The humidity format uses %h for the humidity in percent


#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################################################
#	Modifier: DragonDope				Date: 2015-04-12			#
#	Creator: http://www.schnatterente.net/code/raspberrypi/displaytest.py			#
#												#
#	Diese Programm übergibt den gewünschten Text [display.output(Line1,Line2,Line3,Line4)]	#
#	einem 4x20 LCD-Display									#
#	Kann auch als Biliothek verwendet werden!						#
#												#
#################################################################################################

import time
import RPi.GPIO as GPIO

# Einstellungen 
################

# Zuordnung der GPIO Pins (aktuell: BOARD)
display_RS = 21				# Pin für RS (Befehlsregister/Datenregister)
display_E  = 24				# Pin für Enable (Takt)
display_D4 = 23				# Pin für Datenleitung 4
display_D5 = 26 			# Pin für Datenleitung 5
display_D6 = 29	 			# Pin für Datenleitung 6
display_D7 = 31	 			# Pin für Datenleitung 7

# Display Eigenschaften
display_breite = 20 			# Zeichen je Zeile
display_line_1 = 0x80 			# Adresse der ersten Display Zeile
display_line_2 = 0xC0 			# Adresse der zweiten Display Zeile
display_line_3 = 0x94			# Adresse der dritten Display Zeile
display_line_4 = 0xD4			# Adresse der vierten Display Zeile
display_data = True			# Befehlsregister
display_cmd = False			# Datenregister
E_pulse = 0.0004			# Takt
E_delay = 0.0004			# Takt


def output(line1, line2, line3, line4):
	set_GPIO()				# Aufruf des Unterprogramms zum deklarieren der GPIOs	
	display_init()				# Aufruf des Unterprogramm zur Displayinitialiserung

	lcd_byte(display_line_1, display_cmd)
	lcd_string(line1)
	lcd_byte(display_line_2, display_cmd)
	lcd_string(line2)
	lcd_byte(display_line_3, display_cmd)
	lcd_string(line3)
	lcd_byte(display_line_4, display_cmd)
	lcd_string(line4)
	
	time.sleep(1)
	reset_GPIO()

def set_GPIO():
        GPIO.setmode(GPIO.BOARD)                        # GPIO Mode einstellen (BCM, BOARD)
        GPIO.setup(display_E, GPIO.OUT)                 # GPIO Pin als Ausgang
        GPIO.setup(display_RS, GPIO.OUT)                # GPIO Pin als Ausgang
        GPIO.setup(display_D4, GPIO.OUT)                # GPIO Pin als Ausgang
        GPIO.setup(display_D5, GPIO.OUT)                # GPIO Pin als Ausgang
        GPIO.setup(display_D6, GPIO.OUT)                # GPIO Pin als Ausgang
        GPIO.setup(display_D7, GPIO.OUT)                # GPIO Pin als Ausgang

def reset_GPIO():
        GPIO.cleanup()

def display_init():
	lcd_byte(0x33,display_cmd)
	lcd_byte(0x32,display_cmd)
	lcd_byte(0x28,display_cmd)
	lcd_byte(0x0C,display_cmd)  
	lcd_byte(0x06,display_cmd)
	lcd_byte(0x01,display_cmd)  

def lcd_string(message):
	message = message.ljust(display_breite," ")  
	for i in range(display_breite):
	  lcd_byte(ord(message[i]),display_data)

def lcd_byte(bits, mode):
	GPIO.output(display_RS, mode)
	GPIO.output(display_D4, False)
	GPIO.output(display_D5, False)
	GPIO.output(display_D6, False)
	GPIO.output(display_D7, False)

	if bits&0x10==0x10:
	  GPIO.output(display_D4, True)
	if bits&0x20==0x20:
	  GPIO.output(display_D5, True)
	if bits&0x40==0x40:
	  GPIO.output(display_D6, True)
	if bits&0x80==0x80:
	  GPIO.output(display_D7, True)

	time.sleep(E_delay)    
	GPIO.output(display_E, True)  
	time.sleep(E_pulse)
	GPIO.output(display_E, False)  
	time.sleep(E_delay)      

	GPIO.output(display_D4, False)
	GPIO.output(display_D5, False)
	GPIO.output(display_D6, False)
	GPIO.output(display_D7, False)

	if bits&0x01==0x01:
	  GPIO.output(display_D4, True)
	if bits&0x02==0x02:
	  GPIO.output(display_D5, True)
	if bits&0x04==0x04:
	  GPIO.output(display_D6, True)
	if bits&0x08==0x08:
	  GPIO.output(display_D7, True)

	time.sleep(E_delay)    
	GPIO.output(display_E, True)  
	time.sleep(E_pulse)
	GPIO.output(display_E, False)  
	time.sleep(E_delay)   


#Codeblock bei direktem aufrufen der Datei
###########################################
if __name__ == '__main__':
	output("Linie 1", "Linie 2", "Linie 3", "Linie 4")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################################################################
#       Creator: DragonDope                            Date: 2015-04-12	                        #
#                                                                                               #
#       Diese Programm zeigt die letzten Werte (Temperaturen) einer rrd-Datenbank auf einem	#
#       4x20 LCD-Display an.	                                                                #
#       Die erste Zeile zeigt Datum und Uhrzeit an	                                        #
#       Die restlichen Zeilen zeigen die Werte (max. 6 St.)  an (Zwei Blätter im Wechsel)       #
#################################################################################################

import display
import time
import rrdtool
import os.path

deg = u'\xdf'			# Sonderzeichen °
ue = u'\xf5'			# Sonderzeichen ü

#Zeilentext bitte im Unterprogramm "write_displ" verändern

#Deklarierung der Displayzeilen
zeile1 = 0x80
zeile2 = 0xC0
zeile3 = 0x94
zeile4 = 0xD4

name_rrd_database = "temperature.rrd"				# Name der rrd-Datenbank
path = os.path.dirname(os.path.abspath(__file__))              	# Pfad der aktuellen Datei
splitpath = os.path.split(path)					# Pfad splitten (ein Ordner höher)
db_rrd_path = splitpath[0] + "/" + name_rrd_database		# kompletter Pfad zur rrd-Datenbank

#--------------------------------------------------------------------------

def main():				# Hauptprogramm
	try:
		print (time.strftime("%Y-%m-%d %H:%M ") + "Start Display Temperatur")	# Textausgabe bei Programmstart

		while True:
			init()                  			# Unterprog. Initialisierug
			for a in range(5):			
				zeit_schreiben()			# Unterprog. Zeit schreiben
				temperature = get_temp()		# Untergrog. Temperaturwerte einlesen
				for i in range(6):
					write_displ(temperature)	# Unterprog. für Werte auf Display schreiben
			display.reset_GPIO()				# GPIOs zurücksetzen


	except KeyboardInterrupt:							# Ausnahme, wenn Abbruch durch Strg + C
        	display.reset_GPIO()								# GPIOs zurücksetzen
       		print ("\n" + time.strftime("%Y-%m-%d %H:%M ") + "Abbruch durch den Benutzer")	# Textausgabe

	except:										# Ausnahme, wenn Fehler im Programm
		display.reset_GPIO()							# GPIOs zurücksetzen
		print ("\n"  + time.strftime("%Y-%m-%d %H:%M ") + "Programmfehler")	# Textausgabe


def init():
	display.set_GPIO()  		     	# deklarieren der GPIOs
	display.display_init()			# Displayinitialiserung

        
def get_temp():
	db_rrd = rrdtool.info(db_rrd_path)
	temperature = [db_rrd["ds[Sensor0].last_ds"],db_rrd["ds[Sensor1].last_ds"],db_rrd["ds[Sensor2].last_ds"],db_rrd["ds[Sensor3].last_ds"],db_rrd["ds[Sensor4].last_ds"],db_rrd["ds[Sensor5].last_ds"]]
	return(temperature)

def zeit_schreiben():
	zeit=time.strftime("  %d.%m.%Y %H:%M  ")	# Aktuelle Zeit in Variable speichern
	display.lcd_byte(zeile1, False)			# Displaycursor setzen/verschieben
	display.lcd_string(zeit)			# Aktuelle Zeit aufs Display schreiben


def write_displ(temp):
	#Erste Seite
	display.lcd_byte(zeile2, False)					# Displaycursor setzen/verschieben
	display.lcd_string("Wohnzimmer "+ temp[4] + deg + "C")	# Text aufs Display schreiben

	display.lcd_byte(zeile3, False)					# Displaycursor setzen/verschieben
	display.lcd_string("Kellerraum "+ temp[0] + deg + "C")	# Text aufs Display schreiben

	display.lcd_byte(zeile4, False)					# Displaycursor setzen/verschieben
	display.lcd_string("Dachboden "+ temp[1] + deg + "C")	# Text aufs Display schreiben

	time.sleep(4.84)						# Wartezeit
	
	#Zweite Seite
	display.lcd_byte(zeile2, False)						# Displaycursor setzen/verschieben
	display.lcd_string("Eingangst" + ue +"r "+ temp[3] + deg + "C")	# Text aufs Display schreiben

	display.lcd_byte(zeile3, False)						# Displaycursor setzen/verschieben
	display.lcd_string("R" + ue + "ckseite "+ temp[2] + deg + "C")	# Text aufs Display schreiben

	display.lcd_byte(zeile4, False)						# Displaycursor setzen/verschieben
	display.lcd_string(" ")							# Text aufs Display schreiben

	time.sleep(4.84)							# Wartezeit


#Codeblock bei direktem aufrufen der Datei
###########################################
if __name__ == '__main__':
        main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

def temperature(delete_temp, save_log, save_rrd, output):
        """	Creator: DragonDope		Date: 2016-08-31

	Dies ist ein Programm/Modul welches Temperaturwerte mit dem Tool "digitemp_DS9097" einlist.
        Anschließend werden die Werte in eine *.log Datei und in einer rrd-Datenbank gespeichert.

	Ablauf:
                -> Einlesen (digitemp)
                -> speichert Werte in *.tmp Datei
                -> einlesen aus *.tmp Datei
                -> speichern in *.log Datei
                -> Werte für rrd-Datenbank formatieren
                -> in rrd-Datenbank speichern

        Auswahl über die Eingangsvariablen:
		-> löschen der *.tmp Datei (True/False)
		-> Temperaturwerte in *.log Datei speichern (True/False)
		-> Temperaturwerte in *.rrd Datenbank speichern (True/False)
                -> Temperaturwert über Konsole ausgeben (True/False)
	"""

	import os
	import rrdtool

	#Einstellungen
	###############
	name_tmp_file = "temperature.tmp"			# Dateiname für die Tempdatei
	name_log_file = "temperature.log"			# Dateiname für die Logdatei
	name_rrd_database = "temperature.rrd"			# Dateiname für die rrd-Datenbank
	name_digitemp_config = "digitemp.conf"			# Dateiname für dei Configdatei für DigiTemp

	sensor = ("Kellerraum", "Dachboden", "Rückseite", "Eingangstür", "Wohnzimmer")        	# Namen für Sensoren (Anzahl der Namen entspricht Anzahl der Sensoren) (Sensor0, Sensor2, ...)
	
	sensor_anzahl = len(sensor)							#Anzahl der Sensoren;

        #Pfad und Dateinamen Zusammenstellung
        #####################################
        path = os.path.dirname(os.path.abspath(__file__))       	# Pfad der aktuellen Datei
        path_tmp_file = "%s/%s" %(path, name_tmp_file)          	# Pfad und Dateiname für die Tempdatei
        path_log_file = "%s/%s" %(path, name_log_file)        		# Pfad und Dateiname für die Logdatei
        path_rrd_database = "%s/%s" %(path, name_rrd_database)  	# Pfad und Dateiname für die rrd-Datenbank
	path_digitemp_config = "%s/%s" %(path, name_digitemp_config)	# Pfad und Dateiname für die Configdatei für DigiTemp

	#Temperatur mit digitemp einlesen
	#################################
	bashCommand = "sudo /usr/bin/digitemp_DS9097 -a -c %s -q" %(path_digitemp_config)	# Shell-Befehl in Variable speichern $
        os.system(bashCommand)                                  				# Shell-Befehl ausführen
	
	#Werte lesen und schreiben
	###########################
	file_temp = open(path_tmp_file, "r")			# Tempdatei öffnen
	list = file_temp.readlines()                            # alle Zeilen in eine Liste speichern
	file_temp.close()					# Tempdatei schließen
	if delete_temp: os.remove(path_tmp_file) 		# Tempdatei löschen
	
	if len(list) != sensor_anzahl:				# Vergleich: Anzahl der Zeilen in der Temp-Datei mit der Anzahl vergebener Sensornamen
		print "Warnung!: Anzahl der vergebenen Sensornamen überprüfen\n******************************************************"
	
	if save_log:
		file = open(path_log_file, "a")			# Logdatei öffnen
		file.writelines(list)				# Tempdateiinhalt zur Logdatei hinzufügen
		file.close()					# Logdatei schließen
	
	#Auslesen der Temperaturen aus der Liste
	######################################
	temperatur = {}									# Set erstellen
	for i in range(sensor_anzahl-1,-1,-1):						# Temperaturen auslesen
		line = list[len(list)-i-1]						# Zeile des entsprechenden Sensors lesen
		n = line.rfind(":")							# Stelle des ausgewählten Zeichens finden
		temperatur[sensor_anzahl-i-1] = line[n+2:-1]				# Temperatur in Set speichern
		temperatur[sensor_anzahl-i-1] = float(temperatur[sensor_anzahl-i-1])	# Sting in in float konvertieren
	
	if output:									# Temperaturausgabe auf Konsole?
		for i in range(0, sensor_anzahl):					# Temperaturen von allen Sensoren ausgeben
			print "%s %.1f °C" %(sensor[i], temperatur[i])			# Temperaturausgabe
	
	if save_rrd:
		if sensor_anzahl == 1:
			rrdtool.update(path_rrd_database,"N:%.1f:NaN:NaN:NaN:NaN:NaN" %(temperatur[0]))
		if sensor_anzahl == 2:
			rrdtool.update(path_rrd_database,"N:%.1f:%.1f:NaN:NaN:NaN:NaN" %(temperatur[0],temperatur[1]))
		if sensor_anzahl == 3:
			rrdtool.update(path_rrd_database,"N:%.1f:%.1f:%.1f:NaN:NaN:NaN" %(temperatur[0],temperatur[1],temperatur[2]))
		if sensor_anzahl == 4:
			rrdtool.update(path_rrd_database,"N:%.1f:%.1f:%.1f:%.1f:NaN:NaN" %(temperatur[0],temperatur[1],temperatur[2],temperatur[3]))
		if sensor_anzahl == 5:
			rrdtool.update(path_rrd_database,"N:%.1f:%.1f:%.1f:%.1f:%.1f:NaN" %(temperatur[0],temperatur[1],temperatur[2],temperatur[3],temperatur[4]))
		if sensor_anzahl == 6:		
			rrdtool.update(path_rrd_database,"N:%.1f:%.1f:%.1f:%.1f:%.1f:%.1f" %(temperatur[0],temperatur[1],temperatur[2],temperatur[3],temperatur[4],temperatur[5]))


#Codeblock bei direktem aufrufen der Datei
###########################################
if __name__ == "__main__":
	temperature(True, False, True, False)

	# Beschreibung: temperature(delete_temp, save_log, save_rrd, output)
		# delete_temp	= Soll die Temp-Datei gelöscht werden? (True/False)
		# save_log	= Soll die Temperaturwerte in *.log Datei gespeichert werden? (True/False)
		# save_rrd	= Sollen die Werte in die *.rrd Datenbank gespeichert werden? (True/False)
		# output	= Soll ein Ausgabe der Temperatur in die Konsole oder crontab logs erfolgen? (True/False)

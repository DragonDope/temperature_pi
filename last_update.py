#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lastvalue():
	"""	Creator: DragonDope		Date: 2015-04-09
	Dieses Programm gibt die letzten Werte einer rrd-Datenbank aus
	"""

	import rrdtool
	import os.path

	#Dateiname der rrd-Datenbank
	rrd_name = "temperature.rrd"

	path = os.path.dirname(os.path.abspath(__file__))
	info = rrdtool.info("%s/%s" %(path, rrd_name))
	print 	("Uhrzeit",info["last_update"],"\n",info["ds[Sensor0].last_ds"],"°C\n",info["ds[Sensor1].last_ds"],"°C\n",info["ds[Sensor2].last_ds"],"°C\n",info["ds[Sensor3].last_ds"],"°C\n",info["ds[Sensor4].last_ds"],"°C\n",info["ds[Sensor5].last_ds"],"°C")


#Codeblock bei direktem aufrufen der Datei
###########################################
if __name__ == "__main__":
        lastvalue()


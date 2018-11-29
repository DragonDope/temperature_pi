#!/usr/bin/env python
# -*- coding: utf-8 -*-

def ssh_lastvalue():
	"""	Creator: DragonDope		Date: 2015-12-06
	Dieses Programm gibt die letzten Werte einer rrd-Datenbank aus
	Die Ausgabe ist für den externen Zugriff per ssh optimiert.
	"""

	import rrdtool
	import os.path
	import time

	#Dateiname der rrd-Datenbank
	rrd_name = "temperature.rrd"

	path = os.path.dirname(os.path.abspath(__file__))
	info = rrdtool.info("%s/%s" %(path, rrd_name))
	raw_time = time.localtime(info["last_update"])
	datum = time.strftime("%d-%m-%Y", raw_time)
	zeit = time.strftime("%H:%M",raw_time)

	print 	(datum,"\n",zeit,"\n",info["ds[Sensor0].last_ds"],"\n",info["ds[Sensor1].last_ds"],"\n",info["ds[Sensor2].last_ds"],"\n",info["ds[Sensor3].last_ds"],"\n",info["ds[Sensor4].last_ds"],"\n",info["ds[Sensor5].last_ds"])


#Codeblock bei direktem aufrufen der Datei
###########################################
if __name__ == "__main__":
        ssh_lastvalue()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################################
#
# Dieses kleine Progemm erstellt eine Round Robin Datenbank mittels RRD-Tool
#	Genauere Informationen zu Befehl sind auf der Website des rrdtools zu entnehmen
# 
# -> Für das Projekt "Temperature" muss die Datenbank nur einmal erstellt werden
#
# Creater: DragonDope		Date: 2015-03-12
#
########################################################################################

import rrdtool

rrdtool.create(	"temperature.rrd",
		"--step", "900",
		"DS:Sensor0:GAUGE:1200:-40:80",
		"DS:Sensor1:GAUGE:1200:-40:80",
		"DS:Sensor2:GAUGE:1200:-40:80",
		"DS:Sensor3:GAUGE:1200:-40:80",
		"DS:Sensor4:GAUGE:1200:-40:80",
		"DS:Sensor5:GAUGE:1200:-40:80",
		"RRA:AVERAGE:0.5:1:960",
		"RRA:MIN:0.5:96:18000",
		"RRA:MAX:0.5:96:18000",
		"RRA:AVERAGE:0.5:96:18000"	)


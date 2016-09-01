#!/usr/bin/env python
# -*- coding: utf-8 -*-
def create_graph():
	""" Creator: DragonDope					Date: 2015-09-04
	
	Das Programm/Modul erstellt Diagramme aus den Daten einer rrd-Datenbank.
	
	Folgende Diagramme werden erstellt:
		- Anzeige der letzten Werte aus der rr-Datenbank (alle Werte)
		- letzte 24 Std. (alle Werte)
		- letzte Woche (alle Werte)
		- letzten Monat (je Temperatur ein Diagramm)
		- letztes Jahr (je Temperatur ein Diagramm)
	
	Die Diagramme werden in den Ordner des Webservers gespeichert
	"""
	import rrdtool
	import time
	import os.path

	#Einstellung
	#-----------

	name_temp0 = "Kellerraum" 
	name_temp1 = "Dachboden"
	name_temp2 = "Rückseite"
	name_temp3 = "Eingangstür"
	name_temp4 = "Wohnzimmer"
	
	database = "temperature.rrd"						# Name der rrd-Datenbank
	path = os.path.dirname(os.path.abspath(__file__)) + "/"              	# Pfad der aktuellen Datei
	
	path_plot = "/var/www/plots/"
	
	plot_day = "tag.png"
	plot_week = "woche.png"
	plot_month_temp0 = "monat_temp0.png"
	plot_month_temp1 = "monat_temp1.png"
	plot_month_temp2 = "monat_temp2.png"
	plot_month_temp3 = "monat_temp3.png"
	plot_month_temp4 = "monat_temp4.png"
	plot_year_temp0 = "jahr_temp0.png"
	plot_year_temp1 = "jahr_temp1.png"
	plot_year_temp2 = "jahr_temp2.png"
	plot_year_temp3 = "jahr_temp3.png"
	plot_year_temp4 = "jahr_temp4.png"
	values = "werte.png"

	date = time.strftime("%d-%m-%Y")
	#---------------------------------------------------------

	# Werte
	#-------
	rrdtool.graph("%s%s" %(path_plot, values),
		"--imgformat", "PNG",
		"--width", "854",
		"--height", "10",
		"--start", "now - 1 day",
		"--end", "now",
		"--x-grid", "none",
		"--y-grid", "none",
		"--color", "BACK#FFFFFF00",
		"--color", "CANVAS#FFFFFF00",
		"--color", "AXIS#FFFFFF00",
		"--color", "ARROW#FFFFFF00",
		"--border", "0",
		"--font", "DEFAULT:0:Sans-serif",
		"--legend-position", "north",
		"DEF:temp0=%s%s:Sensor0:AVERAGE" %(path, database),
		"LINE0:temp0#000000:%s" %(name_temp0),
		"VDEF:temp0last=temp0,LAST",
		"GPRINT:temp0last:%.1lf °C\t",
		"DEF:temp1=%s%s:Sensor1:AVERAGE" %(path, database),
		"LINE0:temp1#0000FF:%s" %(name_temp1),
		"VDEF:temp1last=temp1,LAST",
		"GPRINT:temp1last:%.1lf °C\t",
		"DEF:temp2=%s%s:Sensor2:AVERAGE" %(path, database),
		"LINE0:temp2#00FF00:%s" %(name_temp2),
		"VDEF:temp2last=temp2,LAST",
		"GPRINT:temp2last:%.1lf °C\t",
		"DEF:temp3=%s%s:Sensor3:AVERAGE" %(path, database),
		"LINE0:temp3#FF0000:%s" %(name_temp3),
		"VDEF:temp3last=temp3,LAST",
		"GPRINT:temp3last:%.1lf °C\t",
		"DEF:temp4=%s%s:Sensor4:AVERAGE" %(path, database),
		"LINE0:temp4#FF9900:%s" %(name_temp4),
		"VDEF:temp4last=temp4,LAST",
		"GPRINT:temp4last:%.1lf °C"	)

			
	# Tagesdiagramm
	#--------------
	rrdtool.graph("%s%s" %(path_plot, plot_day),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "300",
		"--start", "now - 1 day",
		"--end", "now",
		"--x-grid", "MINUTE:15:HOUR:1:HOUR:2:0:%H:%M",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Tag) LeMenilFleury",
		"--tabwidth", "40",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp0=%s%s:Sensor0:AVERAGE" %(path, database),
		"LINE1:temp0#000000:%s\t" %(name_temp0),
		"VDEF:temp0last=temp0,LAST",
		"GPRINT:temp0last:%.1lf °C\l", 
		"DEF:temp1=%s%s:Sensor1:AVERAGE" %(path, database),
		"LINE1:temp1#0000FF:%s\t" %(name_temp1),
		"VDEF:temp1last=temp1,LAST",
		"GPRINT:temp1last:%.1lf °C\l",
		"DEF:temp2=%s%s:Sensor2:AVERAGE" %(path, database),
		"LINE1:temp2#00FF00:%s\t" %(name_temp2),
		"VDEF:temp2last=temp2,LAST",
		"GPRINT:temp2last:%.1lf °C\l",
		"DEF:temp3=%s%s:Sensor3:AVERAGE" %(path, database),
		"LINE1:temp3#FF0000:%s\t" %(name_temp3),
		"VDEF:temp3last=temp3,LAST",
		"GPRINT:temp3last:%.1lf °C\l",
		"DEF:temp4=%s%s:Sensor4:AVERAGE" %(path, database),
		"LINE1:temp4#FF9900:%s\t" %(name_temp4),
		"VDEF:temp4last=temp4,LAST",
		"GPRINT:temp4last:%.1lf °C\l" 	)


	#Wochendiagramm
	#---------------
	rrdtool.graph("%s%s" %(path_plot, plot_week),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "300",
		"--start", "now - 1 week",	
		"--end", "now",
		"--x-grid", "HOUR:6:DAY:1:DAY:1:86400:%a %d.%m.%y",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Woche) LeMenilFleury",
		"--tabwidth", "43",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp0=%s%s:Sensor0:AVERAGE" %(path, database),
		"LINE1:temp0#000000:%s\t" %(name_temp0),
		"DEF:temp1=%s%s:Sensor1:AVERAGE" %(path, database),
		"LINE1:temp1#0000FF:%s\t" %(name_temp1),
		"DEF:temp2=%s%s:Sensor2:AVERAGE" %(path, database),
		"LINE1:temp2#00FF00:%s\t" %(name_temp2),
		"DEF:temp3=%s%s:Sensor3:AVERAGE" %(path, database),
		"LINE1:temp3#FF0000:%s\t" %(name_temp3),
		"DEF:temp4=%s%s:Sensor4:AVERAGE" %(path, database),
		"LINE1:temp4#FF9900:%s\t" %(name_temp4)   )

		
	# Monatsdiagramm
	#---------------

	#Monatsdiagramm (temp0)
	rrdtool.graph("%s%s" %(path_plot, plot_month_temp0),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 month",
		"--end", "now",
		"--x-grid", "DAY:1:WEEK:1:DAY:1:86400:%d",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Monat) %s" %(name_temp0),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp0min=%s%s:Sensor0:MIN" %(path, database),
		"DEF:temp0=%s%s:Sensor0:AVERAGE" %(path, database),
		"DEF:temp0max=%s%s:Sensor0:MAX" %(path, database),
		"CDEF:temp0area=temp0max,temp0min,-",
		"LINE1:temp0min#000000",
		"AREA:temp0area#00000050::STACK",
		"LINE2:temp0#000000:%s (Ø)\t" %(name_temp0),
		"LINE1:temp0max#000000" )

	#Monatsdiagramm (temp1)
	rrdtool.graph("%s%s" %(path_plot, plot_month_temp1),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 month",
		"--end", "now",
		"--x-grid", "DAY:1:WEEK:1:DAY:1:86400:%d",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Monat) %s" %(name_temp1),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp1min=%s%s:Sensor1:MIN" %(path, database),
		"DEF:temp1=%s%s:Sensor1:AVERAGE" %(path, database),
		"DEF:temp1max=%s%s:Sensor1:MAX" %(path, database),
		"CDEF:temp1area=temp1max,temp1min,-",
		"LINE1:temp1min#0000FF",
		"AREA:temp1area#0000FF50::STACK",
		"LINE2:temp1#0000FF:%s (Ø)\t" %(name_temp1),
		"LINE1:temp1max#0000FF" )

	#Monatsdiagramm (temp2)
	rrdtool.graph("%s%s" %(path_plot, plot_month_temp2),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 month",
		"--end", "now",
		"--x-grid", "DAY:1:WEEK:1:DAY:1:86400:%d",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Monat) %s" %(name_temp2),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp2min=%s%s:Sensor2:MIN" %(path, database),
		"DEF:temp2=%s%s:Sensor2:AVERAGE" %(path, database),
		"DEF:temp2max=%s%s:Sensor2:MAX" %(path, database),
		"CDEF:temp2area=temp2max,temp2min,-",
		"LINE1:temp2min#00FF00",
		"AREA:temp2area#00FF0050::STACK",
		"LINE2:temp2#00FF00:%s (Ø)\t" %(name_temp2),
		"LINE1:temp2max#00FF00"	)

	#Monatsdiagramm (temp3)
	rrdtool.graph("%s%s" %(path_plot, plot_month_temp3),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 month",
		"--end", "now",
		"--x-grid", "DAY:1:WEEK:1:DAY:1:86400:%d",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Monat) %s" %(name_temp3),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp3min=%s%s:Sensor3:MIN" %(path, database),
		"DEF:temp3=%s%s:Sensor3:AVERAGE" %(path, database),
		"DEF:temp3max=%s%s:Sensor3:MAX" %(path, database),
		"CDEF:temp3area=temp3max,temp3min,-",
		"LINE1:temp3min#FF0000",
		"AREA:temp3area#FF000050::STACK",
		"LINE2:temp3#FF0000:%s (Ø)\t" %(name_temp3),
		"LINE1:temp3max#FF0000"	)

	#Monatsdiagramm (temp4)
	rrdtool.graph("%s%s" %(path_plot, plot_month_temp4),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 month",
		"--end", "now",
		"--x-grid", "DAY:1:WEEK:1:DAY:1:86400:%d",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Monat) %s" %(name_temp4),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp4min=%s%s:Sensor4:MIN" %(path, database),
		"DEF:temp4=%s%s:Sensor4:AVERAGE" %(path, database),
		"DEF:temp4max=%s%s:Sensor4:MAX" %(path, database),
		"CDEF:temp4area=temp4max,temp4min,-",
		"LINE1:temp4min#FF9900",
		"AREA:temp4area#FF990050::STACK",
		"LINE2:temp4#FF9900:%s (Ø)\t" %(name_temp4),
		"LINE1:temp4max#FF9900" )

	
	# Jahresdiagramm
	#---------------
	
	#Jahresdiagramm (temp0)
	rrdtool.graph("%s%s" %(path_plot, plot_year_temp0),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 year",
		"--end", "now",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Jahr) %s" %(name_temp0),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp0min=%s%s:Sensor0:MIN" %(path, database),
		"DEF:temp0=%s%s:Sensor0:AVERAGE" %(path, database),
		"DEF:temp0max=%s%s:Sensor0:MAX" %(path, database),
		"CDEF:temp0area=temp0max,temp0min,-",
		"LINE1:temp0min#000000",
		"AREA:temp0area#00000050::STACK",
		"LINE2:temp0#000000:%s (Ø)\t" %(name_temp0),
		"LINE1:temp0max#000000" )

	#Jahresdiagramm (temp1)
	rrdtool.graph("%s%s" %(path_plot, plot_year_temp1),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 year",
		"--end", "now",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Jahr) %s" %(name_temp1),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp1min=%s%s:Sensor1:MIN" %(path, database),
		"DEF:temp1=%s%s:Sensor1:AVERAGE" %(path, database),
		"DEF:temp1max=%s%s:Sensor1:MAX" %(path, database),
		"CDEF:temp1area=temp1max,temp1min,-",
		"LINE1:temp1min#0000FF",
		"AREA:temp1area#0000FF50::STACK",
		"LINE2:temp1#0000FF:%s (Ø)\t" %(name_temp1),
		"LINE1:temp1max#0000FF" )

	#Jahresdiagramm (temp2)
	rrdtool.graph("%s%s" %(path_plot, plot_year_temp2),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 year",
		"--end", "now",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Jahr) %s" %(name_temp2),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp2min=%s%s:Sensor2:MIN" %(path, database),
		"DEF:temp2=%s%s:Sensor2:AVERAGE" %(path, database),
		"DEF:temp2max=%s%s:Sensor2:MAX" %(path, database),
		"CDEF:temp2area=temp2max,temp2min,-",
		"LINE1:temp2min#00FF00",
		"AREA:temp2area#00FF0050::STACK",
		"LINE2:temp2#00FF00:%s (Ø)\t" %(name_temp2),
		"LINE1:temp2max#00FF00" )

	#Jahresdiagramm (temp3)
	rrdtool.graph("%s%s" %(path_plot, plot_year_temp3),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 year",
		"--end", "now",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Jahr) %s" %(name_temp3),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp3min=%s%s:Sensor3:MIN" %(path, database),
		"DEF:temp3=%s%s:Sensor3:AVERAGE" %(path, database),
		"DEF:temp3max=%s%s:Sensor3:MAX" %(path, database),
		"CDEF:temp3area=temp3max,temp3min,-",
		"LINE1:temp3min#FF0000",
		"AREA:temp3area#FF000050::STACK",
		"LINE2:temp3#FF0000:%s (Ø)\t" %(name_temp3),
		"LINE1:temp3max#FF0000" )

	#Jahresdiagramm (temp4)
	rrdtool.graph("%s%s" %(path_plot, plot_year_temp4),
		"--imgformat", "PNG",
		"--width", "750",
		"--height", "100",
		"--start", "now - 1 year",
		"--end", "now",
		"--vertical-label", "Temperatur [°C]",
		"--right-axis", "1:0",
		"--right-axis-label", "Temperatur [°C]",
		"--title", "Temperatur (Jahr) %s" %(name_temp4),
		"--tabwidth", "44",
		"--watermark", "©%s LeMenilFleury@online.de" %(date),
		"--font", "DEFAULT:0:Sans-serif",
		"DEF:temp4min=%s%s:Sensor4:MIN" %(path, database),
		"DEF:temp4=%s%s:Sensor4:AVERAGE" %(path, database),
		"DEF:temp4max=%s%s:Sensor4:MAX" %(path, database),
		"CDEF:temp4area=temp4max,temp4min,-",
		"LINE1:temp4min#FF9900",
		"AREA:temp4area#FF990050::STACK",
		"LINE2:temp4#FF9900:%s (Ø)\t" %(name_temp4),
		"LINE1:temp4max#FF9900" )


#Codeblock bei direktem aufrufen der Datei
###########################################
if __name__ == "__main__":
        create_graph()

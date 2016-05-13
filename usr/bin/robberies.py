#!/usr/bin/env python

import sys
import os

atm_robbery = """

this addAction["ATM ausrauben",life_fnc_robShops];

""".replace('"', '""').replace("\r", " ").replace("\n", " ").replace("\t", " ")

station_robbery = """

this addAction["Tankstelle ausrauben",life_fnc_robShops];

""".replace('"', '""').replace("\r", " ").replace("\n", " ").replace("\t", " ")

#
# main function
#
if __name__ == "__main__":
	with open(sys.argv[1], "r") as file_reader:
		for line in file_reader:
			line = line.replace("@@@CLASSVEHICLES_ROB_ATM@@@;", atm_robbery)
			line = line.replace("@@@CLASSVEHICLES_ROB_STATION@@@;", station_robbery)

			print line.replace("\r", "").replace("\n", "")
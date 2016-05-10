#!/usr/bin/env python

import sys
import os

shops = ["Land_Laptop_unfolded_F"]

shop_locations = [
	"5446.32959,2.57737,15020.101563",
	"5406.741211,0.882408,15046.0458984"
]

output_buffer = []

shop_actions = """

this addAction[
	"Heli Garage",
	{
		if(life_HC_isActive) then {
			[getPlayerUID player,playerSide,"Air",player] remoteExecCall ["HC_fnc_getVehicles",HC_Life];
		} else {
			[getPlayerUID player,playerSide,"Air",player] remoteExecCall ["TON_fnc_getVehicles",2];
		};

		life_garage_type = "Air";
		createDialog "Life_impound_menu";
		disableSerialization;
		ctrlSetText[2802,"Fetching Vehicles...."];
		life_garage_sp = "stadion_heli_spawn_1";
	}
];

this addAction[
	localize"STR_Garage_Title",
	{
		if(life_HC_isActive) then {
			[getPlayerUID player,playerSide,"Car",player] remoteExecCall ["HC_fnc_getVehicles",HC_Life];
		} else {
			[getPlayerUID player,playerSide,"Car",player] remoteExecCall ["TON_fnc_getVehicles",2];
		};
		
		life_garage_type = "Car";
		createDialog "Life_impound_menu";
		disableSerialization;
		ctrlSetText[2802,"Fetching Vehicles...."];
		life_garage_sp = "stadion_heli_spawn_2";
	}
];

this addAction[
	localize "STR_MAR_Car_shop",
	life_fnc_vehicleShopMenu,
	["civ_car",civilian,"stadion_heli_spawn_2","civ","Bruce's New & Used Auto's"]
];

this addAction[
	localize"STR_MAR_Truck_Shop",
	life_fnc_vehicleShopMenu,
	["civ_truck",civilian,"stadion_heli_spawn_2","civ","Bruce's New & Used Trucks"]
];

this addAction[
	localize"STR_MAR_Helicopter_Shop",
	life_fnc_vehicleShopMenu,
	["civ_air",civilian,["stadion_heli_spawn_1","stadion_heli_spawn_2"],"civ","Carl's Airial Auto's"]
];

this addAction[localize"STR_Shops_W_Gun",life_fnc_weaponShopMenu,"gun",0,false,false,"",' license_civ_dvg && license_civ_gun && playerSide == civilian'];

this addAction[localize "STR_Shops_C_Gun",life_fnc_clothingMenu,"gun_clothing",0,false,false,"",' license_civ_dvg && license_civ_gun && playerSide == civilian'];

this addAction[
	format[
		"%1 ($%2)", localize (getText(missionConfigFile >> "Licenses" >> "gun" >> "displayName")),
		[(getNumber(missionConfigFile >> "Licenses" >> "gun" >> "price"))] call life_fnc_numberText
	],
	life_fnc_buyLicense,"gun",0,false,false,"",' license_civ_dvg && !license_civ_gun && playerSide == civilian '
];

this addAction[localize"STR_MAR_Rebel_Market",life_fnc_virt_menu,"rebel"];

this addAction[localize"STR_MAR_Rebel_Clothing_Shop",life_fnc_clothingMenu,"reb",0,false,false,"",' license_civ_dvg && playerSide == civilian && license_civ_rebel && playerSide == civilian'];

this addAction[localize"STR_MAR_Rebel_Weapon_Shop",life_fnc_weaponShopMenu,"rebel",0,false,false,"",' license_civ_dvg && playerSide == civilian && license_civ_rebel && playerSide == civilian'];

this addAction[
	localize"STR_MAR_W_E_Vehicle Shop",
	life_fnc_vehicleShopMenu,
	["reb_car",civilian,["stadion_heli_spawn_1","stadion_heli_spawn_2"],"reb","Rebel Motorpool - DVG Base"],
	0,
	false,
	false,
	"",
	' license_civ_dvg && playerSide == civilian && license_civ_rebel'
];

this addAction[
	format["%1 ($%2)",localize (getText(missionConfigFile >> "Licenses" >> "rebel" >> "displayName")), [(getNumber(missionConfigFile >> "Licenses" >> "rebel" >> "price"))] call life_fnc_numberText],
	life_fnc_buyLicense,
	"rebel",
	0,
	false,
	false,
	"",
	' license_civ_dvg && playerSide == civilian && !license_civ_rebel && playerSide == civilian '
];

this addAction[localize"STR_Shops_Gang",life_fnc_virt_menu,"gang",0,false,false,"", ' license_civ_dvg && playerSide == civilian'];

this addAction[localize"STR_MAR_Armament",life_fnc_weaponShopMenu,"gang",0,false,false,"",' license_civ_dvg && playerSide == civilian'];

this addAction[localize"STR_Shops_C_Gang",life_fnc_clothingMenu,"gang_clothing",0,false,false,"",' license_civ_dvg && playerSide == civilian'];

this setObjectTextureGlobal[0, "textures\\dvg.jpg"]

""".replace('"', '""').replace("\r", " ").replace("\n", " ").replace("\t", " ")

#
# main function
#
if __name__ == "__main__":
	with open(sys.argv[1], "r") as file_reader:
		for line in file_reader:
			if line.find("class Item") > 0:
				if line.find("this enableSimulation false;") > 0:
					for shop in shops:
						if line.find(shop) > 0:
							for shop_location in shop_locations:
								if line.find(shop_location) > 0:
									line = line.replace("this enableSimulation false;", "this enableSimulation false;%s;" % shop_actions)

			output_buffer.append(line.replace("\r", "").replace("\n", ""))

	for line in output_buffer:
		print line

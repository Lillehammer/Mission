
SLICE = usr/bin/sliceClassVehicles.sh

MISSIONBUILDER = bin/missionbuilder.py

CLASSVEHICLE_SCRIPT = bin/injector.sh Vehicles $(@)

CLASSGROUP_SCRIPT = bin/injector.sh Groups $(@)

ITEM_MODS = idpatcher lamps shops billboards ammocrates

TARGETS = clean tmp AUTOGEN vanilla mapping classVehiclesMapping $(ITEM_MODS) vanilla_mission mapping_mission

VANILLA_TMP = AUTOGEN/vanilla
MAPPING_TMP = AUTOGEN/mapping

VANILLA_MISSION = tmp/vanilla/mission.sqm
MAPPING_MISSION = tmp/mapping/mission.sqm

MKT = mkdir -pv $(@)/vanilla && mkdir -pv $(@)/mapping

all: $(TARGETS)

tmp:
	$(MKT)
	
AUTOGEN:
	$(MKT)

vanilla:
	rsync -Pavpx src/mission.sqm/. AUTOGEN/vanilla/.

mapping:
	rsync -Pavpx src/mission.sqm/. AUTOGEN/mapping/.

classVehiclesMapping:
	sed -i 's,\r,,g;' $(SLICE)
	find ../Mapping -type f -ipath "*/mission*.sqm" | sort | uniq | \
		xargs -n1 --no-run-if-empty $(SLICE) | \
			tee -a AUTOGEN/mapping/classMission/classVehicles.sqm

#
# Laptop_Device
#
shops:
	$(CLASSVEHICLE_SCRIPT)

#
# switches on enableSimulation for lamps in the mission.sqm
#
lamps:
	$(CLASSVEHICLE_SCRIPT)

#
# adds the armalife logo to all billboards on the map
#
billboards:
	$(CLASSVEHICLE_SCRIPT)

#
# removes everything from any ammo crate placed with xcam
#
ammocrates:
	$(CLASSVEHICLE_SCRIPT)

#
# patches class ItemXXX and id=YYY values in the mission.sqm
#
idpatcher:
	$(CLASSVEHICLE_SCRIPT)

vanilla_mission:
	$(MISSIONBUILDER) AUTOGEN/vanilla $(VANILLA_MISSION)

mapping_mission:
	$(MISSIONBUILDER) AUTOGEN/mapping $(MAPPING_MISSION)

clean:
	rm -rfv AUTOGEN
	rm -rfv tmp

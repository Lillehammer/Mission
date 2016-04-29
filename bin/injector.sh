#!/bin/bash

set -e

CLASS="${1}"

SCRIPT="${2}"

for TYPE in vanilla mapping; do
	./usr/bin/"${SCRIPT}.py" "AUTOGEN/${TYPE}/classMission/class${CLASS}.sqm" >"AUTOGEN/${TYPE}/classMission/class${CLASS}.sqm2"
	mv -v "AUTOGEN/${TYPE}/classMission/class${CLASS}.sqm2" "AUTOGEN/${TYPE}/classMission/class${CLASS}.sqm"
done

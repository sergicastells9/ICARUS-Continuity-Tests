#!/bin/bash

ARG1={$1:-}
ARG2={$2:-"y"}
ARG3=$3
cd /icarus/app/users/castells/my_test_area/
echo "Moved to ICARUS test environment:"; pwd
if [ "$2" = "n" ]
then
source ./start_root/initialize_icarus.sh
cd /icarus/app/users/castells/my_test_area/$1
echo "Not starting ROOT."
fi
if [ "$2" = "y" ]
then
echo "Initialing ROOT..."
source ./start_root/initialize_icarus.sh
cd /icarus/app/users/castells/my_test_area/$1
echo "Starting ROOT:"
root -l $3
fi
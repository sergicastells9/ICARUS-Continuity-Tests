#! /bin/sh

source /cvmfs/icarus.opensciencegrid.org/products/icarus/setup_icarus.sh
setup icaruscode v06_79_00 -qe15:prof
export PYTHONUSERBASE=/icarus/app/users/wketchum/python_libs
export PYTHONPATH=$PYTHONUSERBASE/bin:$PYTHONPATH
export PATH=$PYTHONUSERBASE/bin:$PATH


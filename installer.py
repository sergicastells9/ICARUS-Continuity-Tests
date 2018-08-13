#written by Sergi Castells

import subprocess as sp
import zipfile

icarus_dest = ""
python_dest = ""

print("\nDo no include a trailing \"/\" in the path.\n")
icarus_dest = raw_input("Absolute filepath for ROOT code install:\n")
icarus_machine = "icarusgpvm01.fnal.gov"
print("")
python_dest = raw_input("Absolute filepath for Python code install:\n").strip('\n')
python_machine = raw_input("Machine (include fnal.gov) location:\n").strip('\n')
print("")
user = raw_input("User:\n").strip('\n')

print("\nInstall confirmation:\n\n \t ROOT -- %s \n \t Machine -- %s \n\n \t Python -- %s\n \t Machine -- %s \n\n \t User: %s\n" % (icarus_dest,icarus_machine,python_dest,python_machine,user))

check = True
while(check):
	confirm = raw_input("Confirm install? (Y/n): ")
	
	if(confirm == "Y"):
		check = False
                print("\nInstall initiated.\n")
		
		with zipfile.ZipFile('./code_for_install.zip','r') as code:
			code.extractall('./install_code')
		
		sp.call(['ssh','-Y','%s@%s' % (user,icarus_machine),'mkdir -p %s/start_root' % icarus_dest])
                sp.call(['scp','./install_code/initialize_icarus.sh','%s@%s:%s/start_root' % (user,icarus_machine,icarus_dest)])
	elif(confirm == "n"):
		check = False
		print("Install aborted.")
	else:
		print("Please input a valid response.\n")


if(confirm == "Y"):
	mv2ic = """#!/bin/bash

ARG1={$1:-}
ARG2={$2:-"y"}
ARG3=$3
cd %s/
echo "Moved to ICARUS test environment:"; pwd
if [ "$2" = "n" ]
then
source ./start_root/initialize_icarus.sh
cd %s/$1
echo "Not starting ROOT."
fi
if [ "$2" = "y" ]
then
echo "Initialing ROOT..."
source ./start_root/initialize_icarus.sh
cd %s/$1
echo "Starting ROOT:"
root -l $3
fi
""" % (icarus_dest,icarus_dest,icarus_dest)

	with open('mv2ic.txt','w') as file:
		file.write(mv2ic)
	
	sp.check_output(['scp','mv2ic.txt','%s@%s:/%s' % (user,icarus_machine,icarus_dest)])
	sp.Popen(['ssh','-Y','%s@%s' % (user, icarus_machine),'mv','%s/mv2ic.txt' % icarus_dest,'%s/mv2ic.sh' % icarus_dest])
	sp.Popen(['ssh','-Y','%s@%s' % (user, icarus_machine),'chmod','+x','%s/mv2ic.sh' % icarus_dest])
        
	sp.check_output(['scp','./install_code/run_fast.c','%s@%s:%s' % (user,icarus_machine,icarus_dest)])
	sp.check_output(['scp','./install_code/analyze.c','%s@%s:%s' % (user,icarus_machine,icarus_dest)])
	
	sp.check_output(['scp','./install_code/test_stats.txt','%s@%s:%s' % (user,python_machine,python_dest)])
	sp.check_output(['scp','./install_code/scope_reader.py','%s@%s:%s' % (user,python_machine,python_dest)])
	sp.check_output(['scp','./install_code/DataLoader.py','%s@%s:%s' % (user,python_machine,python_dest)])
	sp.check_output(['scp','./install_code/waveform_id.txt','%s@%s:%s' % (user,python_machine,python_dest)])
	sp.check_output(['scp','./install_code/waveform_list.txt','%s@%s:%s' % (user,python_machine,python_dest)])

	
	sp.check_output(['rm','-r','./install_code'])
	sp.check_output(['rm','mv2ic.txt'])
	
	sp.check_output(['rm','code_for_install.zip'])
	
	sp.check_output(['reset'])

	print("Install completed successfully.")

#!/usr/bin/python

# Script composed by Young Chen
# This script is to do the experiment outside measuring the cell information.
# Associated scripts files are MRT-test.sh iperf3 for UL/DL python files
# Extra applications are QLog of Quectel
# External HW is Solid disk


# test flow (The harddisk must be linked on the plateform.)
# 1. initialize a ramdisk directory in the /tmp 
# 2. send ATE0 to disable the echo function from module
# 3. cat the return value to a log file
# 4. QLog to /tmp/ramdisk  
# 5. periodically check the files and move them to HDD
# Output files will be
    # log: at command return value
    # file-time-log: time of qxdm files  
    # tcp-file: tcpdump file

import os
import sys
import datetime as dt




if __name__ == '__main__':


    # top to monitor	

    # 
    # print(sys.argv[0])
    if (sys.argv[1] == 'set'):
        print('set')
        os.system('echo "true" > enable')
        if (not os.path.isdir('tcpdump-files')):
            os.system('mkdir tcpdump-files')		
    #	os.system('./MRT-test.sh ramdisk')
        os.system('./MRT-test.sh exp_init')
        os.system('./MRT-test.sh exp')
    #	os.system('tcpdump net 140.112.20.182 -w tcpdump-files/tcp-file- -C 200M &')
        # os.system('/home/work/quectel/QLog -s /tmp/ramdisk')

    if (sys.argv[1] == 'start'):
        print('start to tcpdump, iperf & QLog')
        os.system('python handover-scan.py tcp &')
        #os.system('tcpdump net 140.112.20.182 -w tcpdump-files/tcp-file- -C 200M &')
        os.system('python iperf-script-UL.py &')
        os.system('python iperf-script-DL.py &')
    #	os.system('/home/work/quectel/QLog -s /tmp/ramdisk')

    if (sys.argv[1] == 'tcp'):
        t = dt.datetime.today()
        n = '-'.join([str(x) for x in[ t.year, t.month, t.day, t.hour, t.minute, t.second]])
        os.system('tcpdump net 140.112.20.183 -w tcpdump-files/' + n + ' &')

    if(sys.argv[1] == 'stop'):
        os.system('echo "false" > enable')
        os.system('killall -9 tcpdump')
    #	os.system('mv /tmp/ramdisk/* /home/work/young/ssd-mount/')

        os.system('killall -9 iperf3')
    #	os.system('killall -9 QLog')
#	if(sys.argv[1] == 'reset'):
    #	os.system('umount /home/work/young/ssd-mount')

    #	os.system('./MRT-test.sh ramdiskfree')
    # 

    # thread for experiment
    # while loop script of iperf for UL -D
    # while loop script of iperf for DL -D



    # stop echo "false" > enable time to stop? variable=input() in while loop

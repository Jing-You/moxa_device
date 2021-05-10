import os
import sys
import datetime as dt
import time
if __name__ == '__main__':
    t = dt.datetime.today()
    os.system('iperf3 -c 140.112.20.183 -p 3230 -u -l 250 -b 200k -t 7200')

import os
import sys


if __name__ == '__main__':
    os.system('iperf3 -c 140.112.20.183 -R -p 3231 -l 250 -b 200k -u -t 7200') 

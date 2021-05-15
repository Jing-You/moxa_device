import os
import sys


if __name__ == '__main__':
    os.system('iperf3 -c 140.112.20.183 -R -p 3231 -l 250 -b 200k -u -t 7200') 



# import os
# import sys
# import datetime as dt
# import time
# if __name__ == '__main__':



#     t = dt.datetime.today()
#     os.system('iperf3 -c 140.112.20.183 -p 3230 -u -l 250 -b 200k -t 7200')



import os
import sys
import datetime as dt

if __name__ == '__main__':
    # func = sys.argv[1]
    # port = sys.argv[2]
    file= open('enable','r')
    check=file.readline()
    file.close()
    number=0

    if not os.path.exists("iperf3_log"):
        os.system("mkdir iperf3_log")

    while (check == 'true\n') and number < 10:
        t = dt.datetime.today()
        n = '-'.join([str(x) for x in[ t.year, t.month, t.day, t.hour, t.minute, t.second]])
        print(r'iperf3 -c 140.112.20.183 -p 3231 -R -u -V -t 7200 --logfile ./iperf3_log/RL-'+ str(number) + '-' + n )
        os.system(r'iperf3 -c 140.112.20.183 -p 3231 -R -u -V -t 7200 --logfile ./iperf3_log/RL-'+ str(number) + '-' + n )
        file= open('enable','r')
        check=file.readline()
        file.close()
        number+=1
    # os.system('echo "false" > enable')
    # print(check)
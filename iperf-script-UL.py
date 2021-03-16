import os
import sys


if __name__ == '__main__':
	# func = sys.argv[1]
	# port = sys.argv[2]
	file= open('enable','r')
	check=file.readline()
	file.close()
	number=0
	while (check == 'true\n'):
		# os.system('iperf3 -c bouygues.iperf.fr -p 9206 --logfile UL-'+ str(number))
		os.system('iperf3 -c 140.112.20.182 -p 3252 -u -t 7200 --logfile UL-'+ str(number))
		file= open('enable','r')
		check=file.readline()
		file.close()
		number+=1
	# os.system('echo "false" > enable')
	# print(check)

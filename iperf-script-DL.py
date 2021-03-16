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
		# os.system('iperf3 -c bouygues.iperf.fr -R -p 9207 --logfile DL-'+ str(number))
		os.system('iperf3 -c 140.112.20.182 -R -p 3251 -u -t 7200 --logfile DL-'+ str(number)) 
		file= open('enable','r')
		check=file.readline()
		file.close()
		number+=1
	# os.system('echo "false" > enable')
	# print(check)

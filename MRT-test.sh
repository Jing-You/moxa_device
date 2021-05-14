#!/bin/bash


exp_init()
{
# AT port
	device='/dev/ttyUSB2'
# time duration to check
	t_check=0
	t_up=10
	file='./device_log/log-at-'
	file="${file}`(date +%Y%m%d%H%M)`"
	echo 'true' > enable
	echo 'ATE0' > "$device"
	echo 'AT+QNWPREFCFG="nsa_nr5g_band"' > "$device"
	sleep 0.5
	cat "$device" > $file &
	echo 'AT' > "$device"
	sleep 0.5
	#mount -t ntfs-3g /dev/sda1 /home/work/young/ssd-mount
}

test1()
{
	exp_init
	for i in {1..5}
	do
		echo 'at+qeng="servingcell"' >> "$device"
		sleep 0.5
		echo 'at+QLTS=2' >> "$device"
		sleep 0.5

		if [ $t_check == $t_up ]
		then
			t_check=0
			echo "$t_check"
			echo "reset"
		else
			t_check=$((t_check+1))
			echo "$t_check"
			echo "counting"
		fi

	done

	killall cat
	cat log
}

ramdisk()
{
	mkdir /tmp/ramdisk
	chmod 777 /tmp/ramdisk
	mount -t tmpfs -o size=6G tmpfs /tmp/ramdisk/
	touch /tmp/ramdisk/initialfile
       	echo "/tmp/ramdisk initialization done"
	df -h	
}
ramdiskfree()
{
	moveall
	umount /tmp/ramdisk
	rm -r /tmp/ramdisk/
}

moveall()
{
	mv /tmp/ramdisk/* ./
}


check()
{
	numoffile=`find /tmp/ramdisk -maxdepth 1 -type f | wc -l`
	numoffile_tcpdump=`find tcpdump-files/ -maxdepth 1 -type f | wc -l`
#	echo "$numoffile"
	filename=`ls /tmp/ramdisk -t | tail -1`
#	curdir=$PWD
	if [ $numoffile -gt 1 ]
	then
		temp=`ls /tmp/ramdisk -lht --time-style=full-iso | tail -1`
		mv /tmp/ramdisk/"$filename" /home/work/young/ssd-mount/"$filename"
		echo "$temp" >> file-time-log
		echo "$filename moving done"
	else
		echo "No target file to be moved"
	fi
	if [ $numoffile_tcpdump -gt 1 ]
	then

		filename=`ls tcpdump-files/ -t | tail -1`
		mv tcpdump-files/"$filename" /home/work/young/ssd-mount/
	else
		echo "No tcpdump files to be moved"
	fi
}

t()
{
#	echo "true" > enable
#	en=$(cat enable)
#	echo "$en"
#	rm enable
	file='log-'
	file="${file}`(date +%Y%d)`"
	echo "$file"


}



exp()
{
#	exp_init
	device='/dev/ttyUSB2'
	en=$(cat enable)
	t_check=0
	t_up=10
#	for i in {1..100}
	while $en
	do
		en=$(cat enable)

		echo 'at+qeng="servingcell"' > "$device"
		sleep 0.5
		echo 'at+qeng="neighbourcell"' > "$device"
		sleep 0.5
		echo 'at+QLTS=2' > "$device"
		sleep 0.5

		if [ $t_check == $t_up ]
		then
			t_check=0
			echo "$t_check"
			echo "reset & checking"
			#check
		else
			t_check=$((t_check+1))
			echo "counting $t_check"
		fi
	
	done

	killall cat
#	cat log
}
# testing start
$1

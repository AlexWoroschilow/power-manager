#!/bin/sh

for file in /etc/powermanager/*
do
	if [ -f $file -a -x $file ]
	then
		exec `$file true` >> /dev/null
	fi
  
done

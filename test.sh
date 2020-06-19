#!/bin/bash

st=$1
ed=$2
inc=$3

while [ `$st < $ed|bc` -eq 1 ]
do
	st=`$((st+$inc))|bc`
	echo $st
done

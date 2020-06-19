#!/bin/bash

#conda activate bsn

#ulimit -n 65535
low=`echo 0.0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5`
high=`echo 0.5 0.55 0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95 1`
count=0
tot=120

python main.py --module TEM --mode inference --customized_data --actioness_loss_weight 0.25
python main.py --module PGM

for l in $low
do
	for h in $high
	do
		step=0
		tot_step=2
		echo Trial $count out of $tot
	
		echo Step [$step/$tot_step]
		python main.py --module PEM --mode inference --checkpoint_path ./checkpoint --pem_high_iou_thres $h --pem_low_iou_thres $l
		step=$((step+1))
	
		echo Step [$step/$tot_step]
		python main.py --module Post_processing --actioness_loss_weight 0.25 --pem_high_iou_thres $h --pem_low_iou_thres $l
		step=$((step+1))
	
		count=$((count+1))
	done
done

#!/bin/bash

for i in {1..8}
do
	python Controller.py > $i.out&
	sleep 4
done

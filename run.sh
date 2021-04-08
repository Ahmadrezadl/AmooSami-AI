#!/bin/bash

for i in {1..8}
do
	python Controller.py > logs/$i.out&
	sleep 4
done

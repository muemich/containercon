#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import time
import datetime
import RPi.GPIO as io
import paramiko

io.setmode(io.BCM)

magnetic_pin = 23

ssh = paramiko.SSHClient()
ssh.connect('IP', username='username', password='password')

io.setup(magnetic_pin, io.IN, pull_up_down=io.PUD_UP)  # activate input with PullUp
counter = 0 # variable to count rounds
register = 0 # variable to control the sensor status
distance = 0while True:
	if io.input(magnetic_pin): 
		if register==0:
			counter += 1
			register = 1		
	else:
		if register==1:
			register = 0
	time.sleep(0.01) # performs checks every 0.01 seconds
	
    if counter%30==0:
    		ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("kubectl ...")
		
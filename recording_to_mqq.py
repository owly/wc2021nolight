import serial
import paho.mqtt.publish as publish
import time
import sys
import datetime		
import time		
import glob
import os
from time import sleep
import pandas as pd
import sys


offset = 0
if (len(sys.argv) > 1):
	input_file = sys.argv[1]
if (len(sys.argv) > 2):
	offset = sys.argv[2]
else:
	list_of_files = glob.glob('./recordings/*') # * means all if need specific format then *.csv
	input_file = max(list_of_files, key=os.path.getctime)

# .\mos158\mosquitto_sub.exe -h 192.168.18.103 -v -t test_channel
# .\mos158\mosquitto_sub.exe -h localhost -v -t test_channel

# MQTT_SERVER = "192.168.18.105"
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
 
offset = pd.to_timedelta(offset)

# f = open(latest_file, "r")
with open(input_file) as file:
  lines = [i.strip() for i in file]

while(True):
	start_time = datetime.datetime.now()
	for l in lines: 
		now = datetime.datetime.now() + offset
		time = l.split(" ")[0]
		data = l.split(" ")[1] +  " " + l.split(" ")[2] 
		td = pd.to_timedelta(time)
		if (td < offset):
			continue
		if (td + start_time > now):
			diff = td + start_time - now 
			sleep(diff.total_seconds())
		publish.single(MQTT_PATH, data, hostname=MQTT_SERVER)
		print("sending:")
		print(data)


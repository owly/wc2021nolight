import serial
import paho.mqtt.publish as publish
import time
import sys
import datetime		
import time		
from serial.tools.list_ports import comports
 
# .\mos158\mosquitto_sub.exe -h 192.168.18.103 -v -t test_channel
# .\mos158\mosquitto_sub.exe -h localhost -v -t test_channel

# MQTT_SERVER = "192.168.18.105"
MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
 

# s = serial.Serial('/dev/ttyUSB0')
devs = comports()
for i in range(len(devs)):
  print(f'{i}":"{devs[i]}')
com = int(input())
print("connecting to port ") 
# dev = devs[len(devs) - 1].device
dev = devs[com].device
print(dev)
serial_com = serial.Serial(dev)
print(serial_com)
start_time = datetime.datetime.now()
file_time = start_time.strftime("%y_%m_%d_%H_%M_%S")
# file_time = datetime.datetime.timestamp()
f = open("recordings/" + str(file_time) + ".txt", "w")
while True:
	data = serial_com.readline()[:-2] #the last bit gets rid of the new-line chars
	print(data)
	if data:
		chime = data.split()[0]
		mvt = int(data.split()[1])
		data_to_send = str(int(chime)) + " " + str(mvt)
		publish.single(MQTT_PATH,data_to_send, hostname=MQTT_SERVER)
		now = datetime.datetime.now()
		diff = now - start_time
		f.write(str(diff) + " " + str(data_to_send) + "\n")




#		data = data.decode("utf-8") 
		print("sending:")
		print(data_to_send)
#		a = data.split()
#		print ("num:")
#		print (type(a[0]))
#		print (a[0])
#		print ("val:")
#		print (a[1])

# 		res = s.read()
# print(res)


f.close()
import serial

s = serial.Serial('COM6')
while True:
	data = s.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print(data)
# 		res = s.read()
# print(res)
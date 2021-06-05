import serial

s = serial.Serial('/dev/ttyUSB0')
while True:
	data = s.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		data = data.decode("utf-8") 
		print(data)
		a = data.split()
		print ("num:")
		print (type(a[0]))
		print (a[0])
		print ("val:")
		print (a[1])

# 		res = s.read()
# print(res)



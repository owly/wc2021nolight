Start-Process .\mos158\mosquitto.exe
$msub = ".\mos158\mosquitto_sub.exe"
$arguments = "-h localhost -v -t test_channel"
start-process $msub $arguments 


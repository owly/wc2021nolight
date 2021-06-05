# importing the requests library 
import requests 

# defining the api-endpoint 
# API_ENDPOINT = "http://localhost:9876/drumify"
API_ENDPOINT = "http://drumbot.glitch.me/drumify"


# data to be sent to api 
data = {"notes":
	[{"pitch":48,"velocity":40,"program":26,"startTime":1.3293333333333308,"endTime":1.5793333333333308}
	,{"pitch":53,"velocity":40,"program":26,"startTime":1.838666666666665,"endTime":2.088666666666665}
	,{"pitch":57,"velocity":40,"program":26,"startTime":2.34,"endTime":2.59}
	,{"pitch":59,"velocity":40,"program":26,"startTime":2.9079999999999977,"endTime":3.1579999999999977}
	]
	,"tempos":[{"qpm":120}]
	,"totalTime":4
	,"temperature":1}
# data = {'api_dev_key':API_KEY, 
# 		'api_option':'paste', 
# 		'api_paste_code':source_code, 
# 		'api_paste_format':'python'} 

# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 

# extracting response text 
re = r.text 
print("response:%s"%re) 

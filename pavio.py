#try:
if True:
	import os
	import time
	import json
	import requests
	import time
	import pyupm_grove as grove

	from random import randint
	url ='https://auth.written28.hasura-app.io/login'
	data={"username":"admin_pavio","password":"password"}
	data_json = json.dumps(data)
	headers = {'Content-type': 'application/json'}
	response = requests.post(url, data=data_json, headers=headers)
	d=json.dumps(response.json())
	json1_data =json.loads(d)['auth_token']
	json2_data =json.loads(d)['hasura_roles']
	json3_data =json.loads(d)["hasura_id"]
	k1=json2_data
	headers1={'Content-type': 'application/json','Authorization':'Bearer '+json1_data,'X-Hasura-User-Id':str(json3_data),"X-Hasura-Role":str(k1[0])}
	url1 ='https://data.written28.hasura-app.io/v1/query'

#except:
	#print ("import error plz check your import module")


def hazura(val,fl):
	#try:
	if True:


		k1={"intel_Temp":
		           {
		           "bpm":val
		           }
		}
		#d1=json.dumps(k1)

		datain={
		"type": "insert",
	    "args": {
	        "table": "pavio_intel_temp_readings",
	        "returning": [
	            "id"
	        ],
	        "objects": [
	            {
				"value":k1,
				"flag":1,
				"scenario":fl
	            }
	        ]
	    }
	}

		data_json = json.dumps(datain)
		response = requests.post(url1,headers=headers1, data=data_json)
		print data_json,url1,headers1

	#except :
		#print ("hazura showing error")






#50 to 250




while True:
	#try:
	if True:
		# Create the temperature sensor object using AIO pin 0
		temp = grove.GroveTemp(0)
		print temp.name()

		# Read the temperature ten times, printing both the Celsius and
		# equivalent Fahrenheit temperature, waiting one second between readings
		for i in range(0, 10):
		    celsius = temp.value()
		    fahrenheit = celsius * 9.0/5.0 + 32.0;
		    print fahrenheit, celsius
		    val=fahrenheit, celsius
		    time.sleep(1)
		    hazura(val,fl)
		# Delete the temperature sensor object
		del temp

	#except:
		#print ("error in main function ")

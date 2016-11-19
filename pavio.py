try:

	import os
	import time
	import json
	import requests
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

except:
	print ("import error plz check your import module")


def hazura(val,fl):
	try:


		k1={"Heart Rate":
		           {
		           "bpm":val
		           }
		}
		#d1=json.dumps(k1)

		datain={
		"type": "insert",
	    "args": {
	        "table": "pavio_readings",
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

	except :
		print ("hazura showing error")











while True:
	try:


		Userinput=int(input("Enter your option "))


		if (Userinput is 1):
			#mid_to_high
			mid_to_high=[60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]

			for i in range(10):
				print ("mid_to_high",mid_to_high[randint(0,9)],"bpm")
				v=str(mid_to_high[randint(0,9)])
				hazura(v,1)

				time.sleep(1)

			for i in range(10):
				print("mid_to_high",mid_to_high[randint(5,14)],"bpm")
				v=str(mid_to_high[randint(5,14)])
				hazura(v,1)
				time.sleep(1)

			for i in range(10,15):
				print("mid_to_high",mid_to_high[i],"bpm")
				v=str(mid_to_high[i])
				hazura(v,1)
				time.sleep(1)





		elif (Userinput is 2):
			#mid_to_low
			mid_to_low=[120,110,102,103,105,100,98,87,90,93,80,74,70,60,50]


			for i in range(10):
				print ("mid_to_low",mid_to_low[randint(0,9)],"bpm")
				v=str(mid_to_low[randint(0,9)])
				hazura(v,2)
				time.sleep(1)

			for i in range(10):
				print("mid_to_low",mid_to_low[randint(5,15)],"bpm")
				v=str(mid_to_low[randint(5,15)])
				hazura(v,2)
				time.sleep(1)

			for i in range(10,15):
				print("mid_to_low",mid_to_low[i],"bpm")
				v=str(mid_to_low[i])
				hazura(v,2)
				time.sleep(1)


		elif (Userinput is 3):
			#low mid to high mid 
			low_mid_to_high_mid=[120,113,110,102,103,105,100,90,95,80,85,70,73,60]

			for i in range(10):
				print ("low_mid_to_high_mid",strlow_mid_to_high_mid[randint(0,9)],"bpm")
				v=str(low_mid_to_high_mid[randint(0,9)])
				hazura(v,3)
				time.sleep(1)

			for i in range(10):
				print("low_mid_to_high_mid",low_mid_to_high_mid[randint(5,14)],"bpm")
				v=str(low_mid_to_high_mid[randint(5,14)])
				hazura(v,3)
				time.sleep(1)

			for i in range(10,14):
				print("low_mid_to_high_mid",low_mid_to_high_mid[i],"bpm")
				v=str(low_mid_to_high_mid[i])
				hazura(v,3)
				time.sleep(1)


	except:
		print ("error in main function ")
















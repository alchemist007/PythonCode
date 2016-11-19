#try:
if True:
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

#except:
	#print ("import error plz check your import module")


def hazura(val,val1,val2,val3,fl):
	#try:
	if True:




		k1={"Heart_Rate":
		           {
		           "bpm":val
		           },
		           "Blood_Pressure":
		           {
		           "Hg":val1
		           },
		           "temp":
		           {
		           "F":val2
		           },
		           "Blood_sugar":
		           {
		           "Dl":val3
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

	#except :
		#print ("hazura showing error")






#50 to 250


#1 hardrate
#preshure
#2 temp
#3 gl

while True:
	#try:
	if True:


		Userinput=int(input("Enter your option "))


		if (Userinput is 1):
			#mid_to_high
			mid_to_high=[60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
			temp_mid_high=[90,92,93,94,95,96,97,98,99,100,105,110,115,120]
			Blood_Pressure_mid_high=['90/60','92/61','93/62','95/63','96/65','100/69','102/71','102/73','120/80','121/81','122/82','125/81','123/83','124/84','125/81','126/82','123/83','146/106','149/108','152/109']
			Blood_sugar_mid_high=[70,72,75,77,79,80,80,85,90]
			for i in range(10):
				print ("mid_to_high",mid_to_high[randint(0,9)],"bpm")
				v=str(mid_to_high[randint(0,9)])
				v2=str(temp_mid_high[randint(0,9)])
				v1=str(Blood_Pressure_mid_high[randint(0,15)])
				v3=str(Blood_sugar_mid_high[randint(0,8)])
				hazura(v,v1,v2,v3,1)
				# hazura(v,1,1)

				# hazura(v2,1,2)

				# hazura(v1,1,3)

				# hazura(v3,1,4)

				time.sleep(1)

			for i in range(10):
				print("mid_to_high",mid_to_high[randint(5,14)],"bpm")
				v=str(mid_to_high[randint(5,14)])
				# hazura(v,1,1)
				v2=str(temp_mid_high[randint(0,9)])
				v1=str(Blood_Pressure_mid_high[randint(0,15)])
				v3=str(Blood_sugar_mid_high[randint(0,8)])
				hazura(v,v1,v2,v3,1)
				# hazura(v2,1,2)
				# hazura(v1,1,3)
				# hazura(v3,1,4)
				time.sleep(1)

			for i in range(10,15):
				print("mid_to_high",mid_to_high[i],"bpm")
				v=str(mid_to_high[i])
				# hazura(v,1,1)
				time.sleep(1)
				v2=str(temp_mid_high[randint(0,9)])
				v1=str(Blood_Pressure_mid_high[randint(0,15)])
				v3=str(Blood_sugar_mid_high[randint(0,8)])
				hazura(v,v1,v2,v3,1)
				# hazura(v2,1,2)
				# hazura(v1,1,3)
				# hazura(v3,1,4)
				time.sleep(1)




		elif (Userinput is 2):
			#mid_to_low
			mid_to_low=[120,110,102,103,105,100,98,87,90,93,80,74,70,60,50]
			temp_to_low=[80,90,70,63,65,50,55,60,61]
			Blood_Pressure_mid_to_low=['88/59','87/58','86/57','85/56','84/55','83/52','80/51','78/50','77/49','75/49','71/48','68/46','65/45','64/43','62/41','60/38','54/37','52/36','50/34','51/33','47/31','45/29','43/28','41/27','40/25','39/23','38/22','37/20','35/18']
			Blood_sugar_mid_to_low=[100,110,120,130,135,140,150,160,170,180,190,200]
			for i in range(10):
				print ("mid_to_low",mid_to_low[randint(0,9)],"bpm")
				v=str(mid_to_low[randint(0,9)])
				v2=str(temp_to_low[randint(0,6)])
				v1=str(Blood_Pressure_mid_to_low[randint(0,15)])
				v3=str(Blood_sugar_mid_to_low[randint(0,10)])
				hazura(v,v1,v2,v3,2)


				time.sleep(1)

			for i in range(10):
				print("mid_to_low",mid_to_low[randint(5,10)],"bpm")
				v=str(mid_to_low[randint(5,10)])



				v2=str(temp_to_low[randint(0,6)])
				v1=str(Blood_Pressure_mid_to_low[randint(0,10)])
				v3=str(Blood_sugar_mid_to_low[randint(0,10)])

				hazura(v,v1,v2,v3,2)
				time.sleep(1)

			for i in range(8,10):
				print("mid_to_low",mid_to_low[i],"bpm")
				v=str(mid_to_low[i])


				v2=str(temp_to_low[randint(0,6)])
				v1=str(Blood_Pressure_mid_to_low[randint(0,10)])
				v3=str(Blood_sugar_mid_to_low[randint(0,10)])

				hazura(v,v1,v2,v3,2)
				time.sleep(1)


		elif (Userinput is 3):
			#low mid to high mid 
			low_mid_to_high_mid=[120,113,110,102,103,105,100,90,95,80,85,70,73,60]

			temp_to_normal=[90,91,92,93,94,95,97,99,100]
			Blood_Pressure_normal=['135/65','136/67','137/68']
			Blood_sugar_normal=[70,80,90,100,108]
			for i in range(10):
				print ("low_mid_to_high_mid",low_mid_to_high_mid[randint(0,9)],"bpm")
				v=str(low_mid_to_high_mid[randint(0,9)])



				v2=str(temp_to_normal[randint(0,6)])
				v1=str(Blood_Pressure_normal[randint(0,2)])
				v3=str(Blood_sugar_normal[randint(0,4)])
				hazura(v,v1,v2,v3,3)
				time.sleep(1)

			for i in range(10):
				print("low_mid_to_high_mid",low_mid_to_high_mid[randint(5,8)],"bpm")
				v=str(low_mid_to_high_mid[randint(5,9)])



				v2=str(temp_to_normal[randint(0,8)])
				v1=str(Blood_Pressure_normal[randint(0,2)])
				v3=str(Blood_sugar_normal[randint(0,4)])
				hazura(v,v1,v2,v3,3)

				time.sleep(1)

			for i in range(5,8):
				print("low_mid_to_high_mid",low_mid_to_high_mid[i],"bpm")
				v=str(low_mid_to_high_mid[i])



				v2=str(temp_to_normal[randint(0,6)])
				v1=str(Blood_Pressure_normal[randint(0,2)])
				v3=str(Blood_sugar_normal[randint(0,4)])
				hazura(v,v1,v2,v3,3)

				time.sleep(1)


	#except:
		#print ("error in main function ")

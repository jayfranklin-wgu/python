#!/usr/bin/python

import json

with open('json1.json') as f:
		data = json.loads(f.read())

i = 0
for item in data["response"]:
		print ("Network Device ID: " + data["response"][i]["hostname"]")  
		print("\t" + ["managementIpAddress"])
		i += 1

#Author: Zhiao Zhou
#This script shows you number of the active buses and their location at present

from __future__ import print_function
import sys
import os
import json
import urllib

if len(sys.argv) != 3:
    print("Invalid number of arguments, please try python show_bus_locations_zz1749.py [MTAKEY][BUSLINE]")
    sys.exit()

#get the bus info
url = os.getenv("MTAURL1")+sys.argv[1]+os.getenv("MTAURL2")+sys.argv[2]
urllib.urlretrieve(url, os.getenv("PUIDATA")+sys.argv[2]+"info.json")

#read the file
response = open(os.getenv("PUIDATA")+sys.argv[2]+"info.json","r+")
data = response.read().decode("utf-8")
data = json.loads(data)
try:
    activity = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
except KeyError:
    print("there is no such route as: "+sys.argv[2])
    sys.exit()

#print outputs
print("Bus Line : "+sys.argv[2])
print("Number of Active Buses : "+str(len(activity)))
for i in range(len(activity)):
    location = activity[i]["MonitoredVehicleJourney"]["VehicleLocation"].items()
    print("Bus "+ str(i) +" is at latitude "+str(location[0][1])+" and longitude "+str(location[1][1]))
sys.exit()

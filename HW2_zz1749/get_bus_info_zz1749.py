#Author: Zhiao Zhou
#This script shows you info on the next stop location of all buses of a given line

from __future__ import print_function
import sys
import os
import json
import urllib
import pandas as pd
import numpy as np

if len(sys.argv) != 4:
    print("Invalid number of arguments, please try python get_bus_info_zz1749.py [MTAKEY][BUSLINE][BUSLINE.csv]")
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

#get outputs
latitude = []
longitude = []
stop_name = []
stop_status = []
for i in range(len(activity)):
    location = activity[i]["MonitoredVehicleJourney"]["VehicleLocation"].items()
    stopname = activity[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
    stopstatus = activity[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
    latitude.append(location[0][1])
    longitude.append(location[1][1])
    if activity[i]["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
        stop_name.append('N/A')
        stop_status.append('N/A')
    stop_name.append(stopname)
    stop_status.append(stopstatus)

#outputs into dataframe
dataframe = pd.DataFrame({'Latitude':latitude, 'Longitude':longitude, 'Stop Name':stop_name, 'Stop Status':stop_status})

#create csv, save it and print it
dataframe.to_csv(sys.argv[3],index=False)
print("the "+sys.argv[3]+" file has been saved")

data = pd.read_csv(sys.argv[3])
print(data)






sys.exit()

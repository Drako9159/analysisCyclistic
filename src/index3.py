import pandas as pd
from datetime import datetime
from datetime import timedelta
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("./csv/202201-divvy-tripdata.csv")

station = "start_station_name"
bike = "rideable_type"
started = "started_at"
ended = "ended_at"
memberType = "member_casual"

# Clean values NaN
df.rename(columns={station: "Station", bike: "Bike", started: "Started",
          ended: "Ended", memberType: "CasualOrMember"}, inplace=True)
df.dropna(subset=["Station", "Bike", "Started",
          "Ended", "CasualOrMember"], inplace=True)
df = df.loc[:, ["Station", "Bike", "Started", "Ended",
                "CasualOrMember"]].sort_values(by="Started")
###
def getStation():
    data = []
    avist = []
    #lg = df.loc[:,["Station"]]
    lg = df["Station"]
    for row in lg:
        data.append(row)
    data = list(set(data))
    for row in data:
        check = df["Station"].value_counts()[row]
        avist.append(check)
        print(check)



    #print(data)

#print(df["CasualOrMember"].value_counts()["member"])

getStation()
    
# Get Bikes for Members
def getBikesMembers():
    bikeMembers = df.loc[:, ["Bike", "CasualOrMember"]]
    members = df.CasualOrMember.isin(["member"])
    members = bikeMembers[members]
    casual = df.CasualOrMember.isin(["casual"])
    casual = bikeMembers[casual]
    electricM = members["Bike"].value_counts()["electric_bike"]
    classicM = members["Bike"].value_counts()["classic_bike"]
    electricC = casual["Bike"].value_counts()["electric_bike"]
    classicC = casual["Bike"].value_counts()["classic_bike"]
    bikesType = {"customers": ["casual", "members"], "electric_bike": [
        electricC, electricM], "classic_bike": [classicC, classicM]}
    bikesType = pd.DataFrame(bikesType)
    print(bikesType)

#dockedM = members["Bike"].value_counts()["docked_bike"]
started = df.loc[:, ["Started"]]
ended = df.loc[:, ["Ended"]]
# Get Date in minutes
def getTripTime(start, end):
    date1 = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    date2 = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    minutes = (date2 - date1) / timedelta(minutes=1)
    return minutes

def getDate():
    st = df["Started"]
    ed = df["Ended"]
    resume = []
    fechaInicio = []
    fechaFinal = []
    for row in st:
        fechaInicio.append(row)
    for row in ed:
        fechaFinal.append(row)
    cs = 0
    for row in st:
       resume.append(getTripTime(fechaInicio[cs], fechaFinal[cs])) 
       cs = cs + 1
    table = {"trip_minutes": resume, "average" : "lol"}
    mean = pd.DataFrame(table).sort_values(by="trip_minutes")
    average = mean["trip_minutes"].mean()
    print(mean)
    print(average)
 

# Ahora sumar algunas horas. Vamos a parsear la fecha:
# print(df["CasualOrMember"].value_counts()["member"])
##all = list(set(all))

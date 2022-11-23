
#import numpy as np #linear algebra
#import pandas as pd # data processing, CSV file I/O / (e.g. pd.read_csv) 
#import seaborn as sns # data visalization
#import matplotlib.pyplot as plt
#from sklearn.tree import DecisionTreeRegressor
'''
import os
for dirname, _, filenames in os.walk("/csv/202201-divvy-tripdata.csv"):
    for filename in filenames:
        print(os.path.join(dirname, filename))
'''
#data202201 = pd.read_csv("csv/202201-divvy-tripdata.csv")


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data202201 = pd.read_csv("./csv/202201-divvy-tripdata.csv")
#print(data202201.head())

#precio = []
#Promedio de cada 25 muestras
#precioPromedio = precio.rolling(30, min_periods=1).mean()

#Selecciona todos con member 5& casual
members = data202201[data202201["member_casual"] == "member"]
casual = data202201[data202201["member_casual"] == "casual"]
electric_bike = data202201[data202201["rideable_type"] == "electric_bike"]
'''
electric_bike = electric_bike.set_index("started_at")
electric_bike = electric_bike.sort_values(by="started_at")
'''

membersCount = data202201["member_casual"].value_counts()["member"]
casualCount = data202201["member_casual"].value_counts()["casual"]
print(membersCount)

'''
#Mueve la fecha al index
electric_bike = electric_bike.set_index("started_at")
#Ordena por la fecha
electric_bike = electric_bike.sort_values(by="started_at")

started_at = electric_bike["rideable_type"][: MAX_SAMPLES]
plt.plot(started_at, label="Fecha de inicio")
plt.title("Fechas de prueba")
plt.xlabel("Fecha")
#plt.xticks(rotation=90)
plt.ylabel("Fecha Y")
plt.legend()
plt.show()
'''



'''

'''

#print(data202201["member_casual"].value_counts())
#print(data202201["started_at"])

#Graficos
#Máximo de muestras
'''
MAX_SAMPLES = 100
started_at = membersByStarTrip["started_at"][: MAX_SAMPLES]
plt.plot(started_at, label="Fecha de inicio")
plt.title("Fechas de prueba")
plt.xlabel("Fecha")
#plt.xticks(rotation=90)
plt.ylabel("Fecha Y")
plt.legend()
plt.show()
'''

'''
casuales = data202201[data202201["member_casual"] == "casual"]
fecha_inicio = casuales["started_at"]
fecha_final = casuales["ended_at"]
tipoBici = casuales["rideable_type"]

#filas,columnas,eje
plt.subplot(221)
plt.title("Fecha Inicio")
plt.plot(fecha_inicio, label="Bici", color="orange")
plt.legend()

plt.subplot(222)
plt.title("Fecha Final")
plt.plot(fecha_final, label="Fecha final", color="pink")
plt.legend()

plt.subplot(223)
plt.title("Tipo de Bici")
plt.plot(tipoBici, label="Fecha final", color="red")
plt.legend()

plt.subplot(224)
plt.title("Fecha Final")
plt.plot(fecha_final, label="Fecha final", color="black")
plt.legend()
#Para espaciar los elementos
plt.tight_layout()
plt.show()
'''



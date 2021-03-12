import pandas as pd
from os import listdir, mkdir
from os.path import isfile, join
import numpy as np

path = r"C:\Users\U40687\Desktop\curso"

# Punto 1 leemos solo archivos de una carpeta

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

# punto 2 concatenamos todo

df_list = []

for file in onlyfiles:
    df = pd.read_csv(path+"\\"+file,sep=",")
    df_list.append(df)

df = pd.concat(df_list)    

# punto 3 Observar los datos

df.describe()
df.head()

# punto 4 rellenamos con nan valores vacios
df.replace('', np.nan, inplace=True)

#  punto 5 eliminamos aquellos registros duplicados
df=df.set_index("id")
df = df[~df.index.duplicated(keep='first')]

# 6 creamos la columna nueva forma facil
df["edad_real"] = df["age"]*(1+df["bmi"]*0.01)+df["hypertension"]*3

# 7 piechart 

import matplotlib.pyplot as plt

mujer = df[(df["gender"]=="Female")&(df["stroke"]==1)]["gender"].count()
hombre =  df[(df["gender"]=="Male")&(df["stroke"]==1)]["gender"].count()
plt.pie([hombre,mujer],labels  = ["Hombres "+ str(hombre),"Mujeres "+ str(mujer)] )
plt.show()
plt.close()
# 8 barchart

Urbano = df[(df["Residence_type"]=="Urban")&(df["stroke"]==1)]["Residence_type"].count()
Rural =  df[(df["Residence_type"]=="Rural")&(df["stroke"]==1)]["Residence_type"].count()
plt.bar(["Urbano "+ str(Urbano),"Rural "+ str(Rural)],[Urbano,Rural] )
plt.show()
plt.close()

#9 matriz de correlacion y guardado

mkdir(path+"//OUT2//")
df.corr().to_csv(path+"//OUT//"+"correlation_matrix.csv")
df.corr().to_hdf(path+"//OUT//"+"correlation_matrix.h5", key='df', mode='w')


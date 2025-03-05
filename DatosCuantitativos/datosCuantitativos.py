import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import kurtosis
# %% Cargar datos
Data = pd.read_csv('DatosCuantitativos.csv')

# %% Crear histograma
clases = int(round(math.sqrt(len(Data['Temperatura del sello anular']))))
plt.hist(Data['Temperatura del sello anular'], bins=clases, edgecolor='black', color="pink")
plt.xlabel('Temperatura °F')
plt.ylabel('Frecuencia')
plt.title('Histograma Temperatura del sello anular')
plt.grid(True)
plt.show()

# %% Crear diagrama de dispersión
plt.scatter(Data.index, Data['Temperatura del sello anular'], color='blue', marker='o', alpha=0.7)
plt.show()

# %%Tabla de frecuencia
frecuencia = pd.cut(Data['Temperatura del sello anular'], bins=clases).value_counts().sort_index()

#%% Cajas y Bigotes
Datos_lista = (Data['Temperatura del sello anular'].tolist())
plt.boxplot(Datos_lista)
plt.title("Diagrama de caja y bigotes")
plt.ylabel('Temperatura °F')
plt.show()

Q1 = np.percentile(Datos_lista, 25)
Q2 = np.percentile(Datos_lista, 50)
Q3 = np.percentile(Datos_lista, 75)
fs = Q3 - Q1

DatosApartados_izq = []
DatosApartados_der = []
for element in Datos_lista:
    if element<=(Q1-1.5*fs):
        DatosApartados_izq.append(element)
    if element >= (1.5*fs + Q3):
        DatosApartados_der.append(element)

media = np.mean(Datos_lista)
varianza = np.var(Datos_lista)
desvEst = np.std(Datos_lista)

#%%Curtosis
curtosis = kurtosis(Datos_lista)

Data.describe() 
Data.mode()








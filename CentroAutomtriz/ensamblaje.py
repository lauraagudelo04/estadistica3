import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
Data = pd.read_csv('Centro Automotriz.csv')

# Obtener nombres de columnas sin la primera (asumiendo que es un índice o ID)
column_titles = Data.columns.tolist()[1:]

# Calcular las frecuencias totales por categoría de defecto
Total_categories = [sum(Data[element]) for element in column_titles]

# Crear tabla de frecuencias
TablaFrecuencias = pd.DataFrame({
    'Categoria': column_titles,
    'Frecuencias': Total_categories
})

# Calcular la frecuencia relativa
TablaFrecuencias['Frecuencia_relativa'] = TablaFrecuencias['Frecuencias'] / sum(TablaFrecuencias['Frecuencias'])

# Gráfico de barras
plt.figure(figsize=(10, 5))
graph = plt.bar(TablaFrecuencias['Categoria'], TablaFrecuencias['Frecuencias'])

plt.xlabel('Categorías')
plt.ylabel('Frecuencia')
plt.title('Diagrama de barras para tipo de defectos')
plt.xticks(rotation=90, ha='center')

# Agregar etiquetas a las barras
for bar in graph:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')

plt.show()

# Gráfico de pastel
plt.figure(figsize=(8, 8))
plt.pie(
    TablaFrecuencias['Frecuencia_relativa'],
    labels=TablaFrecuencias['Categoria'],
    autopct=lambda p: f'{p:.1f}%', 
    startangle=90
)
plt.title('Distribución porcentual de los defectos')
plt.axis('equal')  # Hace que el gráfico de pastel sea circular
plt.show()

# Ordenar por frecuencia descendente para el diagrama de Pareto
ParetoTable = TablaFrecuencias.sort_values(by='Frecuencias', ascending=False)
ParetoTable['Frecuencia._r_acum'] = ParetoTable['Frecuencia_relativa'].cumsum()

# Gráfico de Pareto
fig, ax1 = plt.subplots(figsize=(10, 5))

# Gráfico de barras
color = 'tab:blue'
ax1.bar(ParetoTable["Categoria"], ParetoTable["Frecuencias"], color=color)
ax1.set_xlabel('Categorías')
ax1.set_ylabel('Frecuencias')

# Ajustar etiquetas en eje X
ax1.set_xticks(range(len(ParetoTable)))
ax1.set_xticklabels(ParetoTable['Categoria'], rotation=90, ha='center')

# Segundo eje Y para la frecuencia relativa acumulada
ax2 = ax1.twinx()
color = 'tab:red'

ax2.plot(ParetoTable['Categoria'], ParetoTable['Frecuencia._r_acum'], color=color, marker='o')
ax2.set_ylabel('Frecuencia Relativa Acumulada', color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Diagrama de Pareto con frecuencia relativa acumulada')
plt.show()

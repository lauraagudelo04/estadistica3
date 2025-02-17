import pandas as pd
import matplotlib.pyplot as plt

Cutting_Data = pd.read_excel(r'.\ManufacturingArea_Data.xlsx', sheet_name="cutting area")
Manufacturing_Data = pd.read_excel(r'.\ManufacturingArea_Data.xlsx', sheet_name="ManufacturingArea")

print(type(Cutting_Data["Fabric_arrival_time"][0]))
print(type(Cutting_Data["Wait_time"][0]))
print(type(Cutting_Data["CUT_BY"][0]))

total_secondsv = Cutting_Data["Wait_time"].dt.total_seconds()

Cutting_Data["wait_seconds"] = total_secondsv

n, bins, patches = plt.hist(Cutting_Data["wait_seconds"],bins=5, edgecolor= 'black')

for i in range(len(patches)):
    height = patches[i].get_height()
    x = patches[i].get_x() + patches[i].get_width() / 2
    plt.text(x, height ,f'{int(height)}', ha='center', va = 'bottom')
    
plt.xlabel('Wait Time(Seconds)')
plt.ylabel('Frequency')
plt.title('Histogram of Wait Time')

plt.show()

summary = Cutting_Data["wait_seconds"].describe()


Temperature=dict()
Humidity=dict()
accTemp=[]
accHum=[]

def get_membership_input(variable_name, accumulator):
    print(f"Enter {variable_name} key:value pairs (one per line, empty line to finish):")
    while True:
        entry = input()
        if not entry:
            break
        
        try:
            key, value = entry.split(':')
            key = float(key)
            value = float(value)
            accumulator.append((key, value))
            variable_dict = Temperature if variable_name == "Temperature" else Humidity
            variable_dict[key] = value
        except ValueError:
            print("Invalid format. Please use key:value format with numbers.")

print("Input membership functions")
get_membership_input("Temperature", accTemp)
get_membership_input("Humidity", accHum)

print("\nTemperature membership function:", Temperature)
print("Humidity membership function:", Humidity)

threshTemp = float(input("Enter threshold temperature: "))
threshHum = float(input("Enter threshold humidity: "))

for i in Temperature.keys():
    if i >= threshTemp:
        accTemp.append((i, Temperature[i]))

for j in Humidity.keys():
    if j >= threshHum:
        accHum.append((j, Humidity[j]))

print("\nAccumulated Temperature membership function:", accTemp)
print("Accumulated Humidity membership function:", accHum)

import pandas as pd
pro=[]
for i in accTemp:
    for j in accHum:
        pro.append((i,j))

print("\nProduct of accumulated membership functions:")
df = pd.DataFrame(pro, columns=['Temperature', 'Humidity'])
print(df)
print("Temperature\tHumidity")
for i in accTemp:
    for j in accHum:
        print(f"{i[0]}:{i[1]}\t\t{j[0]}:{j[1]}")


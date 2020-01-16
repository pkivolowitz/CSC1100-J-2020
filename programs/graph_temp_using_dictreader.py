import csv
from matplotlib import pyplot as plt 

input_file = open('may_6_with_heading.csv')
reader = csv.DictReader(input_file)

yearly_data = {}

for line in reader:
    year = line['date'][0:4]
    if year not in yearly_data:
        yearly_data[year] = { }
    yearly_data[year][float(line['depth'])] = float(line['temperature'])


for year in sorted(yearly_data):
    depths = sorted(list(yearly_data[year]))
    temps = []
    for d in depths:
        temps.append(yearly_data[year][d])
    plt.plot(depths, temps, label='5/6/' + str(year))

plt.style.use('fivethirtyeight')
plt.legend()
plt.title('Lake Mendota - Madison, WI')
plt.xlabel('Depth (Feet)')
plt.ylabel('Temperature (C)')
plt.show()


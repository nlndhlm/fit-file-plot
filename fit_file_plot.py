import fitparse
import datetime
import matplotlib.pyplot as plt



f = fitparse.FitFile('fil3.fit')



date = None

dist = []
height = []
speed = []
heart_rate = []
position_long = []
position_lat = []

for record in f.get_messages("record"):

    for data in record:

        date = record.get_value('timestamp')

        dist.append(record.get_value('distance'))
        height.append(record.get_value('enhanced_altitude'))
        heart_rate.append(record.get_value('heart_rate'))
        speed.append(record.get_value('enhanced_speed'))

        position_long.append(record.get_value('position_long'))
        position_lat.append(record.get_value('position_lat'))
        

# print ut denne for å se oversikten over values
print(record.get_values())

# regne ut snittverdier av fart og puls, må gjøres etter loopen
avg_speed = str(round(sum(speed) / len(speed), 2))
avg_heart_rate = str(round(sum(heart_rate) / len(heart_rate), 2))



# PLOTTING
plt.suptitle(date.strftime("%d. %B %Y - kl. %H:%M"), fontsize=25)

plt.subplot(2, 2, 1)
plt.title('Hjertefrekvens (snitt = ' + avg_heart_rate + ' bpm)')
plt.grid(axis='y')
plt.xlabel('Meter')
plt.ylabel('bpm')
plt.plot(dist, heart_rate)

plt.subplot(2, 2, 2)
plt.title('Fart (snitt = ' + avg_speed + ' m/s)')
plt.grid(axis='y')
plt.xlabel('Meter')
plt.ylabel('m/s')
plt.plot(dist, speed)
# for å unngå den lange halen, kan vi shave vekk 50m i starten av økta:
# plt.plot(dist[50:], speed[50:])

plt.subplot(2, 2, 3)
plt.title('GPS')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.plot(position_long, position_lat)

plt.subplot(2, 2, 4)
plt.title('Høydeprofil')
plt.grid(axis='y')
plt.xlabel('Meter')
plt.ylabel('Høydemeter')
plt.plot(dist, height)



plt.show()

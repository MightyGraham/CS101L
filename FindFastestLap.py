import csv
'''altitude = open ('_GPS.csv', 'r')
altitude2 = open ('_GPS(1).csv', 'r')
while True:
    altitude.readlines()
    for row in altitude:
        alt = row[4]
        print(alt)
    altitude2.readlines()
    for row2 in altitude2:
        alt2 = row[4]
        print(alt2)
    if (alt or alt2):
        if (alt != alt2):
            print(altitude, altitude2)
    else:
    altitude.close()
    altitude2.close()
    break'''

with open('_GPS.csv') as results:
    reader = csv.reader(results)
    for row in reader:
        time = row[0]
        alt = row[4]
with open('_GPS(1).csv') as results2:
    reader2 = csv.reader(results2)
    for row in reader2:
        altitude = row[4]
while True:
    if (alt and altitude):
        if (alt == altitude):
            print(time, alt, altitude)
    else:
        break

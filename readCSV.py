import csv
import matplotlib.pyplot as plt
bTime = False
timeArr = []
greenlandArr = []
antarticaArr = []

with open('landIce.csv', 'rb') as csvfile:
    csvReader = csv.reader(csvfile, delimiter= ' ', quotechar ='|')
    for currRow in csvReader:
        if bTime :
            columns = currRow[0].split(',')
            timeArr.append(columns[0])
            greenlandArr.append(columns[1])
            antarticaArr.append((columns[2]))

        if currRow[0] == 'TIME':
            bTime = True
    plt.plot(timeArr, greenlandArr)
    plt.plot(timeArr, antarticaArr)
    plt.show();


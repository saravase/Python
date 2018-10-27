import csv
with open('example.csv') as csvfile:
    csvdata=csv.reader(csvfile,delimiter=',')
    
    colors=[]
    dates=[]
    
    for c in csvdata:
        color=c[3]
        date=c[0]
        print(color,date)
        colors.append(color)
        dates.append(date)

    print(colors)
    print(dates)

    whatColor=input('Find the date of the color')
    index=colors.index(whatColor)
    print("the date is "+dates[index]+"!!!")

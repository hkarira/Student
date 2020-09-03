import csv
from string import Template

with open("student1.txt", "r") as csv_file:
    d = dict()
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    d = {}
    for row in csv_reader:
        print(row)
        if row["Rollno"] in d:
            d[row["Rollno"]].append((row["StudName"], row["Marks"], row["Subject"]))
        else:
            d.update({row['Rollno'] : [(row["StudName"], row["Marks"], row["Subject"])]})

    filein = open("template.txt")
    src = Template(filein.read())

    for items in dict.keys(d):
        sum = 0
        with open(f"{d[items][0][0]}_{items}.txt", "w") as file_appender:
            for item in d[items]:
                sum += int(item[1])

                p = {"Rollno": items, "StudName" : item[0],"Subject": item[2],"Marks" : item[1]}
                file_appender.write(src.substitute(p))

                #file_appender.write("Id:{}, Name:{}, Marks: {}, Subject: {}".format(items, item[0], item[1], item[2]))
                file_appender.write("\n")
            file_appender.write("Total Marks: {}".format(sum))





import sys
import csv
import mylist

sys.path.append("./Lec04/lab4")
#sys.path.append(r".\Lec04\lab4")
#sys.path.append(".\\Lec04\\lab4")

streetsCSV = r".\Lec04\lab4\streets.csv"
headernames = mylist.listheadernames(streetsCSV)
print(headernames)


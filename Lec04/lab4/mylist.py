import csv
streetsCSV = r".\Lec04\lab4\streets.csv"
#
# with open(streetsCSV, 'r') as csvFile:
#     reader = csv.reader(csvFile)
#     print(reader)
#     headers = reader.__next__()
# #Create a list to save headers
# headerlist = []
#
# for header in headers:
#     headerlist.append(header)
#     #Print the headers list
#     print(headerlist)

# Make a single function for the previous codes
def listheadernames(csvfilepath):
    with open(csvfilepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        headers = reader.__next__()
        headerlist = []
        for header in headers:
            headerlist.append(header)
    csvFile.close()
    return headerlist

headernames=listheadernames(streetsCSV)
print(headernames)

# This function "listheadernames" works the same as df.columns.

if __name__ == "__main__":
    print()
f=open("./Lec04/hello.txt","w") # "./" means "C:/E/PyExc/"
f.write("GISC4317")
f.write("\nHello, World!")
f.write("\nThs is file processing.")
f.close()

f = open ("./Lec04/hello.txt")  # "r" is the default mode
f.read()

f = open ("./Lec04/hello.txt")  # "r" is the default mode
f.read(3)
f.read(5)
f.read(2)

f.seek(12)  # Move the cursor to the 12th byte
f.read()

# readline() reads a line from the file
# readlines() reads all lines from the file and returns a list

f = open ("./Lec04/hello.txt")
f.readline()

f = open ("./Lec04/hello.txt")
read_lines=f.readlines()
read_lines[1]  # To print, specified line number

with open ("./Lec04/hello.txt") as f:
    print(f.readline())

max([1,2,3,4,5])  # Returns the maximum value in the list


# Define function
def my_function(friend_nm):
    print(friend_nm+"This is my function.")

my_function("Emily, ")
my_function("Tobias, ")


# Define function
def my_function(fst_nm,lst_nm):
    print(f"{fst_nm}, This is my function. Did you copy it,{lst_nm} ?")

my_function("Emily", "Tobias")


def my_function(fst_nm,lst_nm = "Tobias"):
    print(f"{fst_nm}, This is my function. Did you copy it,{lst_nm} ?")

my_function("Emily")
my_function("Emily","Lee")


# Use list parameter
def print_list(any_list):
    for item in any_list:
        print(item)

my_list = ["Emily", "Tobias", "Lee"]
print_list(my_list)

fruits = ["Apple", "Banana", "Cherry"]
print_list(fruits)

numbers = [1, 2, 3, 4, 5]
print_list(numbers)


def times_calc(x):
    return 5 * x

calc_val=times_calc(5)

def exp_calc(x,y):
    return x**y

exp_val = exp_calc(5,2)
exp_val = exp_calc(2,5)
print(exp_val)

# Add the directory containing `mymodule.py` to the Python path
import sys
sys.path.append("./Lec04")

# Importing a module and using its function
import mymodule as mx
mx.greeting("Emily")

import importlib
importlib.reload(mx)

mx.p1

# Print the list of built-in libraries
print(sys.builtin_module_names)

import class_ex
p1=class_ex.Person("John", 36)  # Create an instance of the Person class
p1.myfunc()  # We don't have to type class_ex.p1.myfunc() because we have imported the class_ex module


# Read CSV file with pandas

import pandas as pd
df = pd.read_csv("./Lec04/data.csv")  # Read the CSV file into a DataFrame
print(df.head(10))  # Print the first 5 rows of the DataFrame

df.info()  # Print information about the DataFrame
print(df.describe()) # Print summary statistics of the DataFrame
print(df.shape)
print(df.columns)  # Print the column names of the DataFrame

# Filter and export csv file

pulse = df['Pulse']  # Extract the 'Pulse' column from the DataFrame
print(pulse.head())

timeCal = df[['Duration','Calories']]

filtered_df = df[df['Duration']>60]

filtered_df.to_csv("./Lec04/filtered_data.csv", index=False)

# OS module

import os
os.getcwd()
os.chdir("./Lec04")
os.getcwd()
os.chdir('C:\\E\\PyExC')
os.chdir(r'C:\E\PyExC')  # Use raw string to avoid escape characters
os.listdir(path="./Lec04")  # List files in the specified directory

for (root,dirs,files) in os.walk("./",topdown=True):
    print(root)
    print(dirs)
    print(files)
    print("-----------------------------")




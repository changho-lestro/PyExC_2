import numpy as np


## Create Arrays
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a.shape
a.dtype

arrange_a=np.arange(0,1,0.2)

linspace_a = np.linspace(0,2*np.pi,4)

zero_mat=np.zeros((2,3))
np.ones((2,3))
np.diag([1,1,1]).

np.random.random((2,3))

a = np.random.normal(loc=1.0,scale=2.0,size=(2,2))
np.savetxt("a_out.txt",a)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a[1,2])
elem_a=a[1,2]

d3_a = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(d3_a[0,1,2])  # Accessing the element at index [0,1,2]


## Slicing Arrays

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a[1]
a[1,:]
a[1,1:]
a[:1,1:]

# Array operations
a = np.arange(4) # [0,1,2,3]
b = np.array([2,3,2,4])

a*b
b-a


## Series in Pandas

import pandas as pd

a = [1,7,2]
mySeries=pd.Series(a)
mySeries=pd.Series(a,index=["x","y","z"])

print(mySeries["y"])

# Create Series using a dictionary

calories = {"day1": 420, "day2": 380,"day3":390}

pd.Series(calories)


## Create DataFrame

data = {"calories":[420,380,390],"duration":[50,40,45]}

df = pd.DataFrame(data)

print(df)

# Read CSV file into DataFrame

df = pd.read_csv(r"C:\E\PyExC\Lec05\05Salaries.csv")
print(df)
df.head()  # Display the first 5 rows
df.tail()

df['salary'].dtype
df.dtypes

df.columns[2]  # Accessing the third column name
len(df.columns)

df.values[0,1]  # Get values as Array
df.values
df.values[9,:]

df.describe()

### Data Cleaning

# Read data frame from CSV file
flights_raw = pd.read_csv(r"C:\E\PyExC\Lec05\05flights.csv")
flights_raw.head()

# Count NaN values in each column
sum(flights_raw.isnull().any(axis=1)) # True : 1 and False : 0

# Filter rows with any NaN values
null_df=flights_raw[flights_raw.isnull().any(axis=1)]

# Remove rows with any NaN values
flights = flights_raw.dropna()
sum(flights.isnull().any(axis=1))

print(flights.to_string())  # Takes a long time for large DataFrames


### Advanced: Data Cleaning

df = pd.read_csv(r"C:\E\PyExC\Lec05\W3data.csv")
df.shape
# 1. Cleaning empty values

new_df=df.dropna()
print(new_df)
print(new_df.to_string())

df_fill=df.fillna(130)

avg_x = df["Calories"].mean()  # x : average of Calories column : 304.68
med_x = df["Calories"].median()
mode_x = df["Calories"].mode()[0]
df_fill_mean = df.fillna(avg_x)
df_fill_med = df.fillna(med_x)

# 2.Correct wrong data format

df['Date'] = pd.to_datetime(df['Date'],format='mixed')
print(df.to_string())

df_noNulldate=df.dropna(subset=['Date'])
print(df_noNulldate.to_string())


# 3. Correct Wrong data
df.loc[7,"Duration"]= 45  # Replacing value
print(df.to_string())

for x in df.index:
    if df.loc[x,"Duration"] > 120:
        df.loc[x,"Duration"] = 120  # Correcting wrong data

print(df.to_string())

# 4. Remove duplicates
df.duplicated() # To see if there are duplicates based on row
sum(df.duplicated())  # one duplicated row

df_rmDup=df.drop_duplicates() # Remove duplicates
df_rmDup.shape


### Data Transformation

# Groupby

df = pd.read_csv(r"C:\E\PyExC\Lec05\05Salaries.csv")
df.head()

df_rank = df.groupby('rank').mean() #
df.dtypes

df.describe()
df_grouped=df.groupby('rank')[["yrs.since.phd","yrs.service","salary"]].mean()

# Compute the average departure delay for each carrier

avg_dep_delay = flights.groupby("carrier")['dep_delay'].mean().reset_index(name="avg_dep_delay")
print(avg_dep_delay.to_string())

# Objective: Count flights between each pair of origin and destination

od_cnts=flights.groupby(['origin','dest']).size().reset_index(name="Flight_Count")
print(od_cnts.to_string())

# Aggregation

flights[['dep_delay','arr_delay']].agg(['mean','min','max'])

# Pivot

carrier_month=flights.groupby(['carrier','month']).size().reset_index(name="flight_count")
carrier_month.head()

pivot_table=(carrier_month.pivot(
    index='carrier',
    columns='month',
    values='flight_count'
).fillna(0).astype(int))

print(pivot_table.to_string())

# Melt : Pivot table to long format

melted_df=pivot_table.reset_index().melt(
    id_vars='carrier',
    var_name='month',
    value_name='flight_count'
)

melted_df.head()

# Concatenation

jan_flights = flights[flights['month']==1]
feb_flights = flights[flights['month']==2]

conc_df=pd.concat([jan_flights,feb_flights],ignore_index=True)
conc_df.head()
conc_df.tail()

# Merge data frames
carriers = pd.DataFrame({
    'carrier': ['AA','DL','UA'],
    'airline_name':['American Airlines','Delta Air Lines','United Airlines']
})

carriers.head()

merged_carriers=flights.merge(
    carriers,
    on='carrier',
    how='left'
)

print(merged_carriers.to_string())

# Sorting

df.head()
df.columns
df_sorted = df.sort_values(by='yrs.service', ascending = False)

df_sorted_two = df.sort_values(by=['yrs.service','salary'],ascending =[True,False])
df_sorted_two


#### Matplot to draw plots

import matplotlib.pyplot as plt

years = [1983, 1984, 1985, 1986, 1987]
tot_pop = [8939007, 8954518, 8960387, 8956741, 8943721]

plt.plot(years,tot_pop)
plt.title("Year vs Population in Bulgaria")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.show()

# Line plot
plt.plot(years,tot_pop)
plt.title("Year vs Population in Bulgaria")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.show()

# Scatter plot

plt.scatter(years,tot_pop)
plt.title("Scatter: Year vs Population in Bulgaria")
plt.xlabel("Year")
plt.ylabel("Total Population")
plt.show()



# Bar plot
df_grouped.head()

plt.bar(df_grouped.index,df_grouped["salary"])
plt.show()


# Two Histrograms in a set

data = np.random.randn(1000)
f, (ax1,ax2) = plt.subplots(1,2,figsize=(6,3))

# Histogram (pdf)
ax1.hist(data,bins=30,color='blue')
ax2.hist(data,bins=30,color='red',cumulative=True)

plt.show()
plt.savefig('histogram.png')



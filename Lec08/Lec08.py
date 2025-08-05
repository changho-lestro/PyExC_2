import requests

url = 'https://jsonplacceholder.typicode.com/posts/1'
response = requests.get(url)

print(response.status_code)
response.raise_for_status()

data= response.json()
print(data)

# Shortcut key to execute the highlighted code: Alt + Shift + E


import requests

url = 'https://jsonplaceholder.typicode.com/posts'  # Corrected URL
id_val = 5
params = {'userId':id_val}
response = requests.get(url,params=params) #  get with parameters

print(response.status_code)
response.raise_for_status()

data= response.json()
print(f"Found {len(data)} posts for user {id_val}.")
print(data[0])

# Shortcut key to execute the highlighted code: Alt + Shift + E


new_post = {'title': 'My new post','body':"Hello, World!",'userId': 1 }
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.post(url,json=new_post)

print(response.status_code)
created_post = response.json()
print(created_post)



# Census API key
api_key="538897fae0f36ef60c46c30c96cedcea135463e4"
year = 2021
dataset = 'acs/acs5'

base_url = f'https://api.census.gov/data/{year}/{dataset}'

# Parameters for the request
params = {
    'get' : 'NAME,B01001_001E,B19013_001E',  # Name is the geographic name
    'for': 'state:*',  # Get data for all states
    'key': api_key
}

# Send GET request to the Census API
response = requests.get(base_url,params=params)
response.raise_for_status()

data = response.json()

# The first row
headers = data[0]

# The rest are the data rows
states_data = data[1:]

# Create a list of dictionaries for each state
state_dicts = []

for row in states_data:
    state = {
        'name' : row[0],
        'population': int(row[1]),
        'median_income': int(row[2]),
        'state_code': row[3]
    }
    state_dicts.append(state)


import pandas as pd
df = pd.DataFrame(state_dicts)
df.to_csv('./lec08/state_dicts.csv', index=False) # Export data Frame to CSV

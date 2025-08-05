import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)

print(response.status_code)

data=response.json()
print(data)
print(data['title'])


new_post = {
'title': 'My New Post', 'body': 'Hello, World!', 'userId': 1
}

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.post(url, json=new_post)

print(response.status_code) # Should be 201 created_post = response.json() print(created_post)
created_post = response.json()
print(created_post)

import requests
import csv

url = 'https://restcountries.com/v3.1/independent?status=true'
response = requests.get(url)
response.raise_for_status()
countries_data = response.json()

len(countries_data)
type(countries_data)
type(countries_data[0])

import pandas as pd
df = pd.DataFrame(countries_data)
print(df.loc[0,:])


processed_countries = []
for country in countries_data: # Extract name
    name = country['name']['common']

    # Extract population (use 0 if not present)
    population = country.get('population', 0)

    # Extract area (use 0 if not present)
    area = country.get('area', 0)

    # Extract continent (first continent in the list)
    continents = country.get('continents', [])
    continent = continents[0] if continents else 'Unknown'

    # Extract languages (combine into a comma-separated string)
    languages = country.get('languages', {})
    language_names = list(languages.values())  # Get the list of language names
    languages_str = ', '.join(language_names) if language_names else 'None'

    # Append to processed list
    processed_countries.append({
    'name': name, 'population': population, 'area': area, 'continent': continent, 'languages': languages_str
    })


output_file = 'countries_data.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'population', 'area', 'continent', 'languages']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for country in processed_countries:
        writer.writerow(country)

df = pd.DataFrame(processed_countries)
import requests
from bs4 import BeautifulSoup
import yaml

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Municipalities_of_Honduras'

# Send a request to fetch the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the municipalities
table = soup.find('table', {'class': 'wikitable'})

# Extract municipality names from the table
municipalities = []
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    if cells:
        municipality_name = cells[0].text.strip()
        municipalities.append(municipality_name)

# Export to txt file
with open('honduras_municipalities.txt', 'w', encoding='utf-8') as f:
    f.write(str(municipalities))

# Export to yml file
yaml_data = {'municipalities': municipalities}
with open('honduras_municipalities.yml', 'w', encoding='utf-8') as f:
    yaml.dump(yaml_data, f, allow_unicode=True)

print(f"Exported {len(municipalities)} municipalities to honduras_municipalities.txt and honduras_municipalities.yml")

import requests
from bs4 import BeautifulSoup

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

print(municipalities)

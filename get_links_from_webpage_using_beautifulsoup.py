# This program scrapes all of the links of a given website

from bs4 import BeautifulSoup
import requests


# Get data from the server using GET protocal
response = requests.get('https://stackoverflow.com/')

# Convert the raw response to text
data = response.text

# HTML Parser
soup = BeautifulSoup(data, 'html.parser')

# Get all URLS from a tags with attribute href
for link in soup.find_all('a'):
    print(link.get('href'))

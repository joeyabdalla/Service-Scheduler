import requests
from bs4 import BeautifulSoup

URL = "https://example.com/businesses"  # replace with the actual URL you want to scrape
response = requests.get(URL)

soup = BeautifulSoup(response.content, 'lxml')  # Use 'lxml' as the parser

businesses = []

for business_div in soup.find_all('div', class_='business'):  # Adjust based on actual class name or HTML element
    business_name = business_div.find('h2').text
    business_description = business_div.find('p').text
    businesses.append({
        'name': business_name,
        'description': business_description
    })

print(businesses)

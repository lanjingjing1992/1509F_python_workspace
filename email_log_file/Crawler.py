from bs4 import BeautifulSoup
import requests
response = requests.get('http://jecvay.com')
soup=BeautifulSoup(response.text,'html.parser')
print(soup.title.text)
for x in soup.find_all('a'):
    print(x['href'])

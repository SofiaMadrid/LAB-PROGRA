import requests
from bs4 import BeautifulSoup
#Con el web scraping obtenemos las fechas de los proximos conciertos de la banda ms 
r = requests.get('https://www.wegow.com/es-mx/artistas/banda-ms').text
soup = BeautifulSoup(r, 'lxml')
links = soup.find(class_="events-list").get_text()

print(links)

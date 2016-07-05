import requests
from bs4 import BeautifulSoup

hostname = "http://www.nfl.com/player/aaronrodgers/2506363/careerstats"
content = requests.get(hostname)

souper = BeautifulSoup(content.text, "html.parser")

elements = souper.find(class_="data-table1")

for stats in elements.find_all():
    print(stats)

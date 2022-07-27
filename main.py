import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.worldometers.info/coronavirus/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find(class_="maincounter-number")
structure = {
    "number" : result.text,
}

jsonData = json.dumps(structure, indent=1)

with open("test.json", "w") as outfile:
    outfile.write(jsonData)

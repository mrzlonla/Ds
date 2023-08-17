import requests
from bs4 import BeautifulSoup
import json

url = "https://teledeclaration-dgi.cm/modules/immatriculation/Consultation/listecontribuable.aspx"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# Get list of all town
list_of_town = []

for i, option in enumerate(soup.select("[name='TabContainer3$TabPanelCard$ddlCENTRE_DE_RATTACHEMENT'] option")):
    if i == 0:
        continue

    list_of_town.append([option.get("value").strip(), option.text.strip()])

for value, name in list_of_town:
    response = requests.post(url, data={
        "TabContainer3$TabPanelCard$ddlCENTRE_DE_RATTACHEMENT": value
    })

    soup = BeautifulSoup(response.content, "html.parser")


    for i, tr in enumerate(soup.select("#TabContainer3_TabPanelCard_DataGrid1 tr")):
        if i == 0:
            continue

        print(tr)

input()
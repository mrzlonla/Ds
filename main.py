import time

import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://teledeclaration-dgi.cm/modules/immatriculation/Consultation/listecontribuable.aspx"

# Initialiser le navigateur Chrome
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Pour exécuter Chrome en mode headless (sans interface graphique)
driver = webdriver.Chrome(options=options)

index: int = 1

while True:
    # Accéder à la page
    driver.get(url)

    # Attendre que l'élément select soit chargé
    wait = WebDriverWait(driver, 10)
    select_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[name='TabContainer3$TabPanelCard$ddlCENTRE_DE_RATTACHEMENT']")))

    # Récupérer les options de l'élément select
    options = select_element.find_elements(By.TAG_NAME, "option")[index:]

    if not options:
        break
    else:
        option = options[0]
        option_text = option.text
        print(f"Sélection de l'option : {option_text}")
        option.click()  # Sélectionner l'option en cliquant dessus

        button = driver.find_element(By.CSS_SELECTOR, "[id='TabContainer3_TabPanelCard_btnAfficher2']")
        button.click()

        time.sleep(10)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        for i, tr in enumerate(soup.select("#TabContainer3_TabPanelCard_DataGrid1 tr")):
            if i == 0:
                continue
            print(tr)

    index += 1

# Fermer le navigateur
driver.quit()


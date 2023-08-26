import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

url = "https://teledeclaration-dgi.cm/modules/immatriculation/Consultation/listecontribuable.aspx"

# Initialiser le navigateur Firefox
options = webdriver.FirefoxOptions()
# options.headless = True  # Pour exécuter Firefox en mode headless (sans interface graphique)
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

index = 1

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


    index += 1

# Fermer le navigateur
driver.quit()

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.action_chains import ActionChains

#CHROMEDRIVER LOCALISATION - you need to put chromedriver.exe in diskname:/Program Files (x86)
os.environ['PATH'] += r"C:/Program Files (x86)"

#initialize webdriver options for Google Chrome
options = webdriver.ChromeOptions()

# UserData (folder - desktop)
options.add_argument("--user-data-dir=C:\\Users\\akasi\\Desktop\\python_scrape")
options.page_load_strategy = 'normal'

#maximize
options.add_argument("start-maximized")

#  Chrome is being controlled by automated test software // staying undetected
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

# loading driver
driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

item_link = str(input("Podaj link do produktu: "))

if "zalando-lounge" in item_link:
    try:
        driver.get(item_link)
    except:
        print("Podaj odpowiedni link")
else:
    print("Nieprawidłowy link. Uruchom jeszcze raz program.")

driver.implicitly_wait(2) # waiting for page to load (safety) - ONLY IMPLEMENT ONCE. It is the maximum time we can wait
# for action to happen (finding some id in HTML script, etc.


""" PRODUCT THAT WE WANT - DATA """
additional_products = str(input("Czy widzisz produkty pokrewne? T/N: "))
additional_products_state = 0
if additional_products.upper() == "T":
    additional_products_state = 2
else:
    additional_products_state = 1

which_size = int(input("Podaj ktory rozmiar chcesz wybrac (cyfra od lewej, licząc od 1): "))

size_auto_path = f"//*[@id='article-information']/section[{additional_products_state}]/div[2]/div[3]/div[{which_size}]/button"
add_to_cart_ID = "addToCartButton"

### loop, check if the product is added to the cart
#cart_ID = "header-cart"
#cart = driver.find_element(By.ID, cart_ID)
#flag = True
#cart_xpath = '//*[@id="inner-wrapper"]/div/header/div/div[2]/nav/ul/li[3]/div/div/div/span/span'
#cart.click()
#driver.page_source.__contains__("W Twoim koszyku nie ma zarezerwowanych artykułów"):

#################################
c = 0

time.sleep(5)

while True:
    choose_auto = driver.find_element(By.XPATH, size_auto_path)
    add_to_cart = driver.find_element(By.ID, add_to_cart_ID)
    try:
        choose_auto.click()
        add_to_cart.click()
    except:
        c += 1
        print(f"error: {c}")
    driver.refresh()
    time.sleep(1)

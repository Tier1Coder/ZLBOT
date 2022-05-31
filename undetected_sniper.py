import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

if __name__ == '__main__':
    # initialize webdriver options for Google Chrome
    options = uc.ChromeOptions()

    # UserData (folder - desktop)
    options.add_argument("--user-data-dir=C:\\Users\\akasi\\Desktop\\python_scrape")

    # loading driver
    driver = uc.Chrome(options=options)

    driver.get("https://www.zalando-lounge.pl/event#")

    item_link = str(input("Podaj link do produktu: "))

    if "zalando-lounge" in item_link:
        try:
            driver.get(item_link)
        except:
            print("Podaj odpowiedni link")
    else:
        print("Nieprawidłowy link. Uruchom jeszcze raz program.")

    driver.implicitly_wait(2)  # waiting for page to load (safety) - ONLY IMPLEMENT ONCE. It is the maximum time we can wait
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

    c = 0

    time.sleep(2)

    while True:
        try:
            choose_auto = driver.find_element(By.XPATH, size_auto_path)
            add_to_cart = driver.find_element(By.ID, add_to_cart_ID)
            choose_auto.click()
            add_to_cart.click()
            time.sleep(2)
            driver.refresh()
        except ElementClickInterceptedException:
            print("Produkt wyprzedany, kończę program...")
            break




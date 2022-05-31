import os
from selenium import webdriver

os.environ['PATH'] += r"C:/Program Files (x86)"

options = webdriver.ChromeOptions()

options.add_argument("--user-data-dir=C:\\Users\\akasi\\Desktop\\python_scrape")
options.page_load_strategy = 'normal'


options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.zalando-lounge.pl/event#")

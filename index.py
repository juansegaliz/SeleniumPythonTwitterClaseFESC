from pprint import pprint
from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pprint import pprint
import time 

def waitUntilReady(driver, delay, by, value_by):
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by, value_by)))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

driver = webdriver.Chrome('./chromedriver')
#PATH = "C:\\Data\\Universidad\\twitterselenium\\chromedriver.exe"
#driver = webdriver.Chrome(PATH)

driver.get("https://twitter.com/AlvaroUribeVel")
waitUntilReady(driver, 5, By.CSS_SELECTOR, "div[data-testid=cellInnerDiv]")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
elements = driver.find_elements(By.CSS_SELECTOR, "div[data-testid=cellInnerDiv]")
pprint(elements)
#driver.close()

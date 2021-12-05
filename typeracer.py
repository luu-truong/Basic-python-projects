# importing components and module
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Variables
PATH = '/Users/luunhattruong/Downloads/chromedriver'
URL = 'https://play.typeracer.com/'
DELAY = 100 # This value determines typing speed

# Initialize the browser and url
driver = webdriver.Chrome(PATH)
driver.get(URL)

# * Ace the typing race


def get_text(driver):
    wait = WebDriverWait(driver, 30)
    text_elements = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//span[@unselectable='on']")))
    text_parts = [el.text for el in text_elements]
    race_text = ''
    if len(text_parts) == 3:
        race_text = f'{text_parts[0]}{text_parts[1]} {text_parts[2]}'
    elif len(text_parts) == 2:         # One-letter first word
        race_text = f'{text_parts[0]} {text_parts[1]}'
    return race_text


def auto_typing():
    race_text = get_text(driver)
    
    type_wait = WebDriverWait(driver, 30)
    typing_area = type_wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@class='txtInput']")))

    for letter in race_text:
        typing_area.send_keys(letter)
        delay = DELAY/1000
        time.sleep(delay)




while True:
    auto_typing()
    time.sleep(5) # you can adjust this value to your liking
    next_race_wait = WebDriverWait(driver, 30)
    next_race = next_race_wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Race again')]")))
    next_race.click()
    time.sleep(5) # you can adjust this value to your liking
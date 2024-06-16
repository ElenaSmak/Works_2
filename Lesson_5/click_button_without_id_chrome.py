from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#открыть сайт http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")

sleep(5)
search_button = "button"

button_input = driver.find_element(By.CSS_SELECTOR, search_button)
for n in range (0,3):
    button_input.send_keys(Keys.ENTER)

sleep(10)
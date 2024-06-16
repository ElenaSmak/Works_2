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

sleep(1)
for n in range (3):
    search_button = "button.btn-primary" 
    driver.find_element(By.CSS_SELECTOR, search_button).click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "h4").click()

sleep(1)
driver.quit()
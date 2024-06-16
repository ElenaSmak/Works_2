from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#открыть сайт http://uitestingplayground.com/classattr

driver.get("http://uitestingplayground.com/classattr")

sleep(5)

for n in range (3):
    blue_button = "button.btn-primary"
    result_input = driver.find_element(By.CSS_SELECTOR, blue_button).click()
    sleep(5)
    result_input.send_keys(Keys.ESCAPE)

sleep(5)
driver.quit()
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
driver.maximize_window()
#открыть сайт http://uitestingplayground.com/classattr
driver.get("http://uitestingplayground.com/classattr")

sleep(5)
search_button = "btn-primary"
result_input = driver.find_element(By.CSS_SELECTOR, search_button)
for n in range (0,3):
    result_input.send_keys(Keys.ENTER)


sleep(10)
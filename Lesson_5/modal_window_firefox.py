from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chromefirefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
driver.maximize_window()

#открыть  http://the-internet.herokuapp.com/entry_ad.
driver.get("http://the-internet.herokuapp.com/entry_ad.")

sleep(5)
search_delete = "div.modal-footer"
delete_input = driver.find_element(By.CSS_SELECTOR, search_delete).click()

sleep(1)
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
driver.maximize_window()

#открыть страницу
driver.get("http://the-internet.herokuapp.com/login")
sleep(5)
#ввести в поле текст tomsmith
search_field = "#username"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("tomsmith")
sleep(5)
#ввест в поле текст SuperSecretPassword!
search_field_p = "#password"
search_input = driver.find_element(By.CSS_SELECTOR, search_field_p)
search_input.send_keys("SuperSecretPassword!")


sleep(5)
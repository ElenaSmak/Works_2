from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
driver.maximize_window()

#открыть страницу
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(5)
#ввести в поле текст 1000
search_field = "input"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("1000")
sleep(5)
for n in range (0,4):
    search_input.send_keys(Keys.BACKSPACE)
    sleep(2)
search_input.send_keys("999")


sleep(5)
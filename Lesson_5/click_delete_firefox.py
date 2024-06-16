from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import FirefoxDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(service=FirefoxService(FirefoxDriverManager().install()))
driver.maximize_window()
#открыть сайт https://the-internet.herokuapp.com/
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

sleep(5)
search_delete = "button"
delete_input = driver.find_element(By.CSS_SELECTOR, search_delete)
for n in range (0,5):
    delete_input.send_keys(Keys.ENTER)

result_delete = driver.find_element(By.CSS_SELECTOR, "button.added-manually").text
print (len(result_delete))

sleep(10)
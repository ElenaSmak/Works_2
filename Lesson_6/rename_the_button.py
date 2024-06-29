# задача 2 переименовать кнопку
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("http://uitestingplayground.com/textinput")

new_button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")

new_button_name.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(txt)
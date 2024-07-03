from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#здесь команды для импорта и инициализации драйвера
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
#driver.implicitly_wait(20)
#открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

insert = "#delay"
insert_input = driver.find_element(By.CSS_SELECTOR, insert)
insert_input.send_keys("45")
sleep(2)

press_button_7 = "#calculator > div.keys > span:nth-child(1)"
result_1 = driver.find_element(By.CSS_SELECTOR, press_button_7).click()


press_button_plus = "#calculator > div.keys > span:nth-child(4)"
result_2 = driver.find_element(By.CSS_SELECTOR, press_button_plus).click()


press_button_8 = "#calculator > div.keys > span:nth-child(2)"
result_3 = driver.find_element(By.CSS_SELECTOR, press_button_8).click()
sleep(2)

equal = "#calculator > div.keys > span.btn.btn-outline-warning"
result_4 = driver.find_element(By.CSS_SELECTOR, equal).click()
sleep(2)

#ожидание выполнения условий:

waiter = WebDriverWait(driver, 60, 0.1)
waiter.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
)

sleep(2)
driver.quit()
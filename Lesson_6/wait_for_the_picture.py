# задача 3 дождаться картинки
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
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


waiter = WebDriverWait(driver, 40, 0.1) #одна десятая секунды частота опроса

#ожидание выполнения условий:
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)


#читается: найди текст элемента и выведи его в терминал

src = driver.find_element(By.CSS_SELECTOR, "img#award").get_attribute("src")
print( "src = ", src)
driver.quit()
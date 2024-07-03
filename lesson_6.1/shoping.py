# задание 3 автотест на покупку в интернет магазине
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#открыть страницу
driver.get("https://www.saucedemo.com/")
sleep(2)

#ввести в поле Username текст standard_user
search_field = "#user-name"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("standard_user")

sleep(2)
#ввести в поле Login текст secret_sauce  
search_field_2 = "#password"
search_input_2 = driver.find_element(By.CSS_SELECTOR, search_field_2)
search_input_2.send_keys("secret_sauce")

sleep(2)
#нажать кнопку Login
search_field_3 = "#login-button"
search_input_3 = driver.find_element(By.CSS_SELECTOR, search_field_3).click()

sleep(2)


# добавить в корзину Sauce Labs Backpack
search_field_4 = "#add-to-cart-sauce-labs-backpack"
search_input_4 = driver.find_element(By.CSS_SELECTOR, search_field_4).click()

sleep(2)

# добавить в корзину Sauce Labs Bolt T-Shirt
search_field_5 = "#add-to-cart-sauce-labs-bolt-t-shirt"
search_input_5 = driver.find_element(By.CSS_SELECTOR, search_field_5).click()

sleep(2)

# добавить в корзину Sauce Labs Onesie
search_field_6 = "#add-to-cart-sauce-labs-onesie"
search_input_6 = driver.find_element(By.CSS_SELECTOR, search_field_6).click()

sleep(2)

#перейти в корзину
search_field_7 = "#shopping_cart_container > a"
search_input_7 = driver.find_element(By.CSS_SELECTOR, search_field_7).click()

sleep(2)

#нажать cheskout
search_field_8 = "#checkout"
search_input_8 = driver.find_element(By.CSS_SELECTOR, search_field_8).click()

sleep(2)

#ввести в поле First name 
search_field_9 = "#first-name"
search_input_9 = driver.find_element(By.CSS_SELECTOR, search_field_9)
search_input_9.send_keys("Вася")
#search_input_9.send_keys(Keys.TAB)
sleep(2)

#ввести в поле Last name 
search_field_9 = "#last-name"
search_input_9 = driver.find_element(By.CSS_SELECTOR, search_field_9)
search_input_9.send_keys("Васильев")
#search_input_9.send_keys(Keys.TAB)
sleep(2)

#ввести в поле почтовый код
search_field_9 = "#postal-code"
search_input_9 = driver.find_element(By.CSS_SELECTOR, search_field_9)
search_input_9.send_keys("12345678")
#search_input_9.send_keys(Keys.TAB)
sleep(2)

#  нажать на кнопку Continue 
search_field_10 = "#continue"
search_input_10 = driver.find_element(By.CSS_SELECTOR, search_field_10).click()
sleep(5)
#  прочитать чему равна итоговая стоимость 
txt = driver.find_element(By.CSS_SELECTOR, "#checkout_summary_container > div > div.summary_info > div.summary_total_label").text

print("текст = ", txt)
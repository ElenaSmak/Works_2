from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

#открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
sleep(2)

#ввести в поле First name текст Иван
search_field = "input.form-control"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Иван")
search_input.send_keys(Keys.TAB)
sleep(2)
#ввести в поле Last name текст Петров
search_field_2 = "body > main > div > form > div:nth-child(1) > div:nth-child(2) > label > input"
search_input_2 = driver.find_element(By.CSS_SELECTOR, search_field_2)
search_input_2.send_keys("Петров")
search_input_2.send_keys(Keys.TAB)
sleep(2)
#ввести в поле Address текст Ленина, 55-3
search_field_3 = "body > main > div > form > div:nth-child(2) > div.col-md-4.py-2 > label > input"
search_input_3 = driver.find_element(By.CSS_SELECTOR, search_field_3)
search_input_3.send_keys("Ленина, 55-3")
search_input_3.send_keys(Keys.TAB)
sleep(2)

# поле Zip code оставить пустым
search_input_3.send_keys(Keys.TAB)

#ввести в поле City текст Москва
search_field_4 = "body > main > div > form > div:nth-child(2) > div:nth-child(3) > label > input"
search_input_4 = driver.find_element(By.CSS_SELECTOR, search_field_4)
search_input_4.send_keys("Москва")
search_input_4.send_keys(Keys.TAB)
sleep(2)

#ввести в поле Country текст Россия
search_field_5 = "body > main > div > form > div:nth-child(2) > div:nth-child(4) > label > input"
search_input_5 = driver.find_element(By.CSS_SELECTOR, search_field_5)
search_input_5.send_keys("Россия")
search_input_5.send_keys(Keys.TAB)
sleep(2)

#ввести в поле Email текст test@skypro.com
search_field_6 = "body > main > div > form > div:nth-child(3) > div:nth-child(1) > label > input"
search_input_6 = driver.find_element(By.CSS_SELECTOR, search_field_6)
search_input_6.send_keys("test@skypro.com")
search_input_6.send_keys(Keys.TAB)
sleep(2)

#ввести в поле Phone number текст +7985899998787
search_field_7 = "body > main > div > form > div:nth-child(3) > div:nth-child(2) > label > input"
search_input_7 = driver.find_element(By.CSS_SELECTOR, search_field_7)
search_input_7.send_keys("+7985899998787")
search_input_7.send_keys(Keys.TAB)
sleep(2)

#ввести в поле Job position текст QA
search_field_8 = "body > main > div > form > div:nth-child(4) > div:nth-child(1) > label > input"
search_input_8 = driver.find_element(By.CSS_SELECTOR, search_field_8)
search_input_8.send_keys("QA")
search_input_8.send_keys(Keys.TAB)
sleep(2)

#ввести в поле Company position текст SkyPro
search_field_9 = "body > main > div > form > div:nth-child(4) > div:nth-child(2) > label > input"
search_input_9 = driver.find_element(By.CSS_SELECTOR, search_field_9)
search_input_9.send_keys("SkyPro")
search_input_9.send_keys(Keys.TAB)
sleep(2)

#  нажать на кнопку Submit
search_field_10 = "body > main > div > form > div:nth-child(5) > div > button"
search_input_10 = driver.find_element(By.CSS_SELECTOR, search_field_10).click()
sleep(5)

# проверить что поле Zip подсвечен красным
clr_zip = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("color")
print( "цвет = ", clr_zip)

# проверить что остальные поля подсвечены зеленым
# имя
clr_fn = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(4) > div:nth-child(1)").value_of_css_property("color")
print( "цвет = ", clr_fn)
#  фамилия
clr_ln = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(4) > div:nth-child(2)").value_of_css_property("color")
print( "цвет = ", clr_ln)

#  адрес
clr_adr = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(5) > div.col-md-4.py-2").value_of_css_property("color")
print( "цвет = ", clr_adr)

#  город
clr_city = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(5) > div:nth-child(3)").value_of_css_property("color")
print( "цвет = ", clr_city)

#  страна
clr_ctr = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(5) > div:nth-child(4)").value_of_css_property("color")
print( "цвет = ", clr_ctr)

#  Email
clr_eml = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(6) > div:nth-child(1)").value_of_css_property("color")
print( "цвет = ", clr_eml)

#  Phone
clr_ph = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(6) > div:nth-child(2)").value_of_css_property("color")
print( "цвет = ", clr_ph)

#  Job
clr_job = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(7) > div:nth-child(1)").value_of_css_property("color")
print( "цвет = ", clr_job)

#  Company
clr_cmp = driver.find_element(By.CSS_SELECTOR, "body > main > div > div:nth-child(7) > div:nth-child(2)").value_of_css_property("color")
print( "цвет = ", clr_cmp)

#driver.quit()